from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200, blank=True)
    contrasena = models.CharField(max_length=100, default='123456')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, default='Sin nombre')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.CharField(max_length=50)
    marca = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.precio < 0:
            raise ValidationError('El precio no puede ser negativo')
        if self.stock < 0:
            raise ValidationError('El stock no puede ser negativo')

    def descontar_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError('No hay suficiente stock')
        self.stock -= cantidad
        self.save()

class ComentarioProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.nombre} en {self.producto.nombre}"

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=30, choices=[('Efectivo','Efectivo'),('Tarjeta','Tarjeta'),('Transferencia','Transferencia')])
    total = models.DecimalField(max_digits=12, decimal_places=2)
    nit_empresa = models.CharField(max_length=20, default='901234567-8')  # NIT de DigitSoft

    def __str__(self):
        return f"Venta {self.pk} - {self.cliente.nombre}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
        ('facturado', 'Facturado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='pendiente')
    total = models.DecimalField(max_digits=12, decimal_places=2)
    notas_cliente = models.TextField(blank=True, null=True, help_text="Notas adicionales del cliente")
    procesado_por = models.CharField(max_length=100, blank=True, null=True, help_text="Administrador que procesa el pedido")
    fecha_procesamiento = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ['-fecha_pedido']
    
    def __str__(self):
        return f"Pedido {self.pk} - {self.cliente.nombre} ({self.estado})"
    
    def puede_ser_facturado(self):
        return self.estado in ['pendiente', 'procesando']

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    
    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Pedido {self.pedido.pk} - {self.producto.nombre} x{self.cantidad}"