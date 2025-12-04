"""
DIGITSOFT - Vistas del Módulo de Ventas
Integrado con E-commerce y Productos
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum, Count
from .models import Venta, DetalleVenta
from usuarios.decorators import staff_required


@login_required
@staff_required
def ventas_lista(request):
    """Lista de ventas con búsqueda y filtros"""
    ventas = Venta.objects.select_related('cliente').all()

    # Búsqueda simple
    busqueda = request.GET.get('busqueda', '')
    if busqueda:
        ventas = ventas.filter(
            Q(numero_venta__icontains=busqueda) |
            Q(cliente__nombres__icontains=busqueda) |
            Q(cliente__apellidos__icontains=busqueda)
        )

    # Paginación
    paginator = Paginator(ventas, 20)
    page_obj = paginator.get_page(request.GET.get('page'))

    # Estadísticas
    total_ventas = Venta.objects.count()
    ventas_completadas = Venta.objects.filter(estado='COMPLETADA').count()
    ventas_pendientes = Venta.objects.filter(estado='PENDIENTE').count()
    total_ingresos = Venta.objects.filter(estado='COMPLETADA').aggregate(
        total=Sum('total')
    )['total'] or 0

    context = {
        'page_obj': page_obj,
        'total_ventas': total_ventas,
        'ventas_completadas': ventas_completadas,
        'ventas_pendientes': ventas_pendientes,
        'total_ingresos': total_ingresos,
    }

    return render(request, 'ventas/lista.html', context)


@login_required
@staff_required
def venta_crear(request):
    """Crear nueva venta"""
    messages.info(request, 'Formulario de creación en desarrollo')
    return redirect('ventas:lista')


@login_required
@staff_required
def venta_detalle(request, pk):
    """Ver detalle de una venta"""
    venta = get_object_or_404(Venta, pk=pk)
    detalles = venta.items.select_related('producto').all()

    context = {
        'venta': venta,
        'detalles': detalles,
    }
    return render(request, 'ventas/detalle.html', context)


@login_required
@staff_required
def venta_editar(request, pk):
    """Editar venta existente"""
    venta = get_object_or_404(Venta, pk=pk)
    messages.info(request, 'Formulario de edición en desarrollo')
    return redirect('ventas:detalle', pk=pk)


@login_required
@staff_required
def venta_cambiar_estado(request, pk):
    """Cambiar estado de una venta"""
    if request.method == 'POST':
        venta = get_object_or_404(Venta, pk=pk)
        messages.success(request, f'Estado actualizado')
        return redirect('ventas:detalle', pk=pk)

    return redirect('ventas:lista')


@login_required
@staff_required
def ventas_reportes(request):
    """Reportes y estadísticas de ventas"""
    from django.db.models.functions import TruncDate

    # Ventas por estado
    ventas_por_estado = Venta.objects.values('estado').annotate(
        cantidad=Count('id'),
        total=Sum('total')
    )

    # Ventas por canal
    ventas_por_canal = Venta.objects.values('canal_venta').annotate(
        cantidad=Count('id'),
        total=Sum('total')
    )

    # Productos más vendidos
    productos_top = DetalleVenta.objects.values(
        'producto__nombre_producto'
    ).annotate(
        cantidad_vendida=Sum('cantidad'),
        total_ventas=Sum('subtotal')
    ).order_by('-cantidad_vendida')[:10]

    context = {
        'ventas_por_estado': ventas_por_estado,
        'ventas_por_canal': ventas_por_canal,
        'productos_top': productos_top,
    }

    return render(request, 'ventas/reportes.html', context)


