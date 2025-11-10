"""
DIGT SOFT - Admin del Módulo de Garantías
"""

from django.contrib import admin
from .models import Garantia, SeguimientoGarantia


class SeguimientoGarantiaInline(admin.TabularInline):
    model = SeguimientoGarantia
    extra = 0
    readonly_fields = ('fecha_seguimiento',)
    fields = ('fecha_seguimiento', 'estado_anterior', 'estado_nuevo', 'comentarios', 'usuario')


@admin.register(Garantia)
class GarantiaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombre_producto', 'nombre_comprador', 'cedula',
        'fecha_compra', 'fecha_vencimiento', 'estado', 'fecha_registro'
    )
    list_filter = ('estado', 'fecha_compra', 'fecha_vencimiento')
    search_fields = (
        'nombre_comprador', 'cedula', 'nombre_producto',
        'numero_serie', 'factura_compra'
    )
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')
    ordering = ('-fecha_registro',)
    inlines = [SeguimientoGarantiaInline]

    fieldsets = (
        ('Información del Comprador', {
            'fields': ('nombre_comprador', 'cedula', 'telefono', 'correo_electronico', 'cliente')
        }),
        ('Información del Producto', {
            'fields': ('producto', 'nombre_producto', 'numero_serie', 'modelo')
        }),
        ('Información de Compra', {
            'fields': ('fecha_compra', 'factura_compra', 'lugar_compra')
        }),
        ('Detalles de la Garantía', {
            'fields': ('fecha_inicio', 'fecha_vencimiento', 'meses_garantia', 'estado')
        }),
        ('Reclamación', {
            'fields': ('motivo_reclamacion', 'descripcion_problema'),
            'classes': ('collapse',)
        }),
        ('Resolución', {
            'fields': ('solucion', 'fecha_resolucion', 'observaciones'),
            'classes': ('collapse',)
        }),
        ('Auditoría', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('producto', 'cliente')


@admin.register(SeguimientoGarantia)
class SeguimientoGarantiaAdmin(admin.ModelAdmin):
    list_display = (
        'garantia', 'fecha_seguimiento', 'estado_anterior',
        'estado_nuevo', 'usuario'
    )
    list_filter = ('estado_nuevo', 'fecha_seguimiento')
    search_fields = ('garantia__nombre_producto', 'comentarios')
    readonly_fields = ('fecha_seguimiento',)
    ordering = ('-fecha_seguimiento',)

