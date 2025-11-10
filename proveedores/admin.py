"""
DIGT SOFT - Admin del Módulo de Proveedores
"""

from django.contrib import admin
from .models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    """Admin para Proveedores"""
    list_display = ('razon_social', 'nombre_comercial', 'tipo_documento', 'numero_documento', 'telefono', 'ciudad', 'activo')
    list_filter = ('tipo_documento', 'activo', 'ciudad', 'pais')
    search_fields = ('razon_social', 'nombre_comercial', 'numero_documento', 'correo', 'contacto_principal')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('razon_social', 'nombre_comercial', 'tipo_documento', 'numero_documento')
        }),
        ('Información de Contacto', {
            'fields': ('telefono', 'correo', 'direccion', 'ciudad', 'pais')
        }),
        ('Información Comercial', {
            'fields': ('contacto_principal', 'telefono_contacto', 'sitio_web')
        }),
        ('Observaciones y Estado', {
            'fields': ('observaciones', 'activo', 'fecha_registro', 'fecha_actualizacion')
        }),
    )

