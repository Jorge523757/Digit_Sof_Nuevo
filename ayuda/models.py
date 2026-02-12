"""
Modelos para el Sistema de Ayuda y Soporte
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CategoriaAyuda(models.Model):
    """Categorías para organizar los tickets"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=50, default='fa-question-circle')
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría de Ayuda'
        verbose_name_plural = 'Categorías de Ayuda'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class TicketAyuda(models.Model):
    """Tickets de soporte/ayuda de los usuarios"""

    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]

    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('en_proceso', 'En Proceso'),
        ('respondido', 'Respondido'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
    ]

    # Información del ticket
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_ayuda')
    categoria = models.ForeignKey(CategoriaAyuda, on_delete=models.SET_NULL, null=True, blank=True)
    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='media')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='abierto')

    # Archivos adjuntos (opcional)
    archivo = models.FileField(upload_to='tickets/%Y/%m/', null=True, blank=True)

    # Asignación
    asignado_a = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tickets_asignados'
    )

    # Fechas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)

    # Metadata
    ip_usuario = models.GenericIPAddressField(null=True, blank=True)
    navegador = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Ticket de Ayuda'
        verbose_name_plural = 'Tickets de Ayuda'
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['usuario', '-fecha_creacion']),
            models.Index(fields=['estado', '-fecha_creacion']),
        ]

    def __str__(self):
        return f"#{self.pk} - {self.asunto}"

    def marcar_resuelto(self):
        """Marca el ticket como resuelto"""
        self.estado = 'resuelto'
        self.fecha_resolucion = timezone.now()
        self.save()

    def get_tiempo_respuesta(self):
        """Calcula el tiempo de respuesta"""
        if self.fecha_resolucion:
            delta = self.fecha_resolucion - self.fecha_creacion
            return delta
        return None


class RespuestaTicket(models.Model):
    """Respuestas a los tickets"""
    ticket = models.ForeignKey(TicketAyuda, on_delete=models.CASCADE, related_name='respuestas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    archivo = models.FileField(upload_to='respuestas/%Y/%m/', null=True, blank=True)
    es_staff = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Respuesta de Ticket'
        verbose_name_plural = 'Respuestas de Tickets'
        ordering = ['fecha_creacion']

    def __str__(self):
        return f"Respuesta de {self.usuario.username} en #{self.ticket.pk}"


class FAQ(models.Model):
    """Preguntas Frecuentes"""
    categoria = models.ForeignKey(CategoriaAyuda, on_delete=models.SET_NULL, null=True, blank=True)
    pregunta = models.CharField(max_length=300)
    respuesta = models.TextField()
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    vistas = models.IntegerField(default=0)
    util = models.IntegerField(default=0)  # Contador de "Fue útil"
    no_util = models.IntegerField(default=0)  # Contador de "No fue útil"
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pregunta Frecuente'
        verbose_name_plural = 'Preguntas Frecuentes'
        ordering = ['orden', '-fecha_creacion']

    def __str__(self):
        return self.pregunta

    def incrementar_vista(self):
        """Incrementa el contador de vistas"""
        self.vistas += 1
        self.save(update_fields=['vistas'])

