"""
DIGT SOFT - Módulo de Proveedores
Models - Gestión de Proveedores
"""

from django.db import models
from django.core.validators import RegexValidator


class Proveedor(models.Model):
    """
    Modelo para gestionar proveedores de la empresa
    """

    # Información básica
    nombre_empresa = models.CharField(max_length=200, verbose_name="Nombre de la empresa")
    nit = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="NIT",
        validators=[RegexValidator(r'^\d+-?\d*$', 'Ingrese un NIT válido')]
    )

    # Información de contacto
    nombre_contacto = models.CharField(max_length=150, verbose_name="Nombre del contacto")
    telefono = models.CharField(
        max_length=15,
        verbose_name="Teléfono",
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Ingrese un número válido')]
    )
    email = models.EmailField(verbose_name="Correo electrónico")

    # Ubicación
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    ciudad = models.CharField(max_length=100, blank=True, verbose_name="Ciudad")
    pais = models.CharField(max_length=100, default='Colombia', verbose_name="País")

    # Información comercial
    productos_servicios = models.TextField(
        blank=True,
        verbose_name="Productos/Servicios que ofrece",
        help_text="Descripción de lo que suministra el proveedor"
    )
    condiciones_pago = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Condiciones de pago",
        help_text="Ej: 30 días, contado, etc."
    )
    tiempo_entrega = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Tiempo de entrega",
        help_text="Tiempo promedio de entrega"
    )

    # Calificación
    CALIFICACION_CHOICES = [
        (1, '⭐ Malo'),
        (2, '⭐⭐ Regular'),
        (3, '⭐⭐⭐ Bueno'),
        (4, '⭐⭐⭐⭐ Muy Bueno'),
        (5, '⭐⭐⭐⭐⭐ Excelente'),
    ]
    calificacion = models.IntegerField(
        choices=CALIFICACION_CHOICES,
        default=3,
        verbose_name="Calificación"
    )

    # Estado
    activo = models.BooleanField(default=True, verbose_name="Activo")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    # Auditoría
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre_empresa']
        db_table = 'proveedores'

    def __str__(self):
        return f"{self.nombre_empresa} - {self.nit}"

    @property
    def nombre_completo_contacto(self):
        """Retorna nombre y empresa del contacto"""
        return f"{self.nombre_contacto} ({self.nombre_empresa})"

