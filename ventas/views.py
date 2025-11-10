"""
DIGT SOFT - Vistas del Módulo de Ventas
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Venta, ItemVenta
from clientes.models import Cliente
from productos.models import Producto


@login_required
def ventas_lista(request):
    """Lista de ventas con búsqueda y filtros"""
    ventas = Venta.objects.select_related('cliente').all()
    
    # Búsqueda
    query = request.GET.get('q', '').strip()
    if query:
        ventas = ventas.filter(
            Q(numero_venta__icontains=query) |
            Q(cliente__nombres__icontains=query) |
            Q(cliente__apellidos__icontains=query)
        )
    
    # Filtro por estado
    estado = request.GET.get('estado', '')
    if estado:
        ventas = ventas.filter(estado=estado)
    
    context = {
        'ventas': ventas,
        'query': query,
        'estado': estado,
    }
    return render(request, 'ventas/lista.html', context)


@login_required
def venta_detalle(request, pk):
    """Detalle de una venta"""
    venta = get_object_or_404(Venta, pk=pk)
    items = venta.items.select_related('producto').all()
    
    context = {
        'venta': venta,
        'items': items,
    }
    return render(request, 'ventas/detalle.html', context)


@login_required
def venta_crear(request):
    """Crear nueva venta"""
    if request.method == 'POST':
        # Aquí iría la lógica para crear la venta
        messages.success(request, '✅ Venta creada exitosamente.')
        return redirect('ventas:lista')
    
    clientes = Cliente.objects.filter(activo=True)
    productos = Producto.objects.filter(activo=True)
    
    context = {
        'clientes': clientes,
        'productos': productos,
    }
    return render(request, 'ventas/form.html', context)

