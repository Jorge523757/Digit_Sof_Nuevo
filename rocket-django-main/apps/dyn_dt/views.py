import requests, base64, json, csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.utils.safestring import mark_safe
from django.conf import settings
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.views import View
from django.db import models
from pprint import pp 
from django import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from administrador.forms import *
from administrador.models import *

from apps.dyn_dt.models import ModelFilter, PaginaPrincipalItems, HideShowFilter
from apps.dyn_dt.utils import user_filter

from cli import *

# Create your views here.

def index(request):
    
    context = {
        'routes' : settings.DYNAMIC_DATATB.keys(),
        'parent': 'apps',
        'segment': 'dynamic_dt'
    }

    return render(request, 'dyn_dt/index.html', context)

def create_filter(request, model_name):
    model_name = model_name.lower()
    if request.method == "POST":
        keys = request.POST.getlist('key')
        values = request.POST.getlist('value')
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]

            ModelFilter.objects.update_or_create(
                parent=model_name,
                key=key,
                defaults={'value': value}
            )

        return redirect(reverse('model_dt', args=[model_name]))


def create_PaginaPrincipal_items(request, model_name):
    model_name = model_name.lower()
    if request.method == 'POST':
        items = request.POST.get('items')
        PaginaPrincipal_items, created = PaginaPrincipalItems.objects.update_or_create(
            parent=model_name,
            defaults={'items_per_PaginaPrincipal':items}
        )
        return redirect(reverse('model_dt', args=[model_name]))


def create_hide_show_filter(request, model_name):
    model_name = model_name.lower()
    if request.method == "POST":
        data_str = list(request.POST.keys())[0]
        data = json.loads(data_str)

        HideShowFilter.objects.update_or_create(
            parent=model_name,
            key=data.get('key'),
            defaults={'value': data.get('value')}
        )

        response_data = {'message': 'Model updated successfully'}
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_filter(request, model_name, id):
    model_name = model_name.lower()
    filter_instance = ModelFilter.objects.get(id=id, parent=model_name)
    filter_instance.delete()
    return redirect(reverse('model_dt', args=[model_name]))


def get_model_field_names(model, field_type):
    """Returns a list of field names based on the given field type."""
    return [
        field.name for field in model._meta.get_fields() 
        if isinstance(field, field_type)
    ]

def model_dt(request, aPath):
    aModelName  = None
    aModelClass = None
    choices_dict = {}

    if aPath in settings.DYNAMIC_DATATB.keys():
        aModelName  = settings.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )
    
    #db_fields = [field.name for field in aModelClass._meta.get_fields() if not field.is_relation]
    db_fields = [field.name for field in aModelClass._meta.fields]
    fk_fields = get_model_fk_values(aModelClass)
    db_filters = []
    for f in db_fields:
        if f not in fk_fields.keys():
            db_filters.append( f )

    for field in aModelClass._meta.fields:
        if field.choices:
            choices_dict[field.name] = field.choices

    field_names = []
    for field_name in db_fields:
        fields, created = HideShowFilter.objects.get_or_create(key=field_name, parent=aPath.lower())
        if fields.key in db_fields:
            field_names.append(fields)
    
    model_series = {}
    for f in db_fields:
        f_values = list ( aModelClass.objects.values_list( f, flat=True) )
        model_series[ f ] = ', '.join( str(i) for i in f_values)

    # model filter
    filter_string = {}
    filter_instance = ModelFilter.objects.filter(parent=aPath.lower())
    for filter_data in filter_instance:
        if filter_data.key in db_fields: 
            filter_string[f'{filter_data.key}__icontains'] = filter_data.value

    order_by = request.GET.get('order_by', 'id')
    if order_by not in db_fields:
        order_by = 'id'
    
    queryset = aModelClass.objects.filter(**filter_string).order_by(order_by)
    item_list = user_filter(request, queryset, db_fields, fk_fields.keys())

    # pagination
    PaginaPrincipal_items = PaginaPrincipalItems.objects.filter(parent=aPath.lower()).last()
    p_items = 25
    if PaginaPrincipal_items:
        p_items = PaginaPrincipal_items.items_per_PaginaPrincipal

    PaginaPrincipal = request.GET.get('PaginaPrincipal', 1)
    paginator = Paginator(item_list, p_items)

    try:
        items = paginator.PaginaPrincipal(PaginaPrincipal)
    except PaginaPrincipalNotAnInteger:
        return redirect(reverse('model_dt', args=[aPath]))
    except EmptyPaginaPrincipal:
        return redirect(reverse('model_dt', args=[aPath]))
    
    read_only_fields = ('id', )

    integer_fields = get_model_field_names(aModelClass, models.IntegerField)
    date_time_fields = get_model_field_names(aModelClass, models.DateTimeField)
    email_fields = get_model_field_names(aModelClass, models.EmailField)
    text_fields = get_model_field_names(aModelClass, (models.TextField, models.CharField))
    
    context = {
        'PaginaPrincipal_title': 'Dynamic DataTable - ' + aPath.lower().title(),
        'link': aPath,
        'field_names': field_names,
        'db_field_names': db_fields,
        'db_filters': db_filters,
        'items': items,
        'PaginaPrincipal_items': p_items,
        'filter_instance': filter_instance,
        'read_only_fields': read_only_fields,

        'integer_fields': integer_fields,
        'date_time_fields': date_time_fields,
        'email_fields': email_fields,
        'text_fields': text_fields,
        'fk_fields_keys': list( fk_fields.keys() ),
        'fk_fields': fk_fields ,
        'choices_dict': choices_dict,
        'parent': 'apps',
        'segment': 'dynamic_dt'
    }
    return render(request, 'dyn_dt/model.html', context)


