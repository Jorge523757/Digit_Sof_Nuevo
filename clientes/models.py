"""
DIGIT SOFT - Módulo de Clientes
Models - HU1: Gestión de Clientes
"""

from django.db import models
from django.core.validators import EmailValidator

class Cliente(models.Model):
    """Modelo Cliente - HU1"""

    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    numero_documento = models.CharField(max_length=20, unique=True, verbose_name="Número de Documento")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    correo = models.EmailField(validators=[EmailValidator()], verbose_name="Correo Electrónico")
    direccion = models.TextField(verbose_name="Dirección")
    activo = models.BooleanField(default=True, verbose_name="Cliente Activo")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-fecha_registro']
        db_table = 'clientes'

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.numero_documento}"

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"