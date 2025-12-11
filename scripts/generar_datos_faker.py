"""
Script para generar datos falsos (faker) para todos los módulos
Uso: python manage.py shell < scripts/generar_datos_faker.py
O: python scripts/generar_datos_faker.py (si se ejecuta como standalone)
"""

import os
import sys
import django

# Configurar Django si se ejecuta como standalone
if __name__ == '__main__':
    # Agregar el directorio raíz al path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()

from faker import Faker
from decimal import Decimal
import random
from datetime import datetime, timedelta

# Importar modelos
from productos.models import Producto, CategoriaProducto
from clientes.models import Cliente
from proveedores.models import Proveedor
from tecnicos.models import Tecnico
from equipos.models import Equipo
from garantias.models import Garantia
from ordenes.models import OrdenServicio
from ventas.models import Venta, DetalleVenta
from compras.models import Compra, DetalleCompra
from capacitaciones.models import Capacitacion

# Inicializar Faker en español
fake = Faker('es_ES')

print("=" * 60)
print("🚀 GENERADOR DE DATOS FALSOS - DIGITSOFT")
print("=" * 60)
print()


def generar_categorias_productos(cantidad=10):
    """Generar categorías de productos"""
    print(f"📦 Generando {cantidad} categorías de productos...")

    categorias_nombres = [
        'Laptops', 'Computadoras de Escritorio', 'Monitores', 'Teclados',
        'Mouse', 'Impresoras', 'Escáneres', 'Proyectores', 'Accesorios',
        'Componentes', 'Redes', 'Almacenamiento', 'Audio', 'Video',
        'Software', 'Periféricos', 'Cables', 'Adaptadores', 'Cargadores',
        'Baterías'
    ]

    creadas = 0
    for nombre in categorias_nombres[:cantidad]:
        if not CategoriaProducto.objects.filter(nombre=nombre).exists():
            CategoriaProducto.objects.create(
                nombre=nombre,
                descripcion=fake.text(max_nb_chars=100),
                activo=True
            )
            creadas += 1

    print(f"   ✅ {creadas} categorías creadas")
    return CategoriaProducto.objects.all()


def generar_productos(cantidad=50):
    """Generar productos falsos"""
    print(f"📦 Generando {cantidad} productos...")

    categorias = list(CategoriaProducto.objects.all())
    if not categorias:
        categorias = generar_categorias_productos()

    marcas = ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Samsung', 'LG', 'Apple', 'Microsoft', 'Logitech']

    creados = 0
    for i in range(cantidad):
        try:
            codigo_sku = f"PROD-{fake.unique.random_number(digits=6)}"
            if Producto.objects.filter(codigo_sku=codigo_sku).exists():
                continue

            Producto.objects.create(
                codigo_sku=codigo_sku,
                nombre_producto=f"{random.choice(marcas)} {fake.word().title()} {fake.random_number(digits=3)}",
                categoria=random.choice(categorias),
                descripcion=fake.text(max_nb_chars=200),
                marca=random.choice(marcas),
                modelo_equipo=f"MODEL-{fake.random_number(digits=4)}",
                precio_compra=Decimal(str(random.uniform(50, 500))),
                precio_venta=Decimal(str(random.uniform(100, 1000))),
                precio_mayorista=Decimal(str(random.uniform(80, 800))),
                stock_actual=random.randint(0, 100),
                stock_minimo=random.randint(5, 20),
                procesador=random.choice(['Intel i5', 'Intel i7', 'AMD Ryzen 5', 'AMD Ryzen 7', 'N/A']),
                memoria_ram=random.choice(['4GB', '8GB', '16GB', '32GB', 'N/A']),
                memoria_rom=random.choice(['256GB SSD', '512GB SSD', '1TB HDD', '1TB SSD', 'N/A']),
                activo=True,
                disponible_web=random.choice([True, True, True, False]),
                destacado=random.choice([True, False, False, False]),
            )
            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear producto: {e}")

    print(f"   ✅ {creados} productos creados")


def generar_clientes(cantidad=30):
    """Generar clientes falsos"""
    print(f"👥 Generando {cantidad} clientes...")

    creados = 0
    for i in range(cantidad):
        try:
            Cliente.objects.create(
                nombres=fake.first_name(),
                apellidos=fake.last_name(),
                numero_documento=fake.unique.random_number(digits=8),
                telefono=fake.phone_number(),
                correo=fake.unique.email(),
                direccion=fake.address(),
                activo=random.choice([True, True, True, False])
            )
            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear cliente: {e}")

    print(f"   ✅ {creados} clientes creados")


