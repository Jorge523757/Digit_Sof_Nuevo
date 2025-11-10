"""
DIGT SOFT - Módulo de Garantías
Sistema de Gestión de Garantías de Productos
"""

from django.db import models
from django.core.validators import EmailValidator
from clientes.models import Cliente
from productos.models import Producto


class Garantia(models.Model):
    """Modelo de Garantía de Productos"""

    ESTADO_GARANTIA = [
        ('ACTIVA', 'Activa'),
        ('VENCIDA', 'Vencida'),
        ('EN_REVISION', 'En revisión'),
        ('APROBADA', 'Aprobada'),
        ('RECHAZADA', 'Rechazada'),
        ('FINALIZADA', 'Finalizada'),
    ]

    # Información del comprador
    nombre_comprador = models.CharField(max_length=200, verbose_name="Nombre del comprador")
    cedula = models.CharField(max_length=20, verbose_name="Cédula")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    correo_electronico = models.EmailField(
        validators=[EmailValidator()],
        verbose_name="Correo electrónico"
    )

    # Producto con garantía
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='garantias',
        verbose_name="Producto"
    )
    nombre_producto = models.CharField(max_length=200, verbose_name="Nombre del producto")
    numero_serie = models.CharField(max_length=100, blank=True, verbose_name="Número de serie")
    modelo = models.CharField(max_length=100, blank=True, verbose_name="Modelo")

    # Información de compra
    fecha_compra = models.DateField(verbose_name="Fecha de compra")
    factura_compra = models.CharField(max_length=50, blank=True, verbose_name="Número de factura")
    lugar_compra = models.CharField(max_length=200, verbose_name="Lugar de compra")

    # Detalles de la garantía
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio de garantía")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de vencimiento")
    meses_garantia = models.IntegerField(default=12, verbose_name="Meses de garantía")

    # Estado y seguimiento
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_GARANTIA,
        default='ACTIVA',
        verbose_name="Estado"
    )
    motivo_reclamacion = models.TextField(blank=True, verbose_name="Motivo de reclamación")
    descripcion_problema = models.TextField(blank=True, verbose_name="Descripción del problema")

    # Resolución
    solucion = models.TextField(blank=True, verbose_name="Solución aplicada")
    fecha_resolucion = models.DateField(null=True, blank=True, verbose_name="Fecha de resolución")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    # Relación con cliente (opcional)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='garantias',
        verbose_name="Cliente"
    )

    # Auditoría
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Garantía"
        verbose_name_plural = "Garantías"
        ordering = ['-fecha_registro']
        indexes = [
            models.Index(fields=['cedula']),
            models.Index(fields=['factura_compra']),
            models.Index(fields=['estado']),
        ]

    def __str__(self):
        return f"Garantía {self.id} - {self.nombre_producto} ({self.nombre_comprador})"

    @property
    def dias_restantes(self):
        """Calcula los días restantes de garantía"""
        from datetime import date
        if self.fecha_vencimiento:
            dias = (self.fecha_vencimiento - date.today()).days
            return max(0, dias)
        return 0

    @property
    def esta_vigente(self):
        """Verifica si la garantía está vigente"""
        from datetime import date
        return self.fecha_vencimiento >= date.today() and self.estado == 'ACTIVA'

    @property
    def porcentaje_usado(self):
        """Calcula el porcentaje de tiempo usado de la garantía"""
        from datetime import date
        if self.fecha_inicio and self.fecha_vencimiento:
            dias_totales = (self.fecha_vencimiento - self.fecha_inicio).days
            dias_usados = (date.today() - self.fecha_inicio).days
            if dias_totales > 0:
                porcentaje = (dias_usados / dias_totales) * 100
                return min(100, max(0, porcentaje))
        return 0


class SeguimientoGarantia(models.Model):
    """Seguimiento detallado de las garantías"""

    garantia = models.ForeignKey(
        Garantia,
        on_delete=models.CASCADE,
        related_name='seguimientos',
        verbose_name="Garantía"
    )
    fecha_seguimiento = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de seguimiento")
    estado_anterior = models.CharField(max_length=20, verbose_name="Estado anterior")
    estado_nuevo = models.CharField(max_length=20, verbose_name="Estado nuevo")
    comentarios = models.TextField(verbose_name="Comentarios")
    usuario = models.CharField(max_length=100, blank=True, verbose_name="Usuario")

    class Meta:
        verbose_name = "Seguimiento de Garantía"
        verbose_name_plural = "Seguimientos de Garantías"
        ordering = ['-fecha_seguimiento']

    def __str__(self):
        return f"Seguimiento {self.garantia.id} - {self.fecha_seguimiento.strftime('%d/%m/%Y')}"

