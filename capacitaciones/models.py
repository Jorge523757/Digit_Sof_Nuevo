"""
DIGT SOFT - Módulo de Capacitaciones
Models - Gestión de Capacitaciones y Entrenamientos
"""

from django.db import models
from tecnicos.models import Tecnico


class Capacitacion(models.Model):
    """Modelo para capacitaciones"""

    TIPO_CHOICES = [
        ('TECNICA', 'Capacitación Técnica'),
        ('SOFTWARE', 'Software'),
        ('ATENCION_CLIENTE', 'Atención al Cliente'),
        ('SEGURIDAD', 'Seguridad'),
        ('OTRA', 'Otra'),
    ]

    ESTADO_CHOICES = [
        ('PROGRAMADA', 'Programada'),
        ('EN_CURSO', 'En Curso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    codigo_capacitacion = models.CharField(max_length=20, unique=True, verbose_name="Código")
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la capacitación")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo")

    descripcion = models.TextField(verbose_name="Descripción")
    instructor = models.CharField(max_length=150, verbose_name="Instructor")

    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    duracion_horas = models.IntegerField(verbose_name="Duración (horas)")

    lugar = models.CharField(max_length=200, verbose_name="Lugar")
    modalidad = models.CharField(
        max_length=20,
        choices=[('PRESENCIAL', 'Presencial'), ('VIRTUAL', 'Virtual'), ('HIBRIDA', 'Híbrida')],
        default='PRESENCIAL',
        verbose_name="Modalidad"
    )

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PROGRAMADA', verbose_name="Estado")
    cupo_maximo = models.IntegerField(default=20, verbose_name="Cupo máximo")

    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Costo")
    certificado = models.BooleanField(default=True, verbose_name="Otorga certificado")

    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Capacitación"
        verbose_name_plural = "Capacitaciones"
        ordering = ['-fecha_inicio']
        db_table = 'capacitaciones'

    def __str__(self):
        return f"{self.codigo_capacitacion} - {self.nombre}"

    @property
    def cupos_disponibles(self):
        return self.cupo_maximo - self.participantes.count()


class ParticipanteCapacitacion(models.Model):
    """Participantes inscritos en capacitaciones"""

    capacitacion = models.ForeignKey(
        Capacitacion,
        on_delete=models.CASCADE,
        related_name='participantes',
        verbose_name="Capacitación"
    )
    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.CASCADE,
        related_name='capacitaciones',
        verbose_name="Técnico"
    )

    fecha_inscripcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de inscripción")
    asistio = models.BooleanField(default=False, verbose_name="Asistió")
    aprobado = models.BooleanField(default=False, verbose_name="Aprobado")
    calificacion = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Calificación"
    )

    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
        unique_together = ['capacitacion', 'tecnico']
        db_table = 'capacitaciones_participantes'

    def __str__(self):
        return f"{self.tecnico.nombre_completo} - {self.capacitacion.nombre}"

