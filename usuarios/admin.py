"""
DIGT SOFT - Módulo de Usuarios
Admin - Administración de Usuarios, Perfiles y Notificaciones
"""

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone
from .models import PerfilUsuario, Notificacion


class PerfilUsuarioInline(admin.StackedInline):
    """Inline para mostrar el perfil en la edición de usuario"""
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'Perfil de Usuario'
    fields = [
        'tipo_usuario', 'telefono', 'direccion', 'documento', 'foto',
        'activo', 'bloqueado', 'motivo_bloqueo', 'cliente'
    ]
    readonly_fields = ['fecha_registro', 'fecha_actualizacion']


class UserAdmin(BaseUserAdmin):
    """Admin personalizado para el modelo User"""
    inlines = (PerfilUsuarioInline,)
    list_display = [
        'username', 'email', 'nombre_completo', 'tipo_usuario_display',
        'estado_usuario', 'fecha_registro_display', 'acciones'
    ]
    list_filter = ['perfil__tipo_usuario', 'perfil__bloqueado', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'perfil__documento']

    def nombre_completo(self, obj):
        """Muestra el nombre completo del usuario"""
        return f"{obj.first_name} {obj.last_name}".strip() or "-"
    nombre_completo.short_description = "Nombre Completo"

    def tipo_usuario_display(self, obj):
        """Muestra el tipo de usuario con color"""
        if hasattr(obj, 'perfil'):
            tipo = obj.perfil.get_tipo_usuario_display()
            colores = {
                'ADMIN': '#e74c3c',
                'CLIENTE': '#3498db',
                'TECNICO': '#2ecc71',
                'PROVEEDOR': '#f39c12'
            }
            color = colores.get(obj.perfil.tipo_usuario, '#95a5a6')
            return format_html(
                '<span style="background-color: {}; color: white; padding: 3px 10px; '
                'border-radius: 3px; font-weight: bold;">{}</span>',
                color, tipo
            )
        return "-"
    tipo_usuario_display.short_description = "Tipo"

    def estado_usuario(self, obj):
        """Muestra el estado del usuario con indicadores visuales"""
        if hasattr(obj, 'perfil') and obj.perfil.bloqueado:
            return format_html(
                '<span style="color: #e74c3c; font-weight: bold;">'
                '<i class="fas fa-ban"></i> BLOQUEADO</span>'
            )
        elif obj.is_active:
            return format_html(
                '<span style="color: #2ecc71; font-weight: bold;">'
                '<i class="fas fa-check-circle"></i> ACTIVO</span>'
            )
        else:
            return format_html(
                '<span style="color: #95a5a6; font-weight: bold;">'
                '<i class="fas fa-times-circle"></i> INACTIVO</span>'
            )
    estado_usuario.short_description = "Estado"

    def fecha_registro_display(self, obj):
        """Muestra la fecha de registro del perfil"""
        if hasattr(obj, 'perfil'):
            return obj.perfil.fecha_registro.strftime('%d/%m/%Y %H:%M')
        return "-"
    fecha_registro_display.short_description = "Fecha de Registro"

    def acciones(self, obj):
        """Muestra botones de acción personalizados"""
        if hasattr(obj, 'perfil'):
            if obj.perfil.bloqueado:
                return format_html(
                    '<a class="button" href="{}">Desbloquear</a>',
                    reverse('admin:usuarios_perfil_desbloquear', args=[obj.perfil.pk])
                )
            else:
                return format_html(
                    '<a class="button" href="{}">Bloquear</a>',
                    reverse('admin:usuarios_perfil_bloquear', args=[obj.perfil.pk])
                )
        return "-"
    acciones.short_description = "Acciones"

    def get_queryset(self, request):
        """Optimiza las consultas"""
        qs = super().get_queryset(request)
        return qs.select_related('perfil')


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    """Admin para gestionar perfiles de usuario"""
    list_display = [
        'user', 'tipo_usuario', 'telefono', 'documento',
        'estado_display', 'fecha_registro'
    ]
    list_filter = ['tipo_usuario', 'bloqueado', 'activo', 'fecha_registro']
    search_fields = [
        'user__username', 'user__email', 'user__first_name',
        'user__last_name', 'documento', 'telefono'
    ]
    readonly_fields = ['fecha_registro', 'fecha_actualizacion', 'fecha_bloqueo']

    fieldsets = (
        ('Información de Usuario', {
            'fields': ('user', 'tipo_usuario')
        }),
        ('Datos de Contacto', {
            'fields': ('telefono', 'direccion', 'documento', 'foto')
        }),
        ('Control de Acceso', {
            'fields': ('activo', 'bloqueado', 'motivo_bloqueo', 'fecha_bloqueo'),
            'classes': ('collapse',)
        }),
        ('Relaciones', {
            'fields': ('cliente',),
            'classes': ('collapse',)
        }),
        ('Metadatos', {
            'fields': ('fecha_registro', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )

    actions = ['bloquear_usuarios', 'desbloquear_usuarios', 'marcar_como_clientes']

    def estado_display(self, obj):
        """Muestra el estado con colores"""
        if obj.bloqueado:
            return format_html(
                '<span style="background-color: #e74c3c; color: white; '
                'padding: 3px 8px; border-radius: 3px;">BLOQUEADO</span>'
            )
        elif obj.activo:
            return format_html(
                '<span style="background-color: #2ecc71; color: white; '
                'padding: 3px 8px; border-radius: 3px;">ACTIVO</span>'
            )
        return format_html(
            '<span style="background-color: #95a5a6; color: white; '
            'padding: 3px 8px; border-radius: 3px;">INACTIVO</span>'
        )
    estado_display.short_description = "Estado"

    def bloquear_usuarios(self, request, queryset):
        """Acción para bloquear usuarios seleccionados"""
        for perfil in queryset:
            if not perfil.bloqueado:
                perfil.bloquear(motivo="Bloqueado desde el panel de administración")

        count = queryset.count()
        self.message_user(
            request,
            f'{count} usuario(s) bloqueado(s) exitosamente.'
        )
    bloquear_usuarios.short_description = "Bloquear usuarios seleccionados"

    def desbloquear_usuarios(self, request, queryset):
        """Acción para desbloquear usuarios seleccionados"""
        for perfil in queryset:
            if perfil.bloqueado:
                perfil.desbloquear()

        count = queryset.count()
        self.message_user(
            request,
            f'{count} usuario(s) desbloqueado(s) exitosamente.'
        )
    desbloquear_usuarios.short_description = "Desbloquear usuarios seleccionados"

    def marcar_como_clientes(self, request, queryset):
        """Acción para marcar usuarios como clientes"""
        queryset.update(tipo_usuario='CLIENTE')
        count = queryset.count()
        self.message_user(
            request,
            f'{count} usuario(s) marcado(s) como clientes.'
        )
    marcar_como_clientes.short_description = "Marcar como clientes"


# Desregistrar el admin por defecto de User y registrar el personalizado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# ==============================================
# ADMIN DE NOTIFICACIONES
# ==============================================

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    """Admin para gestionar notificaciones"""
    list_display = [
        'titulo', 'usuario', 'tipo', 'estado_lectura',
        'fecha_creacion_display', 'acciones_notificacion'
    ]
    list_filter = ['tipo', 'leida', 'fecha_creacion']
    search_fields = ['titulo', 'mensaje', 'usuario__username', 'usuario__email']
    readonly_fields = ['fecha_creacion', 'fecha_lectura']
    date_hierarchy = 'fecha_creacion'

    fieldsets = (
        ('Información Principal', {
            'fields': ('usuario', 'titulo', 'mensaje', 'tipo')
        }),
        ('Estado', {
            'fields': ('leida', 'fecha_creacion', 'fecha_lectura')
        }),
        ('Opciones Adicionales', {
            'fields': ('url', 'icono', 'color'),
            'classes': ('collapse',)
        }),
    )

    actions = ['marcar_como_leidas', 'marcar_como_no_leidas', 'eliminar_leidas']

    def estado_lectura(self, obj):
        """Muestra el estado de lectura con colores"""
        if obj.leida:
            return format_html(
                '<span style="background-color: #27ae60; color: white; '
                'padding: 3px 8px; border-radius: 3px;">✓ LEÍDA</span>'
            )
        return format_html(
            '<span style="background-color: #3498db; color: white; '
            'padding: 3px 8px; border-radius: 3px;">● NO LEÍDA</span>'
        )
    estado_lectura.short_description = "Estado"

    def fecha_creacion_display(self, obj):
        """Muestra la fecha con tiempo transcurrido"""
        return format_html(
            '<div title="{}">{}</div>',
            obj.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
            obj.tiempo_transcurrido
        )
    fecha_creacion_display.short_description = "Creada hace"

    def acciones_notificacion(self, obj):
        """Muestra botones de acciones rápidas"""
        if obj.url:
            return format_html(
                '<a href="{}" class="button" target="_blank">Ver enlace</a>',
                obj.url
            )
        return "-"
    acciones_notificacion.short_description = "Acciones"

    def marcar_como_leidas(self, request, queryset):
        """Marca las notificaciones seleccionadas como leídas"""
        count = 0
        for notificacion in queryset:
            if not notificacion.leida:
                notificacion.marcar_como_leida()
                count += 1
        self.message_user(
            request,
            f'{count} notificación(es) marcada(s) como leída(s).'
        )
    marcar_como_leidas.short_description = "Marcar como leídas"

    def marcar_como_no_leidas(self, request, queryset):
        """Marca las notificaciones seleccionadas como no leídas"""
        queryset.update(leida=False, fecha_lectura=None)
        self.message_user(
            request,
            f'{queryset.count()} notificación(es) marcada(s) como no leída(s).'
        )
    marcar_como_no_leidas.short_description = "Marcar como no leídas"

    def eliminar_leidas(self, request, queryset):
        """Elimina las notificaciones leídas seleccionadas"""
        leidas = queryset.filter(leida=True)
        count = leidas.count()
        leidas.delete()
        self.message_user(
            request,
            f'{count} notificación(es) leída(s) eliminada(s).'
        )
    eliminar_leidas.short_description = "Eliminar notificaciones leídas"


# ==============================================
# ADMIN DE TOKENS DE RECUPERACIÓN
# ==============================================

from .models import PasswordResetToken


@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    """Admin para tokens de recuperación de contraseña"""
    
    list_display = [
        'user', 'token_corto', 'created_at', 'estado_display', 'used_at'
    ]
    list_filter = ['used', 'created_at']
    search_fields = ['user__username', 'user__email', 'token']
    readonly_fields = ['token', 'created_at', 'used_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Información del Token', {
            'fields': ('user', 'token', 'created_at')
        }),
        ('Estado', {
            'fields': ('used', 'used_at')
        }),
    )
    
    def token_corto(self, obj):
        """Muestra una versión corta del token"""
        token_str = str(obj.token)
        return f"{token_str[:8]}...{token_str[-8:]}"
    token_corto.short_description = "Token"
    
    def estado_display(self, obj):
        """Muestra el estado del token con colores"""
        if obj.used:
            return format_html(
                '<span style="background-color: #95a5a6; color: white; '
                'padding: 3px 10px; border-radius: 3px; font-weight: bold;">'
                '<i class="fas fa-check"></i> USADO</span>'
            )
        elif obj.is_valid():
            return format_html(
                '<span style="background-color: #2ecc71; color: white; '
                'padding: 3px 10px; border-radius: 3px; font-weight: bold;">'
                '<i class="fas fa-clock"></i> VÁLIDO</span>'
            )
        else:
            return format_html(
                '<span style="background-color: #e74c3c; color: white; '
                'padding: 3px 10px; border-radius: 3px; font-weight: bold;">'
                '<i class="fas fa-times"></i> EXPIRADO</span>'
            )
    estado_display.short_description = "Estado"
    
    def has_add_permission(self, request):
        """No permitir agregar tokens manualmente"""
        return False


