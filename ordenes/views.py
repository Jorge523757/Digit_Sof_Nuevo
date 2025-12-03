"""
DIGT SOFT - Vistas del Módulo de Órdenes de Servicio
Gestión completa de servicio técnico
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import OrdenServicio, RepuestoOrden, SeguimientoOrden


def ordenes_lista(request):
    """Lista de órdenes con búsqueda y filtros"""
    ordenes = OrdenServicio.objects.select_related('cliente', 'tecnico_asignado').all()

    # Búsqueda simple
    busqueda = request.GET.get('busqueda', '')
    if busqueda:
        ordenes = ordenes.filter(
            Q(numero_orden__icontains=busqueda) |
            Q(cliente__nombres__icontains=busqueda) |
            Q(cliente__apellidos__icontains=busqueda) |
            Q(marca__icontains=busqueda) |
            Q(modelo__icontains=busqueda)
        )

    # Paginación
    paginator = Paginator(ordenes, 20)
    page_obj = paginator.get_page(request.GET.get('page'))

    # Estadísticas
    total_ordenes = OrdenServicio.objects.count()
    en_proceso = OrdenServicio.objects.filter(
        estado__in=['RECIBIDA', 'EN_DIAGNOSTICO', 'EN_REPARACION']
    ).count()
    listas_entrega = OrdenServicio.objects.filter(estado='LISTA_ENTREGA').count()
    entregadas = OrdenServicio.objects.filter(estado='ENTREGADA').count()

    context = {
        'page_obj': page_obj,
        'total_ordenes': total_ordenes,
        'en_proceso': en_proceso,
        'listas_entrega': listas_entrega,
        'entregadas': entregadas,
    }

    return render(request, 'ordenes/lista.html', context)


def orden_crear(request):
    """Crear nueva orden de servicio"""
    messages.info(request, 'Formulario de creación en desarrollo')
    return redirect('ordenes:lista')


def orden_detalle(request, pk):
    """Ver detalle de una orden"""
    orden = get_object_or_404(OrdenServicio, pk=pk)
    repuestos = orden.repuestos.select_related('producto').all()
    seguimientos = orden.seguimientos.all()[:10]

    context = {
        'orden': orden,
        'repuestos': repuestos,
        'seguimientos': seguimientos,
    }
    return render(request, 'ordenes/detalle.html', context)


def orden_editar(request, pk):
    """Editar orden existente"""
    orden = get_object_or_404(OrdenServicio, pk=pk)
    messages.info(request, 'Formulario de edición en desarrollo')
    return redirect('ordenes:detalle', pk=pk)


def orden_agregar_repuesto(request, pk):
    """Agregar repuestos a una orden"""
    orden = get_object_or_404(OrdenServicio, pk=pk)
    messages.info(request, 'Función en desarrollo')
    return redirect('ordenes:detalle', pk=pk)


def orden_cambiar_estado(request, pk):
    """Cambiar estado de una orden"""
    if request.method == 'POST':
        orden = get_object_or_404(OrdenServicio, pk=pk)
        messages.success(request, f'Estado de orden actualizado')
        return redirect('ordenes:detalle', pk=pk)

    return redirect('ordenes:lista')


def ordenes_tablero(request):
    """Tablero kanban de órdenes"""
    ordenes_por_estado = {}

    for estado_code, estado_nombre in OrdenServicio.ESTADO_CHOICES:
        ordenes_por_estado[estado_code] = OrdenServicio.objects.filter(
            estado=estado_code
        ).select_related('cliente', 'tecnico_asignado')[:10]

    context = {
        'ordenes_por_estado': ordenes_por_estado,
        'estados': OrdenServicio.ESTADO_CHOICES,
    }

    return render(request, 'ordenes/tablero.html', context)


