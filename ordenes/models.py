"""
DIGT SOFT - Módulo de Órdenes de Servicio
Models - Gestión de Órdenes de Servicio Técnico
"""

from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from clientes.models import Cliente
from tecnicos.models import Tecnico


class OrdenServicio(models.Model):
    """Modelo principal de Órdenes de Servicio"""

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('DIAGNOSTICADA', 'Diagnosticada'),
        ('REPARADA', 'Reparada'),
        ('ENTREGADA', 'Entregada'),
        ('CANCELADA', 'Cancelada'),
    ]

    PRIORIDAD_CHOICES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('URGENTE', 'Urgente'),
    ]

    # Información básica
    numero_orden = models.CharField(max_length=50, unique=True, verbose_name="Número de Orden")
    fecha_ingreso = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Ingreso")
    fecha_compromiso = models.DateField(null=True, blank=True, verbose_name="Fecha de Compromiso")

    # Relaciones
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='ordenes_servicio',
        verbose_name="Cliente"
    )
    tecnico_asignado = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ordenes_asignadas',
        verbose_name="Técnico Asignado"
    )

    # Información del equipo
    tipo_equipo = models.CharField(max_length=100, verbose_name="Tipo de Equipo")
    marca = models.CharField(max_length=100, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    serie = models.CharField(max_length=100, blank=True, verbose_name="Número de Serie")

    # Descripción del problema
    falla_reportada = models.TextField(verbose_name="Falla Reportada por el Cliente")
    diagnostico = models.TextField(blank=True, verbose_name="Diagnóstico Técnico")
    solucion = models.TextField(blank=True, verbose_name="Solución Aplicada")

    # Accesorios y estado físico
    accesorios = models.TextField(blank=True, verbose_name="Accesorios Incluidos")
    estado_fisico = models.TextField(blank=True, verbose_name="Estado Físico del Equipo")

    # Estado y prioridad
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='PENDIENTE',
        verbose_name="Estado"
    )
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDAD_CHOICES,
        default='MEDIA',
        verbose_name="Prioridad"
    )

    # Costos
    costo_mano_obra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Costo de Mano de Obra"
    )
    costo_repuestos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Costo de Repuestos"
    )

    # Observaciones
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    # Metadatos
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    fecha_entrega = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Entrega")

    class Meta:
        verbose_name = "Orden de Servicio"
        verbose_name_plural = "Órdenes de Servicio"
        ordering = ['-fecha_ingreso']

    def __str__(self):
        return f"OS {self.numero_orden} - {self.cliente.nombre_completo}"

    @property
    def costo_total(self):
        """Calcula el costo total de la orden"""
        return self.costo_mano_obra + self.costo_repuestos

    @property
    def dias_en_servicio(self):
        """Calcula los días que lleva el equipo en servicio"""
        from django.utils import timezone
        if self.fecha_entrega:
            return (self.fecha_entrega.date() - self.fecha_ingreso.date()).days
        return (timezone.now().date() - self.fecha_ingreso.date()).days


class SeguimientoOrden(models.Model):
    """Seguimiento de cambios en la orden"""

    orden = models.ForeignKey(
        OrdenServicio,
        on_delete=models.CASCADE,
        related_name='seguimientos',
        verbose_name="Orden de Servicio"
    )
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    descripcion = models.TextField(verbose_name="Descripción del Seguimiento")
    estado_anterior = models.CharField(max_length=20, blank=True, verbose_name="Estado Anterior")
    estado_nuevo = models.CharField(max_length=20, blank=True, verbose_name="Estado Nuevo")

    class Meta:
        verbose_name = "Seguimiento de Orden"
        verbose_name_plural = "Seguimientos de Órdenes"
        ordering = ['-fecha']

    def __str__(self):
        return f"Seguimiento {self.orden.numero_orden} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"


