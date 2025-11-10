"""
DIGT SOFT - Admin del Módulo de Compras
"""

from django.contrib import admin
from .models import Compra, ItemCompra


class ItemCompraInline(admin.TabularInline):
    """Inline para items de compra"""
    model = ItemCompra
    extra = 1
    fields = ('producto', 'cantidad', 'precio_unitario', 'subtotal')
    readonly_fields = ('subtotal',)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    """Admin para Compras"""
    list_display = ('numero_compra', 'proveedor', 'fecha_compra', 'total', 'estado', 'metodo_pago')
    list_filter = ('estado', 'metodo_pago', 'fecha_compra')
    search_fields = ('numero_compra', 'proveedor__razon_social', 'factura_proveedor')
    readonly_fields = ('fecha_compra', 'fecha_actualizacion')
    inlines = [ItemCompraInline]

    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_compra', 'fecha_compra', 'proveedor', 'estado', 'factura_proveedor')
        }),
        ('Detalles Financieros', {
            'fields': ('subtotal', 'impuesto', 'descuento', 'total', 'metodo_pago')
        }),
        ('Información Adicional', {
            'fields': ('fecha_recepcion', 'observaciones', 'fecha_actualizacion')
        }),
    )


@admin.register(ItemCompra)
class ItemCompraAdmin(admin.ModelAdmin):
    """Admin para Items de Compra"""
    list_display = ('compra', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    list_filter = ('compra__fecha_compra',)
    search_fields = ('compra__numero_compra', 'producto__nombre_producto')

