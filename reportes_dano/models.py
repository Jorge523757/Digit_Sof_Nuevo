"""
DIGT SOFT - Modelos para Registro de Daños
Temporal: Versión simplificada para integración inicial
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class RegistroDano(models.Model):
    """Registro básico de daños reportados"""

    numero_factura = models.CharField(max_length=50, unique=True, blank=True)
    fecha_reporte = models.DateTimeField(default=timezone.now)
    descripcion_dano = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Relación con Orden de Servicio
    orden = models.ForeignKey(
        'ordenes.OrdenServicio',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reportes_dano',
        verbose_name="Orden de Servicio"
    )

    class Meta:
        verbose_name = "Registro de Daño"
        verbose_name_plural = "Registros de Daños"

    def __str__(self):
        return f"Reporte {self.numero_factura or self.id}"


class ImagenDano(models.Model):
    """Imágenes del daño"""
    registro = models.ForeignKey(RegistroDano, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='reportes_dano/')
    es_principal = models.BooleanField(default=False)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Imagen de Daño"
        verbose_name_plural = "Imágenes de Daños"

    def __str__(self):
        return f"Imagen - {self.registro}"


class DocumentoFactura(models.Model):
    """Documentos generados"""
    registro = models.ForeignKey(RegistroDano, on_delete=models.CASCADE, related_name='documentos')
    tipo_documento = models.CharField(max_length=10, choices=[('PDF', 'PDF'), ('TXT', 'TXT')])
    archivo = models.FileField(upload_to='facturas_dano/')
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Documento de Factura"
        verbose_name_plural = "Documentos de Facturas"

    def __str__(self):
        return f"{self.tipo_documento} - {self.registro}"


class NotaDano(models.Model):
    """Notas sobre el daño"""
    registro = models.ForeignKey(RegistroDano, on_delete=models.CASCADE, related_name='notas')
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contenido = models.TextField()
    es_publica = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Nota de Daño"
        verbose_name_plural = "Notas de Daños"

    def __str__(self):
        return f"Nota - {self.registro}"

