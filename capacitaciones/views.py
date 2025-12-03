"""DIGT SOFT - Vistas Capacitaciones"""
from django.shortcuts import render, get_object_or_404
from .models import Capacitacion

def capacitaciones_lista(request):
    capacitaciones = Capacitacion.objects.all()
    return render(request, 'capacitaciones/lista.html', {'capacitaciones': capacitaciones})

def capacitacion_detalle(request, pk):
    capacitacion = get_object_or_404(Capacitacion, pk=pk)
    return render(request, 'capacitaciones/detalle.html', {'capacitacion': capacitacion})

