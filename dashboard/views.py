from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from datetime import datetime, timedelta

@login_required
def dashboard_view(request):
    """Vista principal del dashboard con estadísticas"""

    # Aquí puedes agregar estadísticas reales cuando tengas los modelos
    context = {
        'total_clientes': 0,
        'ordenes_pendientes': 0,
        'ordenes_hoy': 0,
        'ingresos_mes': 0,
        'usuario': request.user,
    }

    # Cuando tengas los modelos, descomenta y ajusta:
    # from clientes.models import Cliente
    # from ordenes.models import Orden
    # context['total_clientes'] = Cliente.objects.count()
    # context['ordenes_pendientes'] = Orden.objects.filter(estado='pendiente').count()

    return render(request, 'dashboard/dashboard.html', context)
