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


# REPORTES PDF Y EXCEL
# ==============================================

@login_required
@staff_required
def venta_reporte_pdf(request):
    """Generar reporte de ventas en PDF"""
    from utils.reportes import generar_pdf
    from datetime import datetime

    # Obtener filtros
    query = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '')

    # Filtrar datos
    ventas = Venta.objects.all().select_related('cliente')

    if query:
        ventas = ventas.filter(
            Q(numero_venta__icontains=query) |
            Q(cliente__nombres__icontains=query) |
            Q(cliente__apellidos__icontains=query)
        )

    if estado:
        ventas = ventas.filter(estado=estado)

    ventas = ventas.order_by('-fecha_venta')

    context = {
        'ventas': ventas,
        'fecha': datetime.now(),
        'usuario': request.user,
        'total_ventas': ventas.count(),
        'total_ingresos': ventas.aggregate(Sum('total'))['total__sum'] or 0,
    }

    filename = f'reporte_ventas_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    return generar_pdf('reportes/ventas_pdf.html', context, filename)


@login_required
@staff_required
def venta_reporte_excel(request):
    """Generar reporte de ventas en Excel"""
    from utils.reportes import generar_excel_avanzado
    from datetime import datetime

    # Obtener filtros
    query = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '')

    # Filtrar datos
    ventas_query = Venta.objects.all().select_related('cliente')

    if query:
        ventas_query = ventas_query.filter(
            Q(numero_venta__icontains=query) |
            Q(cliente__nombres__icontains=query) |
            Q(cliente__apellidos__icontains=query)
        )

    if estado:
        ventas_query = ventas_query.filter(estado=estado)

    ventas_query = ventas_query.order_by('-fecha_venta')

    # Preparar datos para Excel
    datos = []
    for venta in ventas_query:
        datos.append({
            'numero_venta': venta.numero_venta,
            'cliente': str(venta.cliente) if venta.cliente else 'Sin cliente',
            'fecha_venta': venta.fecha_venta,
            'subtotal': float(venta.subtotal),
            'impuestos': float(venta.impuestos),
            'total': float(venta.total),
            'estado': venta.get_estado_display(),
            'metodo_pago': venta.get_metodo_pago_display(),
        })

    # Definir columnas
    columnas = [
        ('numero_venta', 'Número Venta', 'texto'),
        ('cliente', 'Cliente', 'texto'),
        ('fecha_venta', 'Fecha', 'fecha'),
        ('subtotal', 'Subtotal', 'moneda'),
        ('impuestos', 'Impuestos', 'moneda'),
        ('total', 'Total', 'moneda'),
        ('estado', 'Estado', 'texto'),
        ('metodo_pago', 'Método Pago', 'texto'),
    ]

    titulo = 'Reporte de Ventas'
    filename = f'reporte_ventas_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'

    # Columnas con totales
    totales = ['subtotal', 'impuestos', 'total']

    return generar_excel_avanzado(datos, columnas, titulo, filename, totales=totales)
