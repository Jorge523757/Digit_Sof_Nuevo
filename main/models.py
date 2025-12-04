from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """Perfil de usuario con roles específicos"""
    
    ROLE_CHOICES = [
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
        ('proveedor', 'Proveedor'),
        ('tecnico', 'Técnico'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cliente')
    
    # Campos comunes
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    # Campos específicos para proveedores
    nit = models.CharField(max_length=15, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    
    # Campos específicos para técnicos
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    tipo_tecnico = models.CharField(max_length=50, blank=True, null=True)
    
    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {dict(self.ROLE_CHOICES).get(self.role, self.role)}"
    
    @property
    def is_cliente(self):
        return self.role == 'cliente'
    
    @property
    def is_administrador(self):
        return self.role == 'administrador'
    
    @property
    def is_proveedor(self):
        return self.role == 'proveedor'
    
    @property
    def is_tecnico(self):
        return self.role == 'tecnico'


# SIGNALS DESHABILITADOS - Se usa el signal de usuarios/models.py (PerfilUsuario)
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     """Crear perfil automáticamente cuando se crea un usuario"""
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     """Guardar el perfil cuando se guarda el usuario"""
#     if hasattr(instance, 'profile'):
#         instance.profile.save()


class Cliente(models.Model):
    """Modelo para gestión de clientes"""
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    numero_documento = models.CharField(max_length=15)
    numero_telefonico = models.CharField(max_length=20)
    correo_electronico = models.CharField(max_length=70)
    direccion = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Proveedor(models.Model):
    """Modelo para gestión de proveedores"""
    nit_proveedor = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.nit_proveedor}"

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"


class Tecnico(models.Model):
    """Modelo para gestión de técnicos"""
    id_tecnico = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=20, unique=True)
    cedula = models.CharField(max_length=20)
    correo = models.EmailField(max_length=60)
    direccion = models.CharField(max_length=60)
    especialidad = models.CharField(max_length=40)
    tipo_tecnico = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre_completo} - {self.especialidad}"

    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"


class Administrador(models.Model):
    """Modelo para administradores del sistema"""
    id_administrador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=42)
    correo_electronico = models.EmailField(max_length=40)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"


class Marca(models.Model):
    """Modelo para marcas de productos"""
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=25)
    marca = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=80)

    def __str__(self):
        return self.marca

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


class Producto(models.Model):
    """Modelo para productos"""
    id_producto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=35)
    modelo_producto = models.CharField(max_length=40)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])
    valor_producto = models.CharField(max_length=45)
    diseño = models.CharField(max_length=40)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombreProducto} - {self.modelo_producto}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class Equipo(models.Model):
    """Modelo para equipos"""
    id_equipo = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=35)
    clave = models.CharField(max_length=35)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} ({self.clave})"

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"


class OrdenServicio(models.Model):
    """Modelo para órdenes de servicio"""
    id_ordenServicio = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    descripcion_orden = models.CharField(max_length=255)
    estado = models.CharField(max_length=30, default='Pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id_ordenServicio} - {self.cliente.nombre}"

    class Meta:
        verbose_name = "Orden de Servicio"
        verbose_name_plural = "Órdenes de Servicio"


class ServicioTecnico(models.Model):
    """Modelo para servicios técnicos"""
    id_servicio_tecnico = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    orden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Servicio #{self.id_servicio_tecnico} - {self.cliente.nombre}"

    class Meta:
        verbose_name = "Servicio Técnico"
        verbose_name_plural = "Servicios Técnicos"


class Ventas(models.Model):
    """Modelo para ventas"""
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_vendidas = models.IntegerField(validators=[MinValueValidator(1)])
    valor_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta #{self.id_venta} - {self.cliente.nombre}"

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"


class ComprasMercancia(models.Model):
    """Modelo para compras de mercancía"""
    id_compra = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_comprada = models.IntegerField(validators=[MinValueValidator(1)])
    fecha_compra = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    precio_compra = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra #{self.id_compra} - {self.producto.nombreProducto}"

    class Meta:
        verbose_name = "Compra de Mercancía"
        verbose_name_plural = "Compras de Mercancía"


class Garantias(models.Model):
    """Modelo para garantías"""
    id_garantias = models.AutoField(primary_key=True)
    facturacion = models.CharField(max_length=100)  # Referencia a facturación

    def __str__(self):
        return f"Garantía #{self.id_garantias}"

    class Meta:
        verbose_name = "Garantía"
        verbose_name_plural = "Garantías"


class Facturacion(models.Model):
    """Modelo para facturación"""
    id_recibo = models.AutoField(primary_key=True)
    fecha_factura = models.DateField()
    ventas = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    descripcion_venta = models.CharField(max_length=50)
    terminos_condiciones = models.CharField(max_length=25)
    metodo_pago = models.CharField(max_length=50)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    orden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura #{self.id_recibo}"

    class Meta:
        verbose_name = "Facturación"
        verbose_name_plural = "Facturaciones"


# =============================================================================
# MODELOS DE PRODUCTOS Y ECOMMERCE
# =============================================================================

class Category(models.Model):
    """Categorías de productos"""
    
    CATEGORY_CHOICES = [
        ('laptops', 'Laptops'),
        ('escritorio', 'Computadoras de Escritorio'),
        ('accesorios', 'Accesorios de Computadoras'),
        ('motos_electricas', 'Motos Eléctricas'),
        ('scooters', 'Scooters Eléctricos'),
    ]
    
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, unique=True)
    display_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['display_name']
    
    def __str__(self):
        return self.display_name

    def get_products_count(self):
        return Product.objects.filter(category=self, is_active=True).count()