@login_required(login_url='/accounts/login/')
def create(request, aPath):
    aModelClass = None

    if aPath in settings.DYNAMIC_DATATB.keys():
        aModelName  = settings.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )

    if request.method == 'POST':
        data = {}
        fk_fields = get_model_fk(aModelClass)

        for attribute, value in request.POST.items():
            if attribute == 'csrfmiddlewaretoken':
                continue

            # Process FKs    
            if attribute in fk_fields.keys():
                value = name_to_class( fk_fields[attribute] ).objects.filter(id=value).first()
            
            data[attribute] = value if value else ''

        aModelClass.objects.create(**data)

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/accounts/login/')
def delete(request, aPath, id):
    aModelClass = None

    if aPath in settings.DYNAMIC_DATATB.keys():
        aModelName  = settings.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )
    
    item = aModelClass.objects.get(id=id)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/accounts/login/')
def update(request, aPath, id):
    aModelClass = None

    if aPath in settings.DYNAMIC_DATATB.keys():
        aModelName  = settings.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )

    item = aModelClass.objects.get(id=id)
    fk_fields = get_model_fk(aModelClass)

    if request.method == 'POST':
        for attribute, value in request.POST.items():

            if attribute == 'csrfmiddlewaretoken':
                continue

            if getattr(item, attribute, value) is not None:

                # Process FKs    
                if attribute in fk_fields.keys():
                    value = name_to_class( fk_fields[attribute] ).objects.filter(id=value).first()

                setattr(item, attribute, value)
        
        item.save()

    return redirect(request.META.get('HTTP_REFERER'))



# Export as CSV
class ExportCSVView(View):
    def get(self, request, aPath):
        aModelName  = None
        aModelClass = None

        if aPath in settings.DYNAMIC_DATATB.keys():
            aModelName  = settings.DYNAMIC_DATATB[aPath]
            aModelClass = name_to_class(aModelName)

        if not aModelClass:
            return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )
        
        db_field_names = [field.name for field in aModelClass._meta.get_fields()]
        fields = []
        show_fields = HideShowFilter.objects.filter(value=False, parent=aPath.lower())
        
        for field in show_fields:
            if field.key in db_field_names:
                fields.append(field.key)
            else:
                print(f"Field {field.key} does not exist in {aModelClass} model.")

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{aPath.lower()}.csv"'

        writer = csv.writer(response)
        writer.writerow(fields)  # Write the header

        filter_string = {}
        filter_instance = ModelFilter.objects.filter(parent=aPath.lower())
        for filter_data in filter_instance:
            filter_string[f'{filter_data.key}__icontains'] = filter_data.value

        order_by = request.GET.get('order_by', 'id')
        queryset = aModelClass.objects.filter(**filter_string).order_by(order_by)

        items = user_filter(request, queryset, db_field_names)

        for item in items:
            row_data = []
            for field in fields:
                try:
                    row_data.append(getattr(item, field))
                except AttributeError:
                    row_data.append('') 
            writer.writerow(row_data)

        return response
    
   


# ===================== Administrador =====================

class AdministradorListView(ListView):
    model = Administrador
    template_name = 'administrador/listar_administrador.html'
    context_object_name = 'administradores'
    entidad = 'administrador'

class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:administrador_listar')
    entidad = 'administrador'

