"""
DIGT SOFT - Admin del Módulo de Órdenes de Servicio
"""

from django.contrib import admin
from .models import OrdenServicio, RepuestoOrden, SeguimientoOrden


class RepuestoOrdenInline(admin.TabularInline):
    model = RepuestoOrden
    extra = 1


class SeguimientoOrdenInline(admin.TabularInline):
    model = SeguimientoOrden
    extra = 0
    readonly_fields = ['estado_anterior', 'estado_nuevo', 'descripcion', 'usuario', 'fecha']


@admin.register(OrdenServicio)
class OrdenServicioAdmin(admin.ModelAdmin):
    list_display = ['numero_orden', 'cliente', 'tipo_equipo', 'marca', 'estado', 'prioridad', 'tecnico_asignado', 'fecha_recepcion']
    list_filter = ['estado', 'prioridad', 'tecnico_asignado', 'fecha_recepcion']
    search_fields = ['numero_orden', 'cliente__nombres', 'cliente__apellidos', 'marca', 'modelo']
    ordering = ['-fecha_recepcion']
    inlines = [RepuestoOrdenInline, SeguimientoOrdenInline]
    list_per_page = 25
    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_orden', 'cliente', 'tecnico_asignado')
        }),
        ('Detalles del Equipo', {
            'fields': ('tipo_equipo', 'marca', 'modelo', 'serie', 'estado_fisico', 'accesorios_incluidos')
        }),
        ('Problema y Solución', {
            'fields': ('falla_reportada', 'diagnostico', 'solucion_aplicada')
        }),
        ('Estado y Prioridad', {
            'fields': ('estado', 'prioridad')
        }),
        ('Costos', {
            'fields': ('costo_diagnostico', 'costo_mano_obra', 'costo_repuestos', 'costo_total', 'pagado')
        }),
        ('Fechas', {
            'fields': ('fecha_recepcion', 'fecha_compromiso', 'fecha_entrega', 'fecha_pago')
        }),
        ('Garantía', {
            'fields': ('tiene_garantia', 'dias_garantia')
        }),
        ('Notas', {
            'fields': ('observaciones', 'notas_internas')
        }),
    )
    readonly_fields = ['numero_orden', 'fecha_recepcion', 'costo_total']


@admin.register(RepuestoOrden)
class RepuestoOrdenAdmin(admin.ModelAdmin):
    list_display = ['orden', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    search_fields = ['orden__numero_orden', 'producto__nombre_producto']


@admin.register(SeguimientoOrden)
class SeguimientoOrdenAdmin(admin.ModelAdmin):
    list_display = ['orden', 'estado_anterior', 'estado_nuevo', 'usuario', 'fecha']
    list_filter = ['fecha']
    search_fields = ['orden__numero_orden', 'descripcion']
    readonly_fields = ['fecha']
