"""
DIGIT SOFT - Módulo de Backups
Admin
"""

from django.contrib import admin
from .models import Backup, ConfiguracionBackup


@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'estado', 'get_tamaño_mb', 'fecha_creacion', 'usuario']
    list_filter = ['tipo', 'estado', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    readonly_fields = ['archivo', 'tamaño', 'fecha_creacion', 'usuario', 'error_mensaje']

    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'tipo', 'estado', 'descripcion')
        }),
        ('Detalles del Archivo', {
            'fields': ('archivo', 'tamaño', 'fecha_creacion')
        }),
        ('Usuario y Errores', {
            'fields': ('usuario', 'error_mensaje')
        }),
    )


@admin.register(ConfiguracionBackup)
class ConfiguracionBackupAdmin(admin.ModelAdmin):
    list_display = ['activo', 'frecuencia_horas', 'max_backups', 'ultimo_backup']

    def has_add_permission(self, request):
        # Solo permitir una configuración
        return not ConfiguracionBackup.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # No permitir eliminar la configuración
        return False

