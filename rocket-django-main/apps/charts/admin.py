"""
DIGT SOFT - Admin del Módulo de Equipos
"""

from django.contrib import admin
from .models import Equipo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    """Admin para Equipos"""
    list_display = ('tipo_equipo', 'marca', 'modelo', 'numero_serie', 'cliente', 'estado', 'fecha_registro')
    list_filter = ('tipo_equipo', 'estado', 'fecha_registro', 'marca')
    search_fields = ('numero_serie', 'marca', 'modelo', 'cliente__nombres', 'cliente__apellidos')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')

    fieldsets = (
        ('Información del Equipo', {
            'fields': ('tipo_equipo', 'marca', 'modelo', 'numero_serie')
        }),
        ('Especificaciones Técnicas', {
            'fields': ('procesador', 'memoria_ram', 'almacenamiento', 'sistema_operativo')
        }),
        ('Información de Propietario', {
            'fields': ('cliente',)
        }),
        ('Información de Compra', {
            'fields': ('fecha_compra', 'factura_compra')
        }),
        ('Estado y Observaciones', {
            'fields': ('estado', 'observaciones', 'fecha_registro', 'fecha_actualizacion')
        }),
    )