def generar_proveedores(cantidad=20):
    """Generar proveedores falsos"""
    print(f"🏢 Generando {cantidad} proveedores...")

    creados = 0
    for i in range(cantidad):
        try:
            Proveedor.objects.create(
                nombre_empresa=fake.company(),
                ruc=fake.unique.random_number(digits=11),
                contacto_nombre=fake.name(),
                contacto_telefono=fake.phone_number(),
                contacto_email=fake.company_email(),
                direccion=fake.address(),
                ciudad=fake.city(),
                pais='Perú',
                tipo_proveedor=random.choice(['EQUIPOS', 'REPUESTOS', 'SOFTWARE', 'SERVICIOS']),
                activo=True
            )
            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear proveedor: {e}")

    print(f"   ✅ {creados} proveedores creados")


def generar_tecnicos(cantidad=15):
    """Generar técnicos falsos"""
    print(f"🔧 Generando {cantidad} técnicos...")

    especialidades = ['HARDWARE', 'SOFTWARE', 'REDES', 'GENERAL']

    creados = 0
    for i in range(cantidad):
        try:
            Tecnico.objects.create(
                nombres=fake.first_name(),
                apellidos=fake.last_name(),
                numero_documento=fake.unique.random_number(digits=8),
                telefono=fake.phone_number(),
                email=fake.unique.email(),
                especialidad=random.choice(especialidades),
                nivel_experiencia=random.choice(['JUNIOR', 'SEMI_SENIOR', 'SENIOR']),
                activo=True
            )
            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear técnico: {e}")

    print(f"   ✅ {creados} técnicos creados")


def generar_equipos(cantidad=40):
    """Generar equipos falsos"""
    print(f"💻 Generando {cantidad} equipos...")

    clientes = list(Cliente.objects.all())
    if not clientes:
        print("   ⚠️ No hay clientes. Generando clientes primero...")
        generar_clientes(20)
        clientes = list(Cliente.objects.all())

    tipos = ['LAPTOP', 'DESKTOP', 'IMPRESORA', 'SERVIDOR', 'TABLET', 'OTRO']
    marcas = ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer']

    creados = 0
    for i in range(cantidad):
        try:
            Equipo.objects.create(
                cliente=random.choice(clientes),
                tipo_equipo=random.choice(tipos),
                marca=random.choice(marcas),
                modelo=f"MODEL-{fake.random_number(digits=4)}",
                numero_serie=fake.unique.bothify(text='SN-########'),
                procesador=random.choice(['Intel i5', 'Intel i7', 'AMD Ryzen 5']),
                memoria_ram=random.choice(['4GB', '8GB', '16GB', '32GB']),
                almacenamiento=random.choice(['256GB SSD', '512GB SSD', '1TB HDD']),
                sistema_operativo=random.choice(['Windows 10', 'Windows 11', 'Ubuntu', 'macOS']),
                estado=random.choice(['OPERATIVO', 'EN_REPARACION', 'INOPERATIVO']),
                observaciones=fake.text(max_nb_chars=100)
            )
            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear equipo: {e}")

    print(f"   ✅ {creados} equipos creados")


def generar_garantias(cantidad=25):
    """Generar garantías falsas"""
    print(f"📋 Generando {cantidad} garantías...")

    productos = list(Producto.objects.all()[:20])
    clientes = list(Cliente.objects.all()[:20])

    if not productos or not clientes:
        print("   ⚠️ Necesitas productos y clientes primero")
        return

    creados = 0
    for i in range(cantidad):
        try:
            fecha_compra = fake.date_between(start_date='-2y', end_date='today')
            meses_garantia = random.choice([6, 12, 24, 36])
            fecha_vencimiento = fecha_compra + timedelta(days=meses_garantia * 30)

            Garantia.objects.create(
                producto=random.choice(productos),
                cliente=random.choice(clientes),
                numero_serie=fake.unique.bothify(text='GAR-########'),
                fecha_compra=fecha_compra,
                fecha_vencimiento=fecha_vencimiento,
                estado=random.choice(['ACTIVA', 'VENCIDA', 'UTILIZADA']),
                descripcion=fake.text(max_nb_chars=150),
                terminos=fake.text(max_nb_chars=200)
            )
            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear garantía: {e}")

    print(f"   ✅ {creados} garantías creadas")


