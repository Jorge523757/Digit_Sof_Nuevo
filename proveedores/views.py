"""
DIGT SOFT - Vistas del Módulo de Proveedores
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Proveedor


@login_required
def proveedores_lista(request):
    """Lista de proveedores con búsqueda y filtros"""
    proveedores = Proveedor.objects.all()

    # Búsqueda
    query = request.GET.get('q', '').strip()
    if query:
        proveedores = proveedores.filter(
            Q(razon_social__icontains=query) |
            Q(nombre_comercial__icontains=query) |
            Q(numero_documento__icontains=query) |
            Q(correo__icontains=query)
        )

    # Filtro por estado
    estado = request.GET.get('estado', '')
    if estado == 'activo':
        proveedores = proveedores.filter(activo=True)
    elif estado == 'inactivo':
        proveedores = proveedores.filter(activo=False)

    context = {
        'proveedores': proveedores,
        'query': query,
        'estado': estado,
    }
    return render(request, 'proveedores/lista.html', context)


@login_required
def proveedor_detalle(request, pk):
    """Detalle de un proveedor"""
    proveedor = get_object_or_404(Proveedor, pk=pk)
    compras = proveedor.compras.all()[:10]

    context = {
        'proveedor': proveedor,
        'compras': compras,
    }
    return render(request, 'proveedores/detalle.html', context)


@login_required
def proveedor_crear(request):
    """Crear nuevo proveedor"""
    if request.method == 'POST':
        # Aquí iría la lógica para crear el proveedor
        messages.success(request, '✅ Proveedor creado exitosamente.')
        return redirect('proveedores:lista')

    return render(request, 'proveedores/form.html', {})


@login_required
def proveedor_editar(request, pk):
    """Editar proveedor"""
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == 'POST':
        # Aquí iría la lógica para editar el proveedor
        messages.success(request, '✅ Proveedor actualizado exitosamente.')
        return redirect('proveedores:detalle', pk=pk)

    context = {
        'proveedor': proveedor,
    }
    return render(request, 'proveedores/form.html', context)


@login_required
def proveedor_eliminar(request, pk):
    """Eliminar proveedor"""
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == 'POST':
        nombre = proveedor.razon_social
        proveedor.delete()
        messages.success(request, f'🗑️ Proveedor "{nombre}" eliminado correctamente.')
        return redirect('proveedores:lista')

    context = {
        'proveedor': proveedor,
    }
    return render(request, 'proveedores/eliminar.html', context)