class Product(models.Model):
    """Modelo de productos"""
    
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    short_description = models.CharField(max_length=300, blank=True, verbose_name="Descripción Corta")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Categoría")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))], verbose_name="Precio")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Precio Original")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    sku = models.CharField(max_length=100, unique=True, verbose_name="SKU")
    brand = models.CharField(max_length=100, blank=True, verbose_name="Marca")
    model = models.CharField(max_length=100, blank=True, verbose_name="Modelo")
    
    # Especificaciones técnicas
    specifications = models.JSONField(default=dict, blank=True, verbose_name="Especificaciones")
    
    # Imágenes
    main_image = models.ImageField(upload_to='products/', verbose_name="Imagen Principal")
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Imagen 2")
    image_3 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Imagen 3")
    image_4 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Imagen 4")
    
    # SEO y metadatos
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    # Estado y fechas
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    is_featured = models.BooleanField(default=False, verbose_name="Destacado")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Proveedor
    provider = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, 
                                limit_choices_to={'role': 'proveedor'}, verbose_name="Proveedor")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    @property
    def is_on_sale(self):
        return self.original_price and self.original_price > self.price
    
    @property
    def discount_percentage(self):
        if self.is_on_sale and self.original_price:
            return int(((self.original_price - self.price) / self.original_price) * 100)
        return 0
    
    @property
    def is_in_stock(self):
        return self.stock > 0
    
    def get_images(self):
        """Devuelve lista de todas las imágenes del producto"""
        images = [self.main_image]
        for img in [self.image_2, self.image_3, self.image_4]:
            if img:
                images.append(img)
        return images


class Cart(models.Model):
    """Carrito de compras"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"
    
    def __str__(self):
        return f"Carrito de {self.user.username}"
    
    @property
    def total_items(self):
        return sum(item.quantity for item in self.cartitem_set.all())
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.cartitem_set.all())
    
    def get_items(self):
        return self.cartitem_set.all()


class CartItem(models.Model):
    """Items del carrito"""
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Item del Carrito"
        verbose_name_plural = "Items del Carrito"
        unique_together = ('cart', 'product')
    
    def __str__(self):
        return f"{self.quantity} x {self.product.nombre_producto}"

    @property
    def total_price(self):
        return self.product.precio_venta * self.quantity

    @property
    def available_stock(self):
        return self.product.stock_actual

    def can_increase_quantity(self, amount=1):
        """Verifica si se puede aumentar la cantidad"""
        return (self.quantity + amount) <= self.product.stock_actual


class Order(models.Model):
    """Pedidos/Órdenes de compra"""
    
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmado'),
        ('processing', 'Procesando'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregado'),
        ('cancelled', 'Cancelado'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Efectivo'),
        ('card', 'Tarjeta de Crédito/Débito'),
        ('transfer', 'Transferencia Bancaria'),
        ('pse', 'PSE'),
        ('nequi', 'Nequi'),
        ('daviplata', 'Daviplata'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    
    # Información de entrega
    shipping_address = models.TextField()
    shipping_city = models.CharField(max_length=100)
    shipping_phone = models.CharField(max_length=20)
    delivery_date = models.DateField(null=True, blank=True)
    
    # Precios
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Fechas
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Notas
    notes = models.TextField(blank=True, verbose_name="Notas del pedido")
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Pedido #{self.order_number}"
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            import uuid
            self.order_number = f"DS{str(uuid.uuid4().int)[:8]}"
        super().save(*args, **kwargs)
    
    def get_items(self):
        return self.orderitem_set.all()


class OrderItem(models.Model):
    """Items de un pedido"""
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio al momento de la compra
    
    class Meta:
        verbose_name = "Item del Pedido"
        verbose_name_plural = "Items del Pedido"
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    @property
    def total_price(self):
        return self.price * self.quantity


class Invoice(models.Model):
    """Facturas generadas"""
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='invoice')
    invoice_number = models.CharField(max_length=20, unique=True)
    invoice_date = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='invoices/', blank=True, null=True)
    
    # Información fiscal
    tax_id = models.CharField(max_length=20, blank=True)  # NIT o CC del cliente
    business_name = models.CharField(max_length=200, blank=True)  # Razón social si aplica
    
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['-invoice_date']
    
    def __str__(self):
        return f"Factura #{self.invoice_number}"
    
    def save(self, *args, **kwargs):
        if not self.invoice_number:
            import uuid
            self.invoice_number = f"FAC{str(uuid.uuid4().int)[:8]}"
        super().save(*args, **kwargs)
