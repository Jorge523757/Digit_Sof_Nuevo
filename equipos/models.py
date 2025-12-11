"""
DIGIT SOFT - Módulo de Equipos
Models - Inventario de Equipos de la Empresa
"""

from django.db import models


class Equipo(models.Model):
    """Modelo para equipos de la empresa"""

    TIPO_EQUIPO = [
        ('COMPUTADOR', 'Computador'),
        ('LAPTOP', 'Laptop'),
        ('IMPRESORA', 'Impresora'),
        ('SERVIDOR', 'Servidor'),
        ('ROUTER', 'Router'),
        ('OTRO', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('OPERATIVO', 'Operativo'),
        ('EN_REPARACION', 'En Reparación'),
        ('FUERA_SERVICIO', 'Fuera de Servicio'),
        ('ASIGNADO', 'Asignado'),
        ('DISPONIBLE', 'Disponible'),
    ]

    codigo_equipo = models.CharField(max_length=20, unique=True, verbose_name="Código de equipo")
    nombre = models.CharField(max_length=200, verbose_name="Nombre del equipo")
    tipo_equipo = models.CharField(max_length=20, choices=TIPO_EQUIPO, verbose_name="Tipo")

    marca = models.CharField(max_length=100, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    numero_serie = models.CharField(max_length=100, blank=True, verbose_name="Número de serie")

    especificaciones = models.TextField(blank=True, verbose_name="Especificaciones técnicas")
    fecha_adquisicion = models.DateField(verbose_name="Fecha de adquisición")
    valor_adquisicion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de adquisición")

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE', verbose_name="Estado")
    ubicacion = models.CharField(max_length=200, blank=True, verbose_name="Ubicación")
    responsable = models.CharField(max_length=150, blank=True, verbose_name="Responsable")

    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['codigo_equipo']
        db_table = 'equipos'

    def __str__(self):
        return f"{self.codigo_equipo} - {self.nombre}"
