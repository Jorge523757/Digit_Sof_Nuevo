"""
DIGT SOFT - Módulo de Compras
Models - Gestión de Compras a Proveedores
"""

from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from decimal import Decimal
from proveedores.models import Proveedor
from productos.models import Producto


class Compra(models.Model):
    """
    Modelo principal de Compras a Proveedores
    """

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('APROBADA', 'Aprobada'),
        ('RECIBIDA', 'Recibida'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    METODO_PAGO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('CHEQUE', 'Cheque'),
        ('CREDITO', 'Crédito'),
    ]

    # Información básica
    numero_compra = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Número de compra"
    )
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        related_name='compras',
        verbose_name="Proveedor"
    )

    # Usuario que realiza la compra
    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='compras_realizadas',
        verbose_name="Usuario",
        null=True,
        blank=True
    )

    # Detalles
    fecha_compra = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de compra")
    fecha_entrega_esperada = models.DateField(null=True, blank=True, verbose_name="Fecha de entrega esperada")
    fecha_entrega_real = models.DateField(null=True, blank=True, verbose_name="Fecha de entrega real")

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='PENDIENTE',
        verbose_name="Estado"
    )

    # Montos
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="Subtotal"
    )
    impuestos = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Impuestos"
    )
    descuento = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Descuento"
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
        default='TRANSFERENCIA',
        verbose_name="Método de pago"
    )
    pagado = models.BooleanField(default=False, verbose_name="Pagado")
    fecha_pago = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de pago")

    # Notas
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    notas_internas = models.TextField(blank=True, verbose_name="Notas internas")

    # Auditoría
    responsable = models.CharField(max_length=100, blank=True, verbose_name="Responsable")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['-fecha_compra']
        db_table = 'compras'

    def __str__(self):
        return f"Compra {self.numero_compra} - {self.proveedor.nombre_empresa}"

    def save(self, *args, **kwargs):
        if not self.numero_compra:
            ultimo_numero = Compra.objects.count() + 1
            self.numero_compra = f"COM-{ultimo_numero:06d}"
        super().save(*args, **kwargs)

    def calcular_totales(self):
        """Calcula los totales de la compra"""
        items = self.items.all()
        self.subtotal = sum(item.subtotal for item in items)
        self.total = self.subtotal + self.impuestos - self.descuento
        self.save()


class DetalleCompra(models.Model):
    """
    Detalle de productos en una compra
    """
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Compra"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='compras_detalle',
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
    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Subtotal"
    )

    recibido = models.BooleanField(default=False, verbose_name="Recibido")
    fecha_recepcion = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de recepción")

    class Meta:
        verbose_name = "Detalle de Compra"
        verbose_name_plural = "Detalles de Compra"
        db_table = 'compras_detalle'

    def __str__(self):
        return f"{self.producto.nombre_producto} x{self.cantidad}"

    def save(self, *args, **kwargs):
        self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)
        self.compra.calcular_totales()

        # Si está recibido, actualizar el inventario
        if self.recibido and not self._state.adding:
            self.producto.stock_actual += self.cantidad
            self.producto.save()
