"""
DIGT SOFT - Admin del Módulo de Ventas
"""

from django.contrib import admin
from .models import Venta, ItemVenta


class ItemVentaInline(admin.TabularInline):
    """Inline para items de venta"""
    model = ItemVenta
    extra = 1
    fields = ('producto', 'cantidad', 'precio_unitario', 'subtotal')
    readonly_fields = ('subtotal',)


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    """Admin para Ventas"""
    list_display = ('numero_venta', 'cliente', 'fecha_venta', 'total', 'estado', 'metodo_pago')
    list_filter = ('estado', 'metodo_pago', 'fecha_venta')
    search_fields = ('numero_venta', 'cliente__nombres', 'cliente__apellidos', 'cliente__numero_documento')
    readonly_fields = ('fecha_venta', 'fecha_actualizacion')
    inlines = [ItemVentaInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_venta', 'fecha_venta', 'cliente', 'estado')
        }),
        ('Detalles Financieros', {
            'fields': ('subtotal', 'impuesto', 'descuento', 'total', 'metodo_pago')
        }),
        ('Información Adicional', {
            'fields': ('observaciones', 'fecha_actualizacion')
        }),
    )


@admin.register(ItemVenta)
class ItemVentaAdmin(admin.ModelAdmin):
    """Admin para Items de Venta"""
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    list_filter = ('venta__fecha_venta',)
    search_fields = ('venta__numero_venta', 'producto__nombre_producto')

