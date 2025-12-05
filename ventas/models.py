"""
DIGT SOFT - Módulo de Ventas
Models - Gestión de Ventas integrado con Productos (E-commerce)
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from clientes.models import Cliente
from productos.models import Producto


class Venta(models.Model):
    """
    Modelo principal de Ventas - Integrado con E-commerce
    """

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('PROCESANDO', 'Procesando'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
        ('DEVUELTA', 'Devuelta'),
    ]

    METODO_PAGO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('PSE', 'PSE'),
        ('CREDITO', 'Crédito'),
    ]

    CANAL_VENTA_CHOICES = [
        ('TIENDA', 'Tienda Física'),
        ('WEB', 'Tienda Online'),
        ('TELEFONO', 'Teléfono'),
        ('WHATSAPP', 'WhatsApp'),
    ]

    # Información básica
    numero_venta = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        verbose_name="Número de venta",
        help_text="Generado automáticamente"
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='ventas',
        verbose_name="Cliente"
    )

    # Usuario que realiza la venta
    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='ventas_realizadas',
        verbose_name="Usuario",
        null=True,
        blank=True
    )

    # Detalles de la venta
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de venta")
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='PENDIENTE',
        verbose_name="Estado"
    )
    canal_venta = models.CharField(
        max_length=20,
        choices=CANAL_VENTA_CHOICES,
        default='TIENDA',
        verbose_name="Canal de venta"
    )

    # Montos
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="Subtotal"
    )
    descuento = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Descuento"
    )
    impuestos = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Impuestos (IVA)"
    )
    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="Total"
    )

    # Pago
    metodo_pago = models.CharField(
        max_length=20,
        choices=METODO_PAGO_CHOICES,
        default='EFECTIVO',
        verbose_name="Método de pago"
    )
    pagado = models.BooleanField(default=False, verbose_name="Pagado")
    fecha_pago = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de pago")

    # Entrega (para e-commerce)
    requiere_entrega = models.BooleanField(default=False, verbose_name="Requiere entrega")
    direccion_entrega = models.TextField(blank=True, verbose_name="Dirección de entrega")
    entregado = models.BooleanField(default=False, verbose_name="Entregado")
    fecha_entrega = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de entrega")

    # Notas
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    notas_internas = models.TextField(blank=True, verbose_name="Notas internas")

    # Auditoría
    vendedor = models.CharField(max_length=100, blank=True, verbose_name="Vendedor")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha_venta']
        db_table = 'ventas'
        indexes = [
            models.Index(fields=['numero_venta']),
            models.Index(fields=['cliente', 'fecha_venta']),
            models.Index(fields=['estado']),
        ]

    def __str__(self):
        return f"Venta {self.numero_venta} - {self.cliente.nombre_completo}"

    def save(self, *args, **kwargs):
        if not self.numero_venta:
            # Generar número de venta automático
            ultimo_numero = Venta.objects.count() + 1
            self.numero_venta = f"VEN-{ultimo_numero:06d}"
        super().save(*args, **kwargs)

    def calcular_totales(self):
        """Calcula los totales de la venta"""
        items = self.items.all()
        self.subtotal = sum(item.subtotal for item in items)
        self.total = self.subtotal - self.descuento + self.impuestos
        self.save()


class DetalleVenta(models.Model):
    """
    Detalle de productos en una venta
    """
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Venta"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='ventas_detalle',
        verbose_name="Producto"
    )

    cantidad = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Cantidad"
    )
    precio_unitario = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Precio unitario"
    )
    descuento_item = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Descuento"
    )
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Subtotal"
    )

    # Garantía del producto
    con_garantia = models.BooleanField(default=True, verbose_name="Con garantía")

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"
        db_table = 'ventas_detalle'

    def __str__(self):
        return f"{self.producto.nombre_producto} x{self.cantidad}"

    def save(self, *args, **kwargs):
        # Calcular subtotal
        self.subtotal = (self.precio_unitario * self.cantidad) - self.descuento_item
        super().save(*args, **kwargs)
        # Actualizar totales de la venta
        self.venta.calcular_totales()

