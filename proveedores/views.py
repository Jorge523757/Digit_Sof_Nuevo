"""
DIGT SOFT - Vistas del Módulo de Proveedores
CRUD Completo con Tablas Modernas
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from .models import Proveedor
from .forms import ProveedorForm, BuscarProveedorForm


def proveedores_lista(request):
    """Lista de proveedores con búsqueda y filtros"""
    form = BuscarProveedorForm(request.GET or None)
    proveedores = Proveedor.objects.all()

    # Aplicar filtros
    if form.is_valid():
        busqueda = form.cleaned_data.get('busqueda')
        calificacion = form.cleaned_data.get('calificacion')
        estado = form.cleaned_data.get('estado')

        if busqueda:
            proveedores = proveedores.filter(
                Q(nombre_empresa__icontains=busqueda) |
                Q(nit__icontains=busqueda) |
                Q(nombre_contacto__icontains=busqueda) |
                Q(email__icontains=busqueda) |
                Q(telefono__icontains=busqueda)
            )

        if calificacion:
            proveedores = proveedores.filter(calificacion=calificacion)

        if estado == 'activo':
            proveedores = proveedores.filter(activo=True)
        elif estado == 'inactivo':
            proveedores = proveedores.filter(activo=False)

    # Paginación
    paginator = Paginator(proveedores, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Estadísticas
    total_proveedores = Proveedor.objects.count()
    proveedores_activos = Proveedor.objects.filter(activo=True).count()
    excelentes = Proveedor.objects.filter(calificacion=5).count()

    context = {
        'page_obj': page_obj,
        'form': form,
        'total_proveedores': total_proveedores,
        'proveedores_activos': proveedores_activos,
        'excelentes': excelentes,
    }

    return render(request, 'proveedores/lista.html', context)


def proveedor_crear(request):
    """Crear nuevo proveedor"""
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save()
            messages.success(request, f'✅ Proveedor "{proveedor.nombre_empresa}" creado exitosamente.')
            return redirect('proveedores:detalle', pk=proveedor.pk)
    else:
        form = ProveedorForm()

    context = {
        'form': form,
        'titulo': 'Registrar Nuevo Proveedor',
        'accion': 'Crear'
    }
    return render(request, 'proveedores/form.html', context)


def proveedor_detalle(request, pk):
    """Ver detalle de un proveedor"""
    proveedor = get_object_or_404(Proveedor, pk=pk)

    context = {
        'proveedor': proveedor,
    }
    return render(request, 'proveedores/detalle.html', context)


def proveedor_editar(request, pk):
    """Editar proveedor existente"""
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            proveedor = form.save()
            messages.success(request, f'✅ Proveedor "{proveedor.nombre_empresa}" actualizado correctamente.')
            return redirect('proveedores:detalle', pk=proveedor.pk)
    else:
        form = ProveedorForm(instance=proveedor)

    context = {
        'form': form,
        'proveedor': proveedor,
        'titulo': 'Editar Proveedor',
        'accion': 'Actualizar'
    }
    return render(request, 'proveedores/form.html', context)


def proveedor_eliminar(request, pk):
    """Eliminar proveedor"""
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == 'POST':
        nombre = proveedor.nombre_empresa
        proveedor.delete()
        messages.success(request, f'✅ Proveedor "{nombre}" eliminado correctamente.')
        return redirect('proveedores:lista')

    context = {
        'proveedor': proveedor,
    }
    return render(request, 'proveedores/eliminar.html', context)


def proveedor_toggle_estado(request, pk):
    """Activar/Desactivar proveedor"""
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, pk=pk)
        proveedor.activo = not proveedor.activo
        proveedor.save()

        estado = 'activado' if proveedor.activo else 'desactivado'
        messages.success(request, f'✅ Proveedor "{proveedor.nombre_empresa}" {estado}.')

        return JsonResponse({
            'success': True,
            'activo': proveedor.activo,
            'mensaje': f'Proveedor {estado} correctamente'
        })

    return JsonResponse({'success': False}, status=400)


# REPORTES PDF Y EXCEL
# ==============================================

from django.contrib.auth.decorators import login_required
from usuarios.decorators import staff_required
from django.db.models import Sum

@login_required
@staff_required
def proveedor_reporte_pdf(request):
    """Generar reporte de proveedores en PDF"""
    from utils.reportes import generar_pdf
    from datetime import datetime

    query = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '')
    calificacion = request.GET.get('calificacion', '')

    datos = Proveedor.objects.all()

    if query:
        datos = datos.filter(
            Q(nombre_empresa__icontains=query) |
            Q(nit__icontains=query) |
            Q(nombre_contacto__icontains=query)
        )

    if estado == 'activo':
        datos = datos.filter(activo=True)
    elif estado == 'inactivo':
        datos = datos.filter(activo=False)

    if calificacion:
        datos = datos.filter(calificacion=calificacion)

    datos = datos.order_by('nombre_empresa')

    context = {
        'datos': datos,
        'fecha': datetime.now(),
        'usuario': request.user,
        'total': datos.count(),
    }

    filename = f'reporte_proveedores_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    return generar_pdf('reportes/proveedores_pdf.html', context, filename)


@login_required
@staff_required
def proveedor_reporte_excel(request):
    """Generar reporte de proveedores en Excel"""
    from utils.reportes import generar_excel_avanzado
    from datetime import datetime

    query = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '')
    calificacion = request.GET.get('calificacion', '')

    datos_query = Proveedor.objects.all()

    if query:
        datos_query = datos_query.filter(
            Q(nombre_empresa__icontains=query) |
            Q(nit__icontains=query) |
            Q(nombre_contacto__icontains=query)
        )

    if estado == 'activo':
        datos_query = datos_query.filter(activo=True)
    elif estado == 'inactivo':
        datos_query = datos_query.filter(activo=False)

    if calificacion:
        datos_query = datos_query.filter(calificacion=calificacion)

    datos_query = datos_query.order_by('nombre_empresa')

    datos = []
    for item in datos_query:
        datos.append({
            'nombre_empresa': item.nombre_empresa,
            'nit': item.nit,
            'nombre_contacto': item.nombre_contacto,
            'telefono': item.telefono,
            'email': item.email,
            'ciudad': item.ciudad or '',
            'calificacion': item.calificacion if hasattr(item, 'calificacion') else 0,
            'activo': 'Sí' if item.activo else 'No',
        })

    columnas = [
        ('nombre_empresa', 'Empresa', 'texto'),
        ('nit', 'NIT', 'texto'),
        ('nombre_contacto', 'Contacto', 'texto'),
        ('telefono', 'Teléfono', 'texto'),
        ('email', 'Email', 'texto'),
        ('ciudad', 'Ciudad', 'texto'),
        ('calificacion', 'Calificación', 'numero'),
        ('activo', 'Activo', 'texto'),
    ]

    titulo = 'Reporte de Proveedores'
    filename = f'reporte_proveedores_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'

    return generar_excel_avanzado(datos, columnas, titulo, filename)
