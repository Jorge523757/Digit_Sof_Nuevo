"""
DIGT SOFT - Admin del Módulo de Ventas
"""

from django.contrib import admin
from .models import Venta, DetalleVenta


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    fields = ['producto', 'cantidad', 'precio_unitario', 'descuento_item', 'con_garantia']


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['numero_venta', 'cliente', 'fecha_venta', 'total', 'estado', 'pagado']
    list_filter = ['estado', 'canal_venta', 'pagado', 'fecha_venta']
    search_fields = ['numero_venta', 'cliente__nombres', 'cliente__apellidos']
    ordering = ['-fecha_venta']
    inlines = [DetalleVentaInline]
    list_per_page = 25

    readonly_fields = ['numero_venta', 'fecha_venta', 'fecha_actualizacion', 'subtotal', 'total']

    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_venta', 'cliente', 'canal_venta', 'vendedor')
        }),
        ('Estado y Pago', {
            'fields': ('estado', 'metodo_pago', 'pagado', 'fecha_pago')
        }),
        ('Montos', {
            'fields': ('subtotal', 'descuento', 'impuestos', 'total')
        }),
        ('Entrega', {
            'fields': ('requiere_entrega', 'direccion_entrega', 'entregado', 'fecha_entrega'),
            'classes': ('collapse',)
        }),
        ('Información Adicional', {
            'fields': ('observaciones', 'notas_internas', 'fecha_venta', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    list_filter = ['con_garantia']
    search_fields = ['venta__numero_venta', 'producto__nombre_producto']
