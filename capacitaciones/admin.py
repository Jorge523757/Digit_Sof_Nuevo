"""
DIGT SOFT - Admin del Módulo de Capacitaciones
"""

from django.contrib import admin
from .models import Capacitacion, ParticipanteCapacitacion


@admin.register(Capacitacion)
class CapacitacionAdmin(admin.ModelAdmin):
    list_display = ['codigo_capacitacion', 'nombre', 'tipo', 'instructor', 'fecha_inicio', 'estado', 'cupo_maximo']
    list_filter = ['tipo', 'estado', 'modalidad', 'fecha_inicio']
    search_fields = ['codigo_capacitacion', 'nombre', 'instructor']
    ordering = ['-fecha_inicio']
    list_per_page = 25


@admin.register(ParticipanteCapacitacion)
class ParticipanteCapacitacionAdmin(admin.ModelAdmin):
    list_display = ['capacitacion', 'tecnico', 'fecha_inscripcion', 'asistio', 'aprobado', 'calificacion']
    list_filter = ['asistio', 'aprobado']
    search_fields = ['capacitacion__nombre', 'tecnico__nombres']
