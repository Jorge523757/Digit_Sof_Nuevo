"""
DIGT SOFT - Módulo de Técnicos
Models - Gestión de Técnicos
"""

from django.db import models
from django.core.validators import RegexValidator


class Tecnico(models.Model):
    """
    Modelo para gestionar técnicos de la empresa
    """

    # Información Personal
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    numero_documento = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Número de Documento",
        validators=[RegexValidator(r'^\d+$', 'Solo se permiten números')]
    )

    # Información de Contacto
    telefono = models.CharField(
        max_length=15,
        verbose_name="Teléfono",
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Ingrese un número de teléfono válido')]
    )
    correo = models.EmailField(verbose_name="Correo Electrónico")

    # Información Profesional
    profesion = models.CharField(max_length=100, verbose_name="Profesión")

    # Estado
    activo = models.BooleanField(default=True, verbose_name="Activo")
    eliminado = models.BooleanField(default=False, verbose_name="Eliminado")
    fecha_eliminacion = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de Eliminación"
    )
    motivo_eliminacion = models.TextField(
        blank=True,
        verbose_name="Motivo de Eliminación"
    )

    # Metadatos
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"
        ordering = ['apellidos', 'nombres']
        db_table = 'tecnicos'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    @property
    def nombre_completo(self):
        """Retorna el nombre completo del técnico"""
        return f"{self.nombres} {self.apellidos}"

    def eliminar_logicamente(self, motivo=""):
        """Elimina el técnico de forma lógica"""
        from django.utils import timezone
        self.eliminado = True
        self.activo = False
        self.fecha_eliminacion = timezone.now()
        self.motivo_eliminacion = motivo
        self.save()

    def restaurar(self):
        """Restaura un técnico eliminado"""
        self.eliminado = False
        self.activo = True
        self.fecha_eliminacion = None
        self.motivo_eliminacion = ""
        self.save()

    @property
    def estado_display(self):
        """Retorna el estado del técnico para mostrar"""
        if self.eliminado:
            return "Eliminado"
        elif not self.activo:
            return "Inhabilitado"
        else:
            return "Habilitado"

