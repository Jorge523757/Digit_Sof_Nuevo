"""
DIGT SOFT - Módulo de Equipos
Models - Gestión de Equipos de Clientes
"""

from django.db import models
from clientes.models import Cliente


class Equipo(models.Model):
    """Modelo para gestionar equipos de clientes"""

    TIPO_EQUIPO_CHOICES = [
        ('LAPTOP', 'Laptop'),
        ('DESKTOP', 'PC de Escritorio'),
        ('TABLET', 'Tablet'),
        ('CELULAR', 'Celular'),
        ('IMPRESORA', 'Impresora'),
        ('OTRO', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('EN_REPARACION', 'En Reparación'),
        ('INACTIVO', 'Inactivo'),
    ]

    # Información del equipo
    tipo_equipo = models.CharField(
        max_length=20,
        choices=TIPO_EQUIPO_CHOICES,
        verbose_name="Tipo de Equipo"
    )
    marca = models.CharField(max_length=100, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    numero_serie = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Número de Serie"
    )

    # Especificaciones técnicas
    procesador = models.CharField(max_length=100, blank=True, verbose_name="Procesador")
    memoria_ram = models.CharField(max_length=50, blank=True, verbose_name="Memoria RAM")
    almacenamiento = models.CharField(max_length=50, blank=True, verbose_name="Almacenamiento")
    sistema_operativo = models.CharField(max_length=100, blank=True, verbose_name="Sistema Operativo")

    # Relación con cliente
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='equipos',
        verbose_name="Cliente"
    )

    # Información de compra
    fecha_compra = models.DateField(null=True, blank=True, verbose_name="Fecha de Compra")
    factura_compra = models.CharField(max_length=100, blank=True, verbose_name="Factura de Compra")

    # Estado y observaciones
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='ACTIVO',
        verbose_name="Estado"
    )
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    # Metadatos
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.numero_serie}"

    @property
    def nombre_completo(self):
        """Retorna el nombre completo del equipo"""
        return f"{self.get_tipo_equipo_display()} {self.marca} {self.modelo}"


