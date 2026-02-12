"""
DIGIT SOFT - Modelos para Registro de Daños
Reportes de equipos dañados por clientes
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class RegistroDano(models.Model):
    """Registro de daños reportados por clientes"""

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('REVISADO', 'Revisado por Admin'),
        ('ASIGNADO', 'Asignado a Técnico'),
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado'),
    ]

    # Información básica
    numero_reporte = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Número de reporte"
    )
    fecha_reporte = models.DateTimeField(
        default=timezone.now,
        verbose_name="Fecha de reporte"
    )

    # Cliente y usuario
    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='reportes_dano',
        verbose_name="Cliente"
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Usuario que reportó"
    )

    # Equipo
    equipo = models.ForeignKey(
        'equipos.Equipo',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reportes_dano',
        verbose_name="Equipo"
    )

    # Descripción del daño
    descripcion_dano = models.TextField(verbose_name="Descripción del daño")
    tiempo_requerido_cliente = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Tiempo requerido por cliente",
        help_text="Cuándo necesita el equipo"
    )

    # Estado
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='PENDIENTE',
        verbose_name="Estado"
    )

    # Notificación
    notificado_admin = models.BooleanField(
        default=False,
        verbose_name="Administrador notificado"
    )
    fecha_notificacion_admin = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha notificación admin"
    )

    # Relación con Orden de Servicio
    orden = models.ForeignKey(
        'ordenes.OrdenServicio',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reportes_dano',
        verbose_name="Orden de Servicio"
    )

    # Metadatos
    observaciones = models.TextField(
        blank=True,
        verbose_name="Observaciones"
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización"
    )

    class Meta:
        verbose_name = "Registro de Daño"
        verbose_name_plural = "Registros de Daños"
        ordering = ['-fecha_reporte']
        db_table = 'reportes_dano'

    def __str__(self):
        return f"Reporte {self.numero_reporte or self.id} - {self.cliente.nombre_completo}"

    def save(self, *args, **kwargs):
        if not self.numero_reporte:
            # Generar número de reporte automático
            ultimo_numero = RegistroDano.objects.count() + 1
            self.numero_reporte = f"RD-{ultimo_numero:06d}"
        super().save(*args, **kwargs)


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

