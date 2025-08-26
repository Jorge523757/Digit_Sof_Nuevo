from django import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from administrador.forms import *
from administrador.models import *


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