def generar_ordenes_servicio(cantidad=30):
    """Generar órdenes de servicio falsas"""
    print(f"📝 Generando {cantidad} órdenes de servicio...")

    clientes = list(Cliente.objects.all()[:20])
    equipos = list(Equipo.objects.all()[:20])
    tecnicos = list(Tecnico.objects.all()[:10])

    if not clientes or not equipos or not tecnicos:
        print("   ⚠️ Necesitas clientes, equipos y técnicos primero")
        return

    tipos = ['REPARACION', 'MANTENIMIENTO', 'INSTALACION', 'DIAGNOSTICO']
    prioridades = ['BAJA', 'MEDIA', 'ALTA', 'URGENTE']
    estados = ['PENDIENTE', 'EN_PROCESO', 'COMPLETADA', 'CANCELADA']

    creados = 0
    for i in range(cantidad):
        try:
            OrdenServicio.objects.create(
                numero_orden=f"OS-{fake.unique.random_number(digits=6)}",
                cliente=random.choice(clientes),
                equipo=random.choice(equipos),
                tecnico_asignado=random.choice(tecnicos),
                tipo_servicio=random.choice(tipos),
                prioridad=random.choice(prioridades),
                estado=random.choice(estados),
                descripcion_problema=fake.text(max_nb_chars=200),
                diagnostico=fake.text(max_nb_chars=150) if random.choice([True, False]) else '',
                solucion=fake.text(max_nb_chars=150) if random.choice([True, False]) else '',
                costo_servicio=Decimal(str(random.uniform(50, 500))),
                costo_repuestos=Decimal(str(random.uniform(0, 300))),
                fecha_ingreso=fake.date_time_between(start_date='-60d', end_date='now'),
            )
            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear orden de servicio: {e}")

    print(f"   ✅ {creados} órdenes creadas")


def generar_ventas(cantidad=40):
    """Generar ventas falsas"""
    print(f"💰 Generando {cantidad} ventas...")

    clientes = list(Cliente.objects.all()[:20])
    productos = list(Producto.objects.all()[:30])

    if not clientes or not productos:
        print("   ⚠️ Necesitas clientes y productos primero")
        return

    estados = ['COMPLETADA', 'PENDIENTE', 'CANCELADA']
    metodos_pago = ['EFECTIVO', 'TARJETA', 'TRANSFERENCIA']

    creados = 0
    for i in range(cantidad):
        try:
            # Crear venta
            subtotal = Decimal('0')
            cliente = random.choice(clientes)

            venta = Venta.objects.create(
                numero_venta=f"VEN-{fake.unique.random_number(digits=6)}",
                cliente=cliente,
                estado=random.choice(estados),
                canal_venta=random.choice(['TIENDA', 'WEB', 'TELEFONO']),
                metodo_pago=random.choice(metodos_pago),
                fecha_venta=fake.date_time_between(start_date='-90d', end_date='now'),
            )

            # Agregar detalles (2-5 productos)
            num_productos = random.randint(2, 5)
            productos_seleccionados = random.sample(productos, min(num_productos, len(productos)))

            for producto in productos_seleccionados:
                cantidad = random.randint(1, 3)
                precio = producto.precio_venta
                subtotal_item = precio * cantidad
                subtotal += subtotal_item

                DetalleVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=precio,
                    subtotal=subtotal_item
                )

            # Actualizar totales de la venta
            impuestos = subtotal * Decimal('0.19')
            venta.subtotal = subtotal
            venta.impuestos = impuestos
            venta.total = subtotal + impuestos
            venta.save()

            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear venta: {e}")

    print(f"   ✅ {creados} ventas creadas")


