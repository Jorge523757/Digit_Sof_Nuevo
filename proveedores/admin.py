"""
DIGT SOFT - Admin del Módulo de Proveedores
"""

from django.contrib import admin
from .models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre_empresa', 'nit', 'nombre_contacto', 'telefono', 'calificacion', 'activo']
    list_filter = ['activo', 'calificacion', 'ciudad']
    search_fields = ['nombre_empresa', 'nit', 'nombre_contacto', 'email']
    ordering = ['nombre_empresa']
    list_per_page = 25
