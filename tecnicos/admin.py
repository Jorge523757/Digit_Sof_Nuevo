"""
DIGT SOFT - Módulo de Técnicos
Admin - Configuración del panel de administración
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Tecnico


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_completo', 'numero_documento', 'telefono',
        'correo', 'profesion', 'estado_display', 'fecha_registro'
    )
    search_fields = ('nombres', 'apellidos', 'numero_documento', 'correo', 'telefono', 'profesion')
    list_filter = ('activo', 'profesion', 'fecha_registro')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')

    fieldsets = (
        ('Información Personal', {
            'fields': ('nombres', 'apellidos', 'numero_documento')
        }),
        ('Información de Contacto', {
            'fields': ('telefono', 'correo')
        }),
        ('Información Profesional', {
            'fields': ('profesion',)
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
        ('Metadatos', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )

    def estado_display(self, obj):
        """Muestra el estado con colores"""
        if obj.activo:
            return format_html(
                '<span style="background-color: #2ecc71; color: white; '
                'padding: 3px 8px; border-radius: 3px;">ACTIVO</span>'
            )
        return format_html(
            '<span style="background-color: #e74c3c; color: white; '
            'padding: 3px 8px; border-radius: 3px;">INACTIVO</span>'
        )
    estado_display.short_description = "Estado"

