"""
DIGT SOFT - Módulo de Órdenes de Servicio
Models - Gestión de Órdenes de Servicio Técnico
"""

from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from clientes.models import Cliente
from tecnicos.models import Tecnico
from productos.models import Producto


class OrdenServicio(models.Model):
    """
    Modelo principal de Órdenes de Servicio Técnico
    """

    ESTADO_CHOICES = [
        ('RECIBIDA', 'Recibida'),
        ('EN_DIAGNOSTICO', 'En Diagnóstico'),
        ('DIAGNOSTICADA', 'Diagnosticada'),
        ('EN_REPARACION', 'En Reparación'),
        ('REPARADA', 'Reparada'),
        ('EN_ESPERA_REPUESTOS', 'Esperando Repuestos'),
        ('EN_ESPERA_CLIENTE', 'Esperando Cliente'),
        ('LISTA_ENTREGA', 'Lista para Entrega'),
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
    numero_orden = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Número de orden",
        help_text="Generado automáticamente"
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='ordenes',
        verbose_name="Cliente"
    )
    tecnico_asignado = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ordenes_asignadas',
        verbose_name="Técnico asignado"
    )

    # Detalles del equipo
    tipo_equipo = models.CharField(
        max_length=100,
        verbose_name="Tipo de equipo",
        help_text="Ej: Laptop, PC, Impresora"
    )
    marca = models.CharField(max_length=100, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    serie = models.CharField(max_length=100, blank=True, verbose_name="Número de serie")

    # Problema reportado
    falla_reportada = models.TextField(verbose_name="Falla reportada por el cliente")
    estado_fisico = models.TextField(
        blank=True,
        verbose_name="Estado físico del equipo",
        help_text="Descripción del estado físico al recibir"
    )
    accesorios_incluidos = models.TextField(
        blank=True,
        verbose_name="Accesorios incluidos",
        help_text="Ej: Cargador, mouse, bolso, etc."
    )

    # Diagnóstico técnico
    diagnostico = models.TextField(blank=True, verbose_name="Diagnóstico técnico")
    solucion_aplicada = models.TextField(blank=True, verbose_name="Solución aplicada")

    # Estado y prioridad
    estado = models.CharField(
        max_length=25,
        choices=ESTADO_CHOICES,
        default='RECIBIDA',
        verbose_name="Estado"
    )
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDAD_CHOICES,
        default='MEDIA',
        verbose_name="Prioridad"
    )

    # Costos
    costo_diagnostico = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Costo de diagnóstico"
    )
    costo_mano_obra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Costo mano de obra"
    )
    costo_repuestos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Costo repuestos"
    )
    costo_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Costo total"
    )

    # Pago
    pagado = models.BooleanField(default=False, verbose_name="Pagado")
    fecha_pago = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de pago")

    # Fechas importantes
    fecha_recepcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de recepción")
    fecha_compromiso = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de compromiso",
        help_text="Fecha estimada de entrega"
    )
    fecha_entrega = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de entrega")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    # Garantía
    tiene_garantia = models.BooleanField(default=True, verbose_name="Tiene garantía")
    dias_garantia = models.IntegerField(default=30, verbose_name="Días de garantía")

    # Notas
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    notas_internas = models.TextField(blank=True, verbose_name="Notas internas")

    class Meta:
        verbose_name = "Orden de Servicio"
        verbose_name_plural = "Órdenes de Servicio"
        ordering = ['-fecha_recepcion']
        db_table = 'ordenes_servicio'
        indexes = [
            models.Index(fields=['numero_orden']),
            models.Index(fields=['cliente', 'fecha_recepcion']),
            models.Index(fields=['estado']),
            models.Index(fields=['tecnico_asignado']),
        ]

    def __str__(self):
        return f"Orden {self.numero_orden} - {self.cliente.nombre_completo}"

    def save(self, *args, **kwargs):
        if not self.numero_orden:
            # Generar número de orden automático
            ultimo_numero = OrdenServicio.objects.count() + 1
            self.numero_orden = f"OS-{ultimo_numero:06d}"

        # Calcular costo total
        self.costo_total = self.costo_diagnostico + self.costo_mano_obra + self.costo_repuestos

        super().save(*args, **kwargs)

    @property
    def dias_en_servicio(self):
        """Calcula los días que lleva la orden en servicio"""
        from django.utils import timezone
        if self.fecha_entrega:
            return (self.fecha_entrega - self.fecha_recepcion).days
        return (timezone.now() - self.fecha_recepcion).days

    @property
    def esta_atrasada(self):
        """Verifica si la orden está atrasada"""
        from django.utils import timezone
        if self.fecha_compromiso and not self.fecha_entrega:
            return timezone.now() > self.fecha_compromiso
        return False


class RepuestoOrden(models.Model):
    """
    Repuestos utilizados en una orden de servicio
    """
    orden = models.ForeignKey(
        OrdenServicio,
        on_delete=models.CASCADE,
        related_name='repuestos',
        verbose_name="Orden de servicio"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='ordenes_servicio',
        verbose_name="Producto/Repuesto"
    )
    cantidad = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Cantidad"
    )
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio unitario"
    )
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Subtotal"
    )

    class Meta:
        verbose_name = "Repuesto de Orden"
        verbose_name_plural = "Repuestos de Órdenes"
        db_table = 'ordenes_repuestos'

    def __str__(self):
        return f"{self.producto.nombre_producto} x{self.cantidad}"

    def save(self, *args, **kwargs):
        self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)
        # Actualizar costo de repuestos en la orden
        self.orden.costo_repuestos = sum(
            r.subtotal for r in self.orden.repuestos.all()
        )
        self.orden.save()


class SeguimientoOrden(models.Model):
    """
    Seguimiento de estados y acciones de la orden
    """
    orden = models.ForeignKey(
        OrdenServicio,
        on_delete=models.CASCADE,
        related_name='seguimientos',
        verbose_name="Orden de servicio"
    )
    estado_anterior = models.CharField(max_length=25, verbose_name="Estado anterior")
    estado_nuevo = models.CharField(max_length=25, verbose_name="Estado nuevo")
    descripcion = models.TextField(verbose_name="Descripción del cambio")
    usuario = models.CharField(max_length=100, blank=True, verbose_name="Usuario")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
        verbose_name = "Seguimiento de Orden"
        verbose_name_plural = "Seguimientos de Órdenes"
        ordering = ['-fecha']
        db_table = 'ordenes_seguimiento'

    def __str__(self):
        return f"{self.orden.numero_orden} - {self.estado_anterior} → {self.estado_nuevo}"

