"""
DIGT SOFT - Admin del Módulo de Equipos
"""

from django.contrib import admin
from .models import Equipo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['codigo_equipo', 'nombre', 'tipo_equipo', 'marca', 'estado', 'ubicacion', 'activo']
    list_filter = ['tipo_equipo', 'estado', 'activo']
    search_fields = ['codigo_equipo', 'nombre', 'marca', 'modelo']
    ordering = ['codigo_equipo']
    list_per_page = 25
