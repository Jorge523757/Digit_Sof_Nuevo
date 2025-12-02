from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import datetime, timedelta

@login_required
def dashboard_view(request):
    """Vista principal del dashboard con estadísticas"""

    # Verificar si es staff o cliente
    es_staff = request.user.is_staff or request.user.is_superuser

    context = {
        'usuario': request.user,
        'es_staff': es_staff,
        'es_cliente': not es_staff,
    }

    # Si es staff/admin, mostrar estadísticas completas
    if es_staff:
        try:
            from clientes.models import Cliente
            from productos.models import Producto
            from ventas.models import Venta
            from ordenes.models import OrdenServicio
            from facturacion.models import Factura
            from decimal import Decimal

            # Estadísticas básicas
            total_clientes = Cliente.objects.count()
            ordenes_pendientes = OrdenServicio.objects.filter(estado='PENDIENTE').count()

            # Órdenes de hoy
            hoy = datetime.now().date()
            ordenes_hoy = OrdenServicio.objects.filter(
                fecha_creacion__date=hoy
            ).count()

            # Ingresos del mes
            inicio_mes = datetime.now().replace(day=1)
            ingresos_mes = Venta.objects.filter(
                fecha__gte=inicio_mes
            ).aggregate(total=Sum('total'))['total'] or Decimal('0')

            # Última venta
            ultima_venta = Venta.objects.order_by('-fecha').first()
            ultima_venta_numero = getattr(ultima_venta, 'numero', 'VEN-001') if ultima_venta else "VEN-001"
            ultima_venta_total = getattr(ultima_venta, 'total', Decimal('0')) if ultima_venta else Decimal('0')

            # Última factura
            ultima_factura = Factura.objects.order_by('-fecha_emision').first()
            ultima_factura_numero = getattr(ultima_factura, 'numero', 'FAC-001') if ultima_factura else "FAC-001"

            # Productos actualizados (últimas 24 horas)
            hace_24h = datetime.now() - timedelta(hours=24)
            productos_actualizados = Producto.objects.filter(
                fecha_modificacion__gte=hace_24h
            ).count() if hasattr(Producto, 'fecha_modificacion') else 5

            context.update({
                'total_clientes': total_clientes,
                'ordenes_pendientes': ordenes_pendientes,
                'ordenes_hoy': ordenes_hoy,
                'ingresos_mes': ingresos_mes,
                'ultima_venta_numero': ultima_venta_numero,
                'ultima_venta_total': ultima_venta_total,
                'ultima_factura_numero': ultima_factura_numero,
                'productos_actualizados': productos_actualizados,
            })
        except Exception as e:
            context.update({
                'total_clientes': 0,
                'ordenes_pendientes': 0,
                'ordenes_hoy': 0,
                'ingresos_mes': 0,
                'ultima_venta_numero': 'VEN-001',
                'ultima_venta_total': 0,
                'ultima_factura_numero': 'FAC-001',
                'productos_actualizados': 5,
            })
    else:
        # Si es cliente, mostrar información limitada
        context.update({
            'mensaje_bienvenida': f'¡Bienvenido, {request.user.first_name or request.user.username}!',
            'tipo_usuario': 'Cliente',
        })

    return render(request, 'dashboard/dashboard.html', context)
