from django.contrib import admin
from .models import RegistroDano, ImagenDano, DocumentoFactura, NotaDano


@admin.register(RegistroDano)
class RegistroDanoAdmin(admin.ModelAdmin):
    list_display = ['numero_reporte', 'cliente', 'fecha_reporte', 'estado', 'usuario']
    list_filter = ['fecha_reporte', 'estado', 'notificado_admin']
    search_fields = ['numero_reporte', 'descripcion_dano', 'cliente__nombre']
    readonly_fields = ['numero_reporte', 'fecha_reporte', 'fecha_actualizacion']
    fieldsets = (
        ('Información del Reporte', {
            'fields': ('numero_reporte', 'fecha_reporte', 'cliente', 'usuario', 'equipo')
        }),
        ('Detalles del Daño', {
            'fields': ('descripcion_dano', 'tiempo_requerido_cliente', 'observaciones')
        }),
        ('Estado', {
            'fields': ('estado', 'notificado_admin', 'fecha_notificacion_admin')
        }),
        ('Orden de Servicio', {
            'fields': ('orden',)
        }),
    )


@admin.register(ImagenDano)
class ImagenDanoAdmin(admin.ModelAdmin):
    list_display = ['registro', 'es_principal', 'fecha_subida']
    list_filter = ['es_principal', 'fecha_subida']


@admin.register(DocumentoFactura)
class DocumentoFacturaAdmin(admin.ModelAdmin):
    list_display = ['registro', 'tipo_documento', 'fecha_generacion']
    list_filter = ['tipo_documento', 'fecha_generacion']


@admin.register(NotaDano)
class NotaDanoAdmin(admin.ModelAdmin):
    list_display = ['registro', 'autor', 'es_publica', 'fecha_creacion']
    list_filter = ['es_publica', 'fecha_creacion']

