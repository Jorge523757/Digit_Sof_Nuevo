"""
DIGT SOFT - Módulo de Proveedores
Models - Gestión de Proveedores
"""

from django.db import models
from django.core.validators import RegexValidator


class Proveedor(models.Model):
    """Modelo para gestionar proveedores"""

    TIPO_DOCUMENTO_CHOICES = [
        ('NIT', 'NIT'),
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
    ]

    # Información básica
    razon_social = models.CharField(max_length=200, verbose_name="Razón Social")
    nombre_comercial = models.CharField(max_length=200, blank=True, verbose_name="Nombre Comercial")

    tipo_documento = models.CharField(
        max_length=3,
        choices=TIPO_DOCUMENTO_CHOICES,
        default='NIT',
        verbose_name="Tipo de Documento"
    )
    numero_documento = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Número de Documento",
        validators=[RegexValidator(r'^\d+$', 'Solo se permiten números')]
    )

    # Información de contacto
    telefono = models.CharField(
        max_length=15,
        verbose_name="Teléfono",
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Ingrese un número de teléfono válido')]
    )
    correo = models.EmailField(verbose_name="Correo Electrónico")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    pais = models.CharField(max_length=100, default="Colombia", verbose_name="País")

    # Información comercial
    contacto_principal = models.CharField(max_length=150, blank=True, verbose_name="Contacto Principal")
    telefono_contacto = models.CharField(max_length=15, blank=True, verbose_name="Teléfono de Contacto")
    sitio_web = models.URLField(blank=True, verbose_name="Sitio Web")

    # Observaciones
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    # Estado
    activo = models.BooleanField(default=True, verbose_name="Activo")

    # Metadatos
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['razon_social']

    def __str__(self):
        return self.razon_social or self.nombre_comercial

    @property
    def nombre_completo(self):
        """Retorna el nombre completo del proveedor"""
        if self.nombre_comercial:
            return f"{self.razon_social} ({self.nombre_comercial})"
        return self.razon_social