class AdministradorUpdateView(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:administrador_listar')
    entidad = 'administrador'

class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('apl:administrador_listar')
    entidad = 'administrador'

# ===================== Facturacion =====================

class FacturacionListView(ListView):
    model = Facturacion
    template_name = 'facturacion/listar_facturacion.html'
    context_object_name = 'facturaciones'
    entidad = 'facturacion'

class FacturacionCreateView(CreateView):
    model = Facturacion
    form_class = FacturacionForm
    template_name = 'facturacion/crear.html'
    success_url = reverse_lazy('apl:facturacion_listar')
    entidad = 'facturacion'

class FacturacionUpdateView(UpdateView):
    model = Facturacion
    form_class = FacturacionForm
    template_name = 'facturacion/crear.html'
    success_url = reverse_lazy('apl:facturacion_listar')
    entidad = 'facturacion'

class FacturacionDeleteView(DeleteView):
    model = Facturacion
    template_name = 'facturacion/eliminar.html'
    success_url = reverse_lazy('apl:facturacion_listar')
    entidad = 'facturacion'

# ===================== Cliente =====================

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/listar_cliente.html'
    context_object_name = 'clientes'
    entidad = 'cliente'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('apl:cliente_listar')
    entidad = 'cliente'

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('apl:cliente_listar')
    entidad = 'cliente'

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('apl:cliente_listar')
    entidad = 'cliente'

# ===================== Marca =====================

class MarcaListView(ListView):
    model = Marca
    template_name = 'Marca/listar_marca.html'
    context_object_name = 'marcas'
    entidad = 'marca'

class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'Marca/crear.html'
    success_url = reverse_lazy('apl:marca_listar')
    entidad = 'marca'

class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'Marca/crear.html'
    success_url = reverse_lazy('apl:marca_listar')
    entidad = 'marca'

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'Marca/eliminar.html'
    success_url = reverse_lazy('apl:marca_listar')
    entidad = 'marca'

# ===================== Proveedor =====================

class ProveedorListView(ListView):
    model = Proveedor
    template_name = "Proveedor/listar_proveedor.html"
    context_object_name = "proveedores"
    entidad = "proveedor"

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "Proveedor/crear.html"
    success_url = reverse_lazy("apl:proveedor_listar")
    entidad = "proveedor"

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "Proveedor/crear.html"
    success_url = reverse_lazy("apl:proveedor_listar")
    entidad = "proveedor"

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "Proveedor/eliminar.html"
    success_url = reverse_lazy("apl:proveedor_listar")
    entidad = "proveedor"

# ===================== Producto =====================

class ProductoListView(ListView):
    model = Producto
    template_name = "Producto/listar_producto.html"
    context_object_name = "productos"
    entidad = "producto"

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "Producto/crear.html"
    success_url = reverse_lazy("apl:producto_listar")
    entidad = "producto"

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "Producto/crear.html"
    success_url = reverse_lazy("apl:producto_listar")
    entidad = "producto"

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "Producto/eliminar.html"
    success_url = reverse_lazy("apl:producto_listar")
    entidad = "producto"

# ===================== Equipo =====================

class EquipoListView(ListView):
    model = Equipo
    template_name = "Equipo/listar_equipo.html"
    context_object_name = "equipos"
    entidad = "equipo"

class EquipoCreateView(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "Equipo/crear.html"
    success_url = reverse_lazy("apl:equipo_listar")
    entidad = "equipo"

class EquipoUpdateView(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "Equipo/crear.html"
    success_url = reverse_lazy("apl:equipo_listar")
    entidad = "equipo"

class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = "Equipo/eliminar.html"
    success_url = reverse_lazy("apl:equipo_listar")
    entidad = "equipo"



# ===================== Tecnico =====================

class TecnicoListView(ListView):
    model = Tecnico
    template_name = "Tecnicos/listar_tecnicos.html"
    context_object_name = "tecnicos"
    entidad = "tecnico"

class TecnicoCreateView(CreateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = "Tecnicos/crear.html"
    success_url = reverse_lazy("apl:tecnico_listar")
    entidad = "tecnico"

class TecnicoUpdateView(UpdateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = "Tecnicos/crear.html"
    success_url = reverse_lazy("apl:tecnico_listar")
    entidad = "tecnico"

class TecnicoDeleteView(DeleteView):
    model = Tecnico
    template_name = "Tecnicos/eliminar.html"
    success_url = reverse_lazy("apl:tecnico_listar")
    entidad = "tecnico"

# ===================== Orden de Servicio =====================

class OrdenServicioListView(ListView):
    model = OrdenServicio
    template_name = "Orden_Servicio/listar_orden_servicio.html"
    context_object_name = "ordenes"
    entidad = "ordenservicio"

class OrdenServicioCreateView(CreateView):
    model = OrdenServicio
    form_class = OrdenServicioForm
    template_name = "Orden_Servicio/crear.html"
    success_url = reverse_lazy("apl:ordenservicio_listar")
    entidad = "ordenservicio"

class OrdenServicioUpdateView(UpdateView):
    model = OrdenServicio
    form_class = OrdenServicioForm
    template_name = "Orden_Servicio/crear.html"
    success_url = reverse_lazy("apl:ordenservicio_listar")
    entidad = "ordenservicio"

class OrdenServicioDeleteView(DeleteView):
    model = OrdenServicio
    template_name = "Orden_Servicio/eliminar.html"
    success_url = reverse_lazy("apl:ordenservicio_listar")
    entidad = "ordenservicio"

# ===================== Servicio Tecnico =====================

class ServicioTecnicoListView(ListView):
    model = ServicioTecnico
    template_name = "Servicio_Tecnico/listar_servicio_tecnico.html"
    context_object_name = "servicios"
    entidad = "serviciotecnico"

class ServicioTecnicoCreateView(CreateView):
    model = ServicioTecnico
    form_class = ServicioTecnicoForm
    template_name = "Servicio_Tecnico/crear.html"
    success_url = reverse_lazy("apl:serviciotecnico_listar")
    entidad = "serviciotecnico"

class ServicioTecnicoUpdateView(UpdateView):
    model = ServicioTecnico
    form_class = ServicioTecnicoForm
    template_name = "Servicio_Tecnico/crear.html"
    success_url = reverse_lazy("apl:serviciotecnico_listar")
    entidad = "serviciotecnico"

class ServicioTecnicoDeleteView(DeleteView):
    model = ServicioTecnico
    template_name = "Servicio_Tecnico/eliminar.html"
    success_url = reverse_lazy("apl:serviciotecnico_listar")
    entidad = "serviciotecnico"

# ===================== Venta =====================

class VentaListView(ListView):
    model = Venta
    template_name = "Ventas/listar_ventas.html"
    context_object_name = "ventas"
    entidad = "venta"

class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy("apl:venta_listar")
    entidad = "venta"

class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy("apl:venta_listar")
    entidad = "venta"

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = "Ventas/eliminar.html"
    success_url = reverse_lazy("apl:venta_listar")
    entidad = "venta"

# ===================== Compras Mercancia =====================
class ComprasMercanciaListView(ListView):
    model = ComprasMercancia
    template_name = 'Compras_Mercancia/listar_compras_mercancia.html'
    context_object_name = 'compras'
    entidad = 'comprasmercancia'

class ComprasMercanciaCreateView(CreateView):
    model = ComprasMercancia
    form_class = ComprasMercanciaForm
    template_name = 'Compras_Mercancia/crear.html'
    success_url = reverse_lazy('apl:comprasmercancia_listar')
    entidad = 'comprasmercancia'

class ComprasMercanciaUpdateView(UpdateView):
    model = ComprasMercancia
    form_class = ComprasMercanciaForm
    template_name = 'Compras_Mercancia/crear.html'
    success_url = reverse_lazy('apl:comprasmercancia_listar')
    entidad = 'comprasmercancia'

class ComprasMercanciaDeleteView(DeleteView):
    model = ComprasMercancia
    template_name = 'Compras_Mercancia/eliminar.html'
    success_url = reverse_lazy('apl:comprasmercancia_listar')
    entidad = 'comprasmercancia'

# ===================== Garantias =====================

class GarantiasListView(ListView):
    model = Garantias
    template_name = "Garantias/listar_garantias.html"
    context_object_name = "garantias"
    entidad = "garantias"

class GarantiasCreateView(CreateView):
    model = Garantias
    form_class = GarantiasForm
    template_name = "Garantias/crear.html"
    success_url = reverse_lazy("apl:garantias_listar")
    entidad = "garantias"

class GarantiasUpdateView(UpdateView):
    model = Garantias
    form_class = GarantiasForm
    template_name = "Garantias/crear.html"
    success_url = reverse_lazy("apl:garantias_listar")
    entidad = "garantias"

class GarantiasDeleteView(DeleteView):
    model = Garantias
    template_name = "Garantias/eliminar.html"
    success_url = reverse_lazy("apl:garantias_listar")
    entidad = "garantias"