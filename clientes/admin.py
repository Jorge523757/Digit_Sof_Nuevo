from django.contrib import admin
from django.utils.html import format_html
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_completo', 'numero_documento', 'correo', 'telefono',
        'usuario_asociado', 'estado_display', 'fecha_registro'
    )
    search_fields = ('nombres', 'apellidos', 'numero_documento', 'correo', 'telefono')
    list_filter = ('activo', 'fecha_registro')
    readonly_fields = ('fecha_registro', 'fecha_actualizacion')

    fieldsets = (
        ('Información Personal', {
            'fields': ('nombres', 'apellidos', 'numero_documento')
        }),
        ('Información de Contacto', {
            'fields': ('telefono', 'correo', 'direccion')
        }),
        ('Estado', {
            'fields': ('activo', 'observaciones')
        }),
        ('Metadatos', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )

    def usuario_asociado(self, obj):
        """Muestra si el cliente tiene usuario asociado"""
        if hasattr(obj, 'usuario_perfil') and obj.usuario_perfil.exists():
            perfil = obj.usuario_perfil.first()
            return format_html(
                '<span style="color: #2ecc71;">'
                '<i class="fas fa-user-check"></i> {}</span>',
                perfil.user.username
            )
        return format_html(
            '<span style="color: #95a5a6;">'
            '<i class="fas fa-user-times"></i> Sin usuario</span>'
        )
    usuario_asociado.short_description = "Usuario"

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


