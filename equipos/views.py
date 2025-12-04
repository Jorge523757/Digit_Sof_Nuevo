"""DIGIT SOFT - Vistas Equipos"""
from django.shortcuts import render, get_object_or_404
from .models import Equipo

def equipos_lista(request):
    equipos = Equipo.objects.filter(activo=True)
    return render(request, 'equipos/lista.html', {'equipos': equipos})

def equipo_detalle(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, 'equipos/detalle.html', {'equipo': equipo})

