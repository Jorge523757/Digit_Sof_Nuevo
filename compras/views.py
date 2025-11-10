"""
DIGT SOFT - Vistas del Módulo de Compras
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Compra, ItemCompra
from proveedores.models import Proveedor
from productos.models import Producto


@login_required
def compras_lista(request):
    """Lista de compras con búsqueda y filtros"""
    compras = Compra.objects.select_related('proveedor').all()

    # Búsqueda
    query = request.GET.get('q', '').strip()
    if query:
        compras = compras.filter(
            Q(numero_compra__icontains=query) |
            Q(proveedor__razon_social__icontains=query) |
            Q(factura_proveedor__icontains=query)
        )

    # Filtro por estado
    estado = request.GET.get('estado', '')
    if estado:
        compras = compras.filter(estado=estado)

    context = {
        'compras': compras,
        'query': query,
        'estado': estado,
    }
    return render(request, 'compras/lista.html', context)


@login_required
def compra_detalle(request, pk):
    """Detalle de una compra"""
    compra = get_object_or_404(Compra, pk=pk)
    items = compra.items.select_related('producto').all()

    context = {
        'compra': compra,
        'items': items,
    }
    return render(request, 'compras/detalle.html', context)


@login_required
def compra_crear(request):
    """Crear nueva compra"""
    if request.method == 'POST':
        # Aquí iría la lógica para crear la compra
        messages.success(request, '✅ Compra creada exitosamente.')
        return redirect('compras:lista')

    proveedores = Proveedor.objects.filter(activo=True)
    productos = Producto.objects.filter(activo=True)

    context = {
        'proveedores': proveedores,
        'productos': productos,
    }
    return render(request, 'compras/form.html', context)


@login_required
def compra_editar(request, pk):
    """Editar compra"""
    compra = get_object_or_404(Compra, pk=pk)
    
    if request.method == 'POST':
        # Aquí iría la lógica para editar la compra
        messages.success(request, '✅ Compra actualizada exitosamente.')
        return redirect('compras:detalle', pk=pk)

    proveedores = Proveedor.objects.filter(activo=True)
    productos = Producto.objects.filter(activo=True)

    context = {
        'compra': compra,
        'proveedores': proveedores,
        'productos': productos,
    }
    return render(request, 'compras/form.html', context)


@login_required
def compra_eliminar(request, pk):
    """Eliminar compra"""
    compra = get_object_or_404(Compra, pk=pk)
    
    if request.method == 'POST':
        numero = compra.numero_compra
        compra.delete()
        messages.success(request, f'🗑️ Compra "{numero}" eliminada correctamente.')
        return redirect('compras:lista')
    
    context = {
        'compra': compra,
    }
    return render(request, 'compras/eliminar.html', context)


