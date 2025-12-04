"""
DIGIT SOFT - Módulo de Facturación
Models - Gestión de Facturas Electrónicas
"""

from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from clientes.models import Cliente
from ventas.models import Venta


class Factura(models.Model):
    """Modelo de Factura Electrónica"""

    TIPO_FACTURA = [
        ('VENTA', 'Factura de Venta'),
        ('SERVICIO', 'Factura de Servicio'),
        ('MIXTA', 'Factura Mixta'),
    ]

    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('EMITIDA', 'Emitida'),
        ('PAGADA', 'Pagada'),
        ('VENCIDA', 'Vencida'),
        ('ANULADA', 'Anulada'),
    ]

    numero_factura = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        verbose_name="Número de factura",
        help_text="Generado automáticamente"
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='facturas', verbose_name="Cliente")
    venta = models.OneToOneField(Venta, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Venta relacionada")

    tipo_factura = models.CharField(max_length=10, choices=TIPO_FACTURA, default='VENTA', verbose_name="Tipo")
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='BORRADOR', verbose_name="Estado")

    fecha_emision = models.DateField(auto_now_add=True, verbose_name="Fecha de emisión")
    fecha_vencimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de vencimiento")
    fecha_pago = models.DateField(null=True, blank=True, verbose_name="Fecha de pago")

    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Subtotal")
    iva = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="IVA")
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Total")

    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['-fecha_emision']
        db_table = 'facturas'

    def __str__(self):
        return f"Factura {self.numero_factura} - {self.cliente.nombre_completo}"

    def save(self, *args, **kwargs):
        if not self.numero_factura:
            ultimo = Factura.objects.count() + 1
            self.numero_factura = f"FAC-{ultimo:06d}"
        super().save(*args, **kwargs)