def generar_compras(cantidad=30):
    """Generar compras falsas"""
    print(f"🛒 Generando {cantidad} compras...")

    proveedores = list(Proveedor.objects.all()[:15])
    productos = list(Producto.objects.all()[:30])

    if not proveedores or not productos:
        print("   ⚠️ Necesitas proveedores y productos primero")
        return

    estados = ['COMPLETADA', 'PENDIENTE', 'CANCELADA']

    creados = 0
    for i in range(cantidad):
        try:
            # Crear compra
            subtotal = Decimal('0')
            proveedor = random.choice(proveedores)

            compra = Compra.objects.create(
                numero_compra=f"COMP-{fake.unique.random_number(digits=6)}",
                proveedor=proveedor,
                estado=random.choice(estados),
                fecha_compra=fake.date_time_between(start_date='-120d', end_date='now'),
                observaciones=fake.text(max_nb_chars=100)
            )

            # Agregar detalles (2-6 productos)
            num_productos = random.randint(2, 6)
            productos_seleccionados = random.sample(productos, min(num_productos, len(productos)))

            for producto in productos_seleccionados:
                cantidad = random.randint(5, 50)
                precio = producto.precio_compra or Decimal('50')
                subtotal_item = precio * cantidad
                subtotal += subtotal_item

                DetalleCompra.objects.create(
                    compra=compra,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=precio,
                    subtotal=subtotal_item
                )

            # Actualizar totales
            impuestos = subtotal * Decimal('0.19')
            compra.subtotal = subtotal
            compra.impuestos = impuestos
            compra.total = subtotal + impuestos
            compra.save()

            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear compra: {e}")

    print(f"   ✅ {creados} compras creadas")


def generar_capacitaciones(cantidad=20):
    """Generar capacitaciones falsas"""
    print(f"📚 Generando {cantidad} capacitaciones...")

    tecnicos = list(Tecnico.objects.all()[:10])

    if not tecnicos:
        print("   ⚠️ No hay técnicos. Generando técnicos primero...")
        generar_tecnicos(10)
        tecnicos = list(Tecnico.objects.all())

    temas = [
        'Reparación de Hardware', 'Instalación de Software', 'Redes y Conectividad',
        'Seguridad Informática', 'Mantenimiento Preventivo', 'Soporte Técnico',
        'Diagnóstico de Fallas', 'Gestión de Servidores', 'Cloud Computing'
    ]

    creados = 0
    for i in range(cantidad):
        try:
            fecha_inicio = fake.date_time_between(start_date='-180d', end_date='+60d')
            duracion_horas = random.choice([4, 8, 16, 24, 40])

            capacitacion = Capacitacion.objects.create(
                titulo=random.choice(temas),
                descripcion=fake.text(max_nb_chars=200),
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_inicio + timedelta(hours=duracion_horas),
                duracion_horas=duracion_horas,
                instructor=fake.name(),
                lugar=fake.city(),
                costo=Decimal(str(random.uniform(100, 1000))),
                cupo_maximo=random.randint(10, 30),
                estado=random.choice(['PROGRAMADA', 'EN_CURSO', 'COMPLETADA', 'CANCELADA'])
            )

            # Inscribir algunos técnicos aleatoriamente
            num_inscritos = random.randint(1, min(5, len(tecnicos)))
            tecnicos_inscritos = random.sample(tecnicos, num_inscritos)
            capacitacion.participantes.set(tecnicos_inscritos)

            creados += 1
        except Exception as e:
            print(f"   ⚠️ Error al crear capacitación: {e}")

    print(f"   ✅ {creados} capacitaciones creadas")


def generar_todos_los_datos():
    """Generar datos para todos los módulos"""
    print()
    print("🚀 Iniciando generación masiva de datos...")
    print()

    # Orden de generación (respetando dependencias)
    generar_categorias_productos(15)
    generar_productos(80)
    generar_clientes(50)
    generar_proveedores(25)
    generar_tecnicos(20)
    generar_equipos(60)
    generar_garantias(35)
    generar_ordenes_servicio(45)
    generar_ventas(60)
    generar_compras(40)
    generar_capacitaciones(25)

    print()
    print("=" * 60)
    print("✅ GENERACIÓN COMPLETADA")
    print("=" * 60)
    print()
    print("📊 Resumen:")
    print(f"   • Categorías: {CategoriaProducto.objects.count()}")
    print(f"   • Productos: {Producto.objects.count()}")
    print(f"   • Clientes: {Cliente.objects.count()}")
    print(f"   • Proveedores: {Proveedor.objects.count()}")
    print(f"   • Técnicos: {Tecnico.objects.count()}")
    print(f"   • Equipos: {Equipo.objects.count()}")
    print(f"   • Garantías: {Garantia.objects.count()}")
    print(f"   • Órdenes Servicio: {OrdenServicio.objects.count()}")
    print(f"   • Ventas: {Venta.objects.count()}")
    print(f"   • Compras: {Compra.objects.count()}")
    print(f"   • Capacitaciones: {Capacitacion.objects.count()}")
    print()


if __name__ == '__main__':
    generar_todos_los_datos()

