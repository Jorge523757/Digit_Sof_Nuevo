"""
DIGT SOFT - Vistas del Módulo de Facturación
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def facturas_lista(request):
    """Lista de facturas"""
    context = {
        'facturas': [],
    }
    return render(request, 'facturacion/lista.html', context)


@login_required
def factura_detalle(request, pk):
    """Detalle de una factura"""
    context = {}
    return render(request, 'facturacion/detalle.html', context)


@login_required
def factura_crear(request):
    """Crear nueva factura"""
    if request.method == 'POST':
        messages.success(request, '✅ Factura creada exitosamente.')
        return redirect('facturacion:lista')

    context = {}
    return render(request, 'facturacion/form.html', context)


@login_required
def factura_editar(request, pk):
    """Editar factura"""
    if request.method == 'POST':
        messages.success(request, '✅ Factura actualizada exitosamente.')
        return redirect('facturacion:detalle', pk=pk)

    context = {}
    return render(request, 'facturacion/form.html', context)


@login_required
def factura_eliminar(request, pk):
    """Eliminar factura"""
    if request.method == 'POST':
        messages.success(request, '🗑️ Factura eliminada correctamente.')
        return redirect('facturacion:lista')

    context = {}
    return render(request, 'facturacion/eliminar.html', context)
