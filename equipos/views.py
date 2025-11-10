"""
DIGT SOFT - Vistas del Módulo de Equipos
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Equipo
from clientes.models import Cliente


@login_required
def equipos_lista(request):
    """Lista de equipos con búsqueda y filtros"""
    equipos = Equipo.objects.select_related('cliente').all()

    # Búsqueda
    query = request.GET.get('q', '').strip()
    if query:
        equipos = equipos.filter(
            Q(numero_serie__icontains=query) |
            Q(marca__icontains=query) |
            Q(modelo__icontains=query) |
            Q(cliente__nombres__icontains=query) |
            Q(cliente__apellidos__icontains=query)
        )

    # Filtro por tipo
    tipo = request.GET.get('tipo', '')
    if tipo:
        equipos = equipos.filter(tipo_equipo=tipo)

    # Filtro por estado
    estado = request.GET.get('estado', '')
    if estado:
        equipos = equipos.filter(estado=estado)

    context = {
        'equipos': equipos,
        'query': query,
        'tipo': tipo,
        'estado': estado,
    }
    return render(request, 'equipos/lista.html', context)


@login_required
def equipo_detalle(request, pk):
    """Detalle de un equipo"""
    equipo = get_object_or_404(Equipo, pk=pk)

    context = {
        'equipo': equipo,
    }
    return render(request, 'equipos/detalle.html', context)


@login_required
def equipo_crear(request):
    """Crear nuevo equipo"""
    if request.method == 'POST':
        # Aquí iría la lógica para crear el equipo
        messages.success(request, '✅ Equipo registrado exitosamente.')
        return redirect('equipos:lista')

    clientes = Cliente.objects.filter(activo=True)

    context = {
        'clientes': clientes,
    }
    return render(request, 'equipos/form.html', context)

