"""
DIGT SOFT - Vistas del Módulo de Capacitaciones
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def capacitaciones_lista(request):
    """Lista de capacitaciones"""
    context = {
        'capacitaciones': [],
    }
    return render(request, 'capacitaciones/lista.html', context)


@login_required
def capacitacion_detalle(request, pk):
    """Detalle de una capacitación"""
    context = {}
    return render(request, 'capacitaciones/detalle.html', context)


@login_required
def capacitacion_crear(request):
    """Crear nueva capacitación"""
    if request.method == 'POST':
        messages.success(request, '✅ Capacitación creada exitosamente.')
        return redirect('capacitaciones:lista')

    context = {}
    return render(request, 'capacitaciones/form.html', context)


@login_required
def capacitacion_editar(request, pk):
    """Editar capacitación"""
    if request.method == 'POST':
        messages.success(request, '✅ Capacitación actualizada exitosamente.')
        return redirect('capacitaciones:detalle', pk=pk)

    context = {}
    return render(request, 'capacitaciones/form.html', context)


@login_required
def capacitacion_eliminar(request, pk):
    """Eliminar capacitación"""
    if request.method == 'POST':
        messages.success(request, '🗑️ Capacitación eliminada correctamente.')
        return redirect('capacitaciones:lista')

    context = {}
    return render(request, 'capacitaciones/eliminar.html', context)
