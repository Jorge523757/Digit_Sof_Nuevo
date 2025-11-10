"""
DIGT SOFT - Módulo de Productos
Sistema de Gestión de Productos con E-commerce e Inventario
"""

from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class CategoriaProducto(models.Model):
    """Categorías de productos para organización"""
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de categoría")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Modelo principal de Productos - E-commerce e Inventario"""

    # Información básica del producto
    nombre_producto = models.CharField(max_length=200, verbose_name="Nombre del producto")
    codigo_sku = models.CharField(max_length=50, unique=True, verbose_name="Código SKU")
    categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.SET_NULL,
        null=True,
        related_name='productos',
        verbose_name="Categoría"
    )

    # Especificaciones técnicas (para equipos)
    modelo_equipo = models.CharField(max_length=100, blank=True, verbose_name="Modelo del equipo")
    marca = models.CharField(max_length=100, blank=True, verbose_name="Marca")
    procesador = models.CharField(max_length=100, blank=True, verbose_name="Procesador")
    memoria_ram = models.CharField(max_length=50, blank=True, verbose_name="Memoria RAM")
    memoria_rom = models.CharField(max_length=50, blank=True, verbose_name="Memoria ROM/Almacenamiento")

    # Descripción y detalles
    descripcion = models.TextField(verbose_name="Descripción del producto")
    especificaciones = models.TextField(blank=True, verbose_name="Especificaciones técnicas")

    # Precios
    precio_compra = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio de compra"
    )
    precio_venta = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio de venta"
    )
    precio_mayorista = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio mayorista"
    )

    # Inventario
    stock_actual = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Stock actual"
    )
    stock_minimo = models.IntegerField(
        default=5,
        validators=[MinValueValidator(0)],
        verbose_name="Stock mínimo"
    )
    stock_maximo = models.IntegerField(
        default=100,
        validators=[MinValueValidator(0)],
        verbose_name="Stock máximo"
    )

    # E-commerce
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen del producto")
    disponible_web = models.BooleanField(default=True, verbose_name="Disponible en web")
    destacado = models.BooleanField(default=False, verbose_name="Producto destacado")

    # Control y seguimiento
    activo = models.BooleanField(default=True, verbose_name="Activo")
    tiene_garantia = models.BooleanField(default=True, verbose_name="Tiene garantía")
    meses_garantia = models.IntegerField(default=12, verbose_name="Meses de garantía")

    # Auditoría
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_registro']
        indexes = [
            models.Index(fields=['codigo_sku']),
            models.Index(fields=['nombre_producto']),
        ]

    def __str__(self):
        return f"{self.codigo_sku} - {self.nombre_producto}"

    @property
    def margen_utilidad(self):
        """Calcula el margen de utilidad en porcentaje"""
        if self.precio_compra > 0:
            return ((self.precio_venta - self.precio_compra) / self.precio_compra) * 100
        return 0

    @property
    def necesita_reposicion(self):
        """Verifica si el stock está por debajo del mínimo"""
        return self.stock_actual <= self.stock_minimo

    @property
    def stock_disponible(self):
        """Retorna si hay stock disponible"""
        return self.stock_actual > 0

    @property
    def valor_inventario(self):
        """Calcula el valor total del inventario de este producto"""
        return self.stock_actual * self.precio_compra


class MovimientoInventario(models.Model):
    """Registro de movimientos de inventario"""

    TIPO_MOVIMIENTO = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
        ('AJUSTE', 'Ajuste'),
        ('DEVOLUCION', 'Devolución'),
    ]

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='movimientos',
        verbose_name="Producto"
    )
    tipo_movimiento = models.CharField(max_length=20, choices=TIPO_MOVIMIENTO, verbose_name="Tipo de movimiento")
    cantidad = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Cantidad")
    stock_anterior = models.IntegerField(verbose_name="Stock anterior")
    stock_nuevo = models.IntegerField(verbose_name="Stock nuevo")
    motivo = models.CharField(max_length=200, verbose_name="Motivo")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    # Auditoría
    fecha_movimiento = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del movimiento")
    usuario = models.CharField(max_length=100, blank=True, verbose_name="Usuario")

    class Meta:
        verbose_name = "Movimiento de Inventario"
        verbose_name_plural = "Movimientos de Inventario"
        ordering = ['-fecha_movimiento']

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.producto.nombre_producto} ({self.cantidad})"

