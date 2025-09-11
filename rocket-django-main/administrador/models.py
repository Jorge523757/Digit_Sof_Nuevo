from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=70)
    numero_documento = models.CharField(max_length=15)
    numero_telefonico = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    color = models.CharField(max_length=25)
    marca = models.CharField(max_length=35)
    descripcion = models.CharField(max_length=80)

    def __str__(self):
        return self.marca


class Proveedor(models.Model):
    nit_proveedor = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Administrador(models.Model):
    nombre = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=42)
    correo_electronico = models.EmailField(max_length=40)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=35)
    modelo_producto = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    valor_producto = models.CharField(max_length=45)
    diseno = models.CharField(max_length=40)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto


class Equipo(models.Model):
    modelo = models.CharField(max_length=35)
    clave = models.CharField(max_length=35)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} - {self.clave}"


class Tecnico(models.Model):
    nombre_completo = models.CharField(max_length=50)
    n_documento = models.IntegerField()
    n_tel = models.IntegerField()
    correo = models.CharField(max_length=60)
    direccion = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    tipo_tecnico = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_completo


class OrdenServicio(models.Model):
    id_ordenServicio = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    tecnico = models.ForeignKey('Tecnico', on_delete=models.CASCADE)
    descripcion_orden = models.CharField(max_length=50)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En proceso'),
            ('finalizado', 'Finalizado')
        ]
    )

    def __str__(self):
        return f"Orden {self.id_ordenServicio} - {self.estado}"



class ServicioTecnico(models.Model):
    id = models.AutoField(primary_key=True)  # Campo explícito
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    equipo = models.CharField(max_length=100)
    descripcion_falla = models.TextField()
    fecha_ingreso = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Servicio {self.id} - {self.cliente}"



class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True , blank=True)
    fecha_venta = models.DateField()
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id_venta} - {self.cliente}"



class ComprasMercancia(models.Model):
    id = models.AutoField(primary_key=True)  # ID explícito
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad_compras = models.IntegerField()
    fecha_compra = models.DateField()
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE)
    precio_compra = models.CharField(max_length=50)

    def __str__(self):
        return f"Compra {self.id} - {self.producto}"



class Facturacion(models.Model):
    id_recibo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE,null=True, blank=True)
    descripcion_venta = models.CharField(max_length=50,null=True, blank=True)
    terminos_y_condiciones = models.CharField(max_length=250)
    nit_digisoft = models.CharField(max_length=50)
    administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE,null=True, blank=True)
    orden_servicio = models.ForeignKey('OrdenServicio', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"Factura {self.id_recibo}"



class Garantias(models.Model):
    id = models.AutoField(primary_key=True)
    facturacion = models.ForeignKey('Facturacion', on_delete=models.CASCADE)

    def __str__(self):
        return f"Garantía {self.id}"



