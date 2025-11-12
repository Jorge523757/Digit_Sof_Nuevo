from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
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

            context.update({
                'total_clientes': Cliente.objects.count(),
                'total_productos': Producto.objects.count(),
                'total_ventas': Venta.objects.count(),
                'ordenes_pendientes': OrdenServicio.objects.filter(estado='PENDIENTE').count(),
                'productos_bajo_stock': Producto.objects.filter(
                    stock_actual__lte=5,
                    activo=True
                ).count(),
            })
        except:
            context.update({
                'total_clientes': 0,
                'total_productos': 0,
                'total_ventas': 0,
                'ordenes_pendientes': 0,
                'productos_bajo_stock': 0,
            })
    else:
        # Si es cliente, mostrar información limitada
        context.update({
            'mensaje_bienvenida': f'¡Bienvenido, {request.user.first_name or request.user.username}!',
            'tipo_usuario': 'Cliente',
        })

    return render(request, 'dashboard/dashboard.html', context)
