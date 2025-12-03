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

