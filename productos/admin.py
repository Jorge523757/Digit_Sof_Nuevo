"""
DIGT SOFT - Admin del Módulo de Productos
"""

from django.contrib import admin
from .models import Producto, CategoriaProducto, MovimientoInventario, ReaccionProducto


@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo', 'fecha_registro')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_sku', 'nombre_producto', 'categoria', 'marca',
        'precio_venta', 'stock_actual', 'activo', 'fecha_registro'
    )
    list_filter = ('activo', 'categoria', 'marca', 'disponible_web', 'destacado')
    search_fields = ('codigo_sku', 'nombre_producto', 'marca', 'modelo_equipo')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')
    ordering = ('-fecha_registro',)

    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre_producto', 'codigo_sku', 'categoria', 'descripcion')
        }),
        ('Especificaciones Técnicas', {
            'fields': ('modelo_equipo', 'marca', 'procesador', 'memoria_ram', 'memoria_rom', 'especificaciones'),
            'classes': ('collapse',)
        }),
        ('Precios', {
            'fields': ('precio_compra', 'precio_venta', 'precio_mayorista')
        }),
        ('Inventario', {
            'fields': ('stock_actual', 'stock_minimo', 'stock_maximo')
        }),
        ('E-commerce', {
            'fields': ('imagen', 'disponible_web', 'destacado'),
            'classes': ('collapse',)
        }),
        ('Garantía', {
            'fields': ('tiene_garantia', 'meses_garantia')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
        ('Auditoría', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = (
        'producto', 'tipo_movimiento', 'cantidad',
        'stock_anterior', 'stock_nuevo', 'fecha_movimiento'
    )
    list_filter = ('tipo_movimiento', 'fecha_movimiento')
    search_fields = ('producto__nombre_producto', 'motivo')
    readonly_fields = ('fecha_movimiento',)
    ordering = ('-fecha_movimiento',)

    fieldsets = (
        ('Movimiento', {
            'fields': ('producto', 'tipo_movimiento', 'cantidad', 'motivo')
        }),
        ('Stock', {
            'fields': ('stock_anterior', 'stock_nuevo')
        }),
        ('Detalles', {
            'fields': ('observaciones', 'usuario', 'fecha_movimiento')
        }),
    )


@admin.register(ReaccionProducto)
class ReaccionProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo', 'usuario', 'session_id', 'fecha_creacion')
    list_filter = ('tipo', 'fecha_creacion')
    search_fields = ('producto__nombre_producto', 'usuario__username')
    readonly_fields = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)


