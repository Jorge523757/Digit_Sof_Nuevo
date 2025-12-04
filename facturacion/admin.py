"""
DIGIT SOFT - Admin del Módulo de Facturación
"""

from django.contrib import admin
from .models import Factura


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['numero_factura', 'cliente', 'tipo_factura', 'fecha_emision', 'total', 'estado']
    list_filter = ['estado', 'tipo_factura', 'fecha_emision']
    search_fields = ['numero_factura', 'cliente__nombres', 'cliente__apellidos']
    ordering = ['-fecha_emision']
    list_per_page = 25

    readonly_fields = ['numero_factura', 'fecha_emision']

    fieldsets = (
        ('Información Básica', {
            'fields': ('numero_factura', 'cliente', 'venta', 'tipo_factura')
        }),
        ('Estado y Fechas', {
            'fields': ('estado', 'fecha_emision', 'fecha_vencimiento', 'fecha_pago')
        }),
        ('Montos', {
            'fields': ('subtotal', 'iva', 'total')
        }),
        ('Observaciones', {
            'fields': ('observaciones',),
            'classes': ('collapse',)
        }),
    )
