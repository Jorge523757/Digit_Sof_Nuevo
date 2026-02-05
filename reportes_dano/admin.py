from django.contrib import admin
from .models import RegistroDano, ImagenDano, DocumentoFactura, NotaDano


@admin.register(RegistroDano)
class RegistroDanoAdmin(admin.ModelAdmin):
    list_display = ['numero_factura', 'fecha_reporte', 'usuario']
    list_filter = ['fecha_reporte']
    search_fields = ['numero_factura', 'descripcion_dano']


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

