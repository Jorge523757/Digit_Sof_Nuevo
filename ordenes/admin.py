"""
DIGT SOFT - Admin del Módulo de Órdenes de Servicio
"""

from django.contrib import admin
from .models import OrdenServicio, SeguimientoOrden


class SeguimientoOrdenInline(admin.TabularInline):
    """Inline para seguimientos de orden"""
    model = SeguimientoOrden
    extra = 1
    fields = ('descripcion', 'estado_anterior', 'estado_nuevo')


@admin.register(OrdenServicio)
class OrdenServicioAdmin(admin.ModelAdmin):
    """Admin para Órdenes de Servicio"""
    list_display = ('numero_orden', 'cliente', 'tipo_equipo', 'marca', 'modelo', 'estado', 'prioridad', 'fecha_ingreso')
    list_filter = ('estado', 'prioridad', 'tipo_equipo', 'fecha_ingreso')
    search_fields = ('numero_orden', 'cliente__nombres', 'cliente__apellidos', 'marca', 'modelo', 'serie')
    readonly_fields = ('fecha_ingreso', 'fecha_actualizacion')
    inlines = [SeguimientoOrdenInline]

    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_orden', 'fecha_ingreso', 'fecha_compromiso', 'cliente', 'tecnico_asignado')
        }),
        ('Información del Equipo', {
            'fields': ('tipo_equipo', 'marca', 'modelo', 'serie', 'accesorios', 'estado_fisico')
        }),
        ('Diagnóstico y Solución', {
            'fields': ('falla_reportada', 'diagnostico', 'solucion')
        }),
        ('Estado y Prioridad', {
            'fields': ('estado', 'prioridad')
        }),
        ('Costos', {
            'fields': ('costo_mano_obra', 'costo_repuestos')
        }),
        ('Información Adicional', {
            'fields': ('observaciones', 'fecha_actualizacion', 'fecha_entrega')
        }),
    )


@admin.register(SeguimientoOrden)
class SeguimientoOrdenAdmin(admin.ModelAdmin):
    """Admin para Seguimientos de Orden"""
    list_display = ('orden', 'fecha', 'estado_anterior', 'estado_nuevo')
    list_filter = ('fecha', 'estado_nuevo')
    search_fields = ('orden__numero_orden', 'descripcion')
    readonly_fields = ('fecha',)

