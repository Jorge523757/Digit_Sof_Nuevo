"""
DIGT SOFT - Vistas del Módulo de Órdenes de Servicio
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import OrdenServicio, SeguimientoOrden
from clientes.models import Cliente
from tecnicos.models import Tecnico


@login_required
def ordenes_lista(request):
    """Lista de órdenes con búsqueda y filtros"""
    ordenes = OrdenServicio.objects.select_related('cliente', 'tecnico_asignado').all()

    # Búsqueda
    query = request.GET.get('q', '').strip()
    if query:
        ordenes = ordenes.filter(
            Q(numero_orden__icontains=query) |
            Q(cliente__nombres__icontains=query) |
            Q(cliente__apellidos__icontains=query) |
            Q(marca__icontains=query) |
            Q(modelo__icontains=query)
        )

    # Filtro por estado
    estado = request.GET.get('estado', '')
    if estado:
        ordenes = ordenes.filter(estado=estado)

    context = {
        'ordenes': ordenes,
        'query': query,
        'estado': estado,
    }
    return render(request, 'ordenes/lista.html', context)


@login_required
def orden_detalle(request, pk):
    """Detalle de una orden"""
    orden = get_object_or_404(OrdenServicio, pk=pk)
    seguimientos = orden.seguimientos.all()

    context = {
        'orden': orden,
        'seguimientos': seguimientos,
    }
    return render(request, 'ordenes/detalle.html', context)


@login_required
def orden_crear(request):
    """Crear nueva orden"""
    if request.method == 'POST':
        # Aquí iría la lógica para crear la orden
        messages.success(request, '✅ Orden de servicio creada exitosamente.')
        return redirect('ordenes:lista')

    clientes = Cliente.objects.filter(activo=True)
    tecnicos = Tecnico.objects.filter(activo=True)

    context = {
        'clientes': clientes,
        'tecnicos': tecnicos,
    }
    return render(request, 'ordenes/form.html', context)


@login_required
def orden_editar(request, pk):
    """Editar orden"""
    orden = get_object_or_404(OrdenServicio, pk=pk)

    if request.method == 'POST':
        # Aquí iría la lógica para editar la orden
        messages.success(request, '✅ Orden actualizada exitosamente.')
        return redirect('ordenes:detalle', pk=pk)

    clientes = Cliente.objects.filter(activo=True)
    tecnicos = Tecnico.objects.filter(activo=True)

    context = {
        'orden': orden,
        'clientes': clientes,
        'tecnicos': tecnicos,
    }
    return render(request, 'ordenes/form.html', context)


@login_required
def orden_eliminar(request, pk):
    """Eliminar orden"""
    orden = get_object_or_404(OrdenServicio, pk=pk)

    if request.method == 'POST':
        numero = orden.numero_orden
        orden.delete()
        messages.success(request, f'🗑️ Orden "{numero}" eliminada correctamente.')
        return redirect('ordenes:lista')

    context = {
        'orden': orden,
    }
    return render(request, 'ordenes/eliminar.html', context)


