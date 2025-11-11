"""
DIGT SOFT - Admin del Módulo de Compras
"""

from django.contrib import admin
from .models import Compra, DetalleCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['numero_compra', 'proveedor', 'fecha_compra', 'total', 'estado', 'pagado']
    list_filter = ['estado', 'pagado', 'fecha_compra']
    search_fields = ['numero_compra', 'proveedor__nombre_empresa']
    ordering = ['-fecha_compra']
    list_per_page = 25


@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ['compra', 'producto', 'cantidad', 'precio_unitario', 'subtotal', 'recibido']
    list_filter = ['recibido']
    search_fields = ['compra__numero_compra', 'producto__nombre_producto']
