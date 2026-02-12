"""
DIGIT SOFT - Módulo de Backups
Models para gestión de copias de seguridad
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Backup(models.Model):
    """Modelo para registrar las copias de seguridad"""

    TIPO_CHOICES = [
        ('MANUAL', 'Manual'),
        ('AUTOMATICO', 'Automático'),
        ('PROGRAMADO', 'Programado'),
    ]

    ESTADO_CHOICES = [
        ('EXITOSO', 'Exitoso'),
        ('FALLIDO', 'Fallido'),
        ('EN_PROCESO', 'En Proceso'),
    ]

    nombre = models.CharField(max_length=200, verbose_name='Nombre del Backup')
    archivo = models.CharField(max_length=500, verbose_name='Ruta del Archivo')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='MANUAL')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='EN_PROCESO')
    tamaño = models.BigIntegerField(default=0, verbose_name='Tamaño en Bytes')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    error_mensaje = models.TextField(blank=True, null=True, verbose_name='Mensaje de Error')

    class Meta:
        verbose_name = 'Backup'
        verbose_name_plural = 'Backups'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"

    def get_tamaño_mb(self):
        """Retorna el tamaño en MB"""
        return round(self.tamaño / (1024 * 1024), 2)


class ConfiguracionBackup(models.Model):
    """Configuración para backups automáticos"""

    activo = models.BooleanField(default=False, verbose_name='Backup Automático Activo')
    frecuencia_horas = models.IntegerField(default=24, verbose_name='Frecuencia (horas)')
    max_backups = models.IntegerField(default=10, verbose_name='Máximo de Backups a Mantener')
    ruta_guardado = models.CharField(max_length=500, default='backups/', verbose_name='Ruta de Guardado')
    incluir_media = models.BooleanField(default=False, verbose_name='Incluir Archivos Media')
    notificar_admin = models.BooleanField(default=True, verbose_name='Notificar al Admin')
    ultimo_backup = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Configuración de Backup'
        verbose_name_plural = 'Configuraciones de Backup'

    def __str__(self):
        estado = 'Activo' if self.activo else 'Inactivo'
        return f"Configuración de Backups - {estado}"

