"""
Script MEJORADO para generar datos falsos adaptado a los modelos REALES
Ejecutar: python scripts/generar_datos_faker_mejorado.py
"""

import os
import sys
import django

# Configurar Django
if __name__ == '__main__':
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
print("GENERADOR DE DATOS FALSOS MEJORADO - DIGITSOFT")
print("=" * 60)
print()


def generar_proveedores(cantidad=25):
    """Generar proveedores con campos correctos"""
    print(f"Generando {cantidad} proveedores...")

    creados = 0
    for i in range(cantidad):
        try:
            Proveedor.objects.create(
                nombre_empresa=fake.company(),
                nit=f"{fake.random_number(digits=9)}-{fake.random_number(digits=1)}",
                nombre_contacto=fake.name(),
                telefono=fake.phone_number()[:15],
                email=fake.company_email(),
                direccion=fake.address()[:255],
                ciudad=fake.city(),
                pais='Colombia',
                productos_servicios=fake.text(max_nb_chars=200),
                condiciones_pago=random.choice(['Contado', '30 días', '60 días', '90 días']),
                tiempo_entrega=f"{random.randint(1, 30)} días",
                calificacion=random.randint(1, 5),
                activo=True
            )
            creados += 1
        except Exception as e:
            print(f"   Error: {e}")

    print(f"   {creados} proveedores creados")
    return Proveedor.objects.all()


def generar_tecnicos(cantidad=20):
    """Generar técnicos con campos correctos"""
    print(f"Generando {cantidad} tecnicos...")

    creados = 0
    for i in range(cantidad):
        try:
            Tecnico.objects.create(
                nombres=fake.first_name(),
                apellidos=fake.last_name(),
                numero_documento=fake.unique.random_number(digits=8),
                telefono=fake.phone_number()[:15],
                correo=fake.unique.email(),
                direccion=fake.address()[:255],
                especialidad=fake.job()[:100],
                activo=True
            )
            creados += 1
        except Exception as e:
            print(f"   Error: {e}")

    print(f"   {creados} tecnicos creados")
    return Tecnico.objects.all()


def generar_equipos(cantidad=40):
    """Generar equipos con campos correctos"""
    print(f"Generando {cantidad} equipos...")

    clientes = list(Cliente.objects.all())
    if not clientes:
        print("   No hay clientes. Saltando...")
        return []

    marcas = ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer']

    creados = 0
    for i in range(cantidad):
        try:
            cliente = random.choice(clientes)
            Equipo.objects.create(
                cliente=cliente,
                tipo_equipo=random.choice(['Laptop', 'Desktop', 'Impresora', 'Servidor']),
                marca=random.choice(marcas),
                modelo=f"MODEL-{fake.random_number(digits=4)}",
                numero_serie=fake.unique.bothify(text='SN-########'),
                descripcion=fake.text(max_nb_chars=200),
                estado=random.choice(['Bueno', 'Regular', 'Malo']),
                observaciones=fake.text(max_nb_chars=150)
            )
            creados += 1
        except Exception as e:
            print(f"   Error: {e}")

    print(f"   {creados} equipos creados")
    return Equipo.objects.all()


def generar_garantias(cantidad=30):
    """Generar garantías con campos correctos"""
    print(f"Generando {cantidad} garantias...")

    productos = list(Producto.objects.all()[:20])
    clientes = list(Cliente.objects.all()[:20])

    if not productos or not clientes:
        print("   Necesitas productos y clientes. Saltando...")
        return []

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
                condiciones=fake.text(max_nb_chars=200),
                estado=random.choice(['Activa', 'Vencida', 'Utilizada']),
                observaciones=fake.text(max_nb_chars=150)
            )
            creados += 1
        except Exception as e:
            print(f"   Error: {e}")

    print(f"   {creados} garantias creadas")
    return Garantia.objects.all()


def generar_ordenes_servicio(cantidad=35):
    """Generar órdenes de servicio con campos correctos"""
    print(f"Generando {cantidad} ordenes de servicio...")

    clientes = list(Cliente.objects.all()[:20])
    equipos = list(Equipo.objects.all()[:20])
    tecnicos = list(Tecnico.objects.all()[:10])

    if not clientes or not equipos or not tecnicos:
        print("   Necesitas clientes, equipos y tecnicos. Saltando...")
        return []

    creados = 0
    for i in range(cantidad):
        try:
            OrdenServicio.objects.create(
                numero_orden=f"OS-{fake.unique.random_number(digits=6)}",
                cliente=random.choice(clientes),
                equipo=random.choice(equipos),
                tecnico_asignado=random.choice(tecnicos),
                tipo_servicio=random.choice(['Reparacion', 'Mantenimiento', 'Instalacion']),
                descripcion_problema=fake.text(max_nb_chars=200),
                diagnostico=fake.text(max_nb_chars=150) if random.choice([True, False]) else '',
                solucion=fake.text(max_nb_chars=150) if random.choice([True, False]) else '',
                estado=random.choice(['Pendiente', 'En proceso', 'Completada', 'Cancelada']),
                prioridad=random.choice(['Baja', 'Media', 'Alta', 'Urgente']),
                costo_mano_obra=Decimal(str(random.uniform(50, 300))),
                costo_repuestos=Decimal(str(random.uniform(0, 500))),
                fecha_ingreso=fake.date_time_between(start_date='-60d', end_date='now'),
            )
            creados += 1
        except Exception as e:
            print(f"   Error: {e}")

    print(f"   {creados} ordenes creadas")
    return OrdenServicio.objects.all()


def generar_compras(cantidad=30):
    """Generar compras con campos correctos"""
    print(f"Generando {cantidad} compras...")

    proveedores = list(Proveedor.objects.all()[:15])
    productos = list(Producto.objects.all()[:30])

    if not proveedores or not productos:
        print("   Necesitas proveedores y productos. Saltando...")
        return []

    creados = 0
    for i in range(cantidad):
        try:
            subtotal = Decimal('0')
            proveedor = random.choice(proveedores)

            compra = Compra.objects.create(
                numero_compra=f"COMP-{fake.unique.random_number(digits=6)}",
                proveedor=proveedor,
                estado=random.choice(['Completada', 'Pendiente', 'Cancelada']),
                fecha_compra=fake.date_time_between(start_date='-120d', end_date='now'),
                observaciones=fake.text(max_nb_chars=100)
            )

            # Agregar detalles
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
            print(f"   Error: {e}")

    print(f"   {creados} compras creadas")


def generar_capacitaciones(cantidad=20):
    """Generar capacitaciones con campos correctos"""
    print(f"Generando {cantidad} capacitaciones...")

    tecnicos = list(Tecnico.objects.all()[:10])

    if not tecnicos:
        print("   No hay tecnicos. Generando tecnicos primero...")
        generar_tecnicos(10)
        tecnicos = list(Tecnico.objects.all())

    temas = [
        'Reparacion de Hardware', 'Instalacion de Software', 'Redes y Conectividad',
        'Seguridad Informatica', 'Mantenimiento Preventivo', 'Soporte Tecnico',
        'Diagnostico de Fallas', 'Gestion de Servidores', 'Cloud Computing'
    ]

    creados = 0
    for i in range(cantidad):
        try:
            fecha_inicio = fake.date_time_between(start_date='-180d', end_date='+60d')
            duracion_horas = random.choice([4, 8, 16, 24, 40])

            capacitacion = Capacitacion.objects.create(
                nombre=random.choice(temas),
                descripcion=fake.text(max_nb_chars=200),
                instructor=fake.name(),
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_inicio + timedelta(hours=duracion_horas),
                duracion_horas=duracion_horas,
                lugar=fake.city(),
                costo=Decimal(str(random.uniform(100, 1000))),
                cupo_maximo=random.randint(10, 30),
                estado=random.choice(['Programada', 'En curso', 'Completada', 'Cancelada'])
            )

            # Inscribir técnicos
            num_inscritos = random.randint(1, min(5, len(tecnicos)))
            tecnicos_inscritos = random.sample(tecnicos, num_inscritos)
            capacitacion.participantes.set(tecnicos_inscritos)

            creados += 1
        except Exception as e:
            print(f"   Error: {e}")

    print(f"   {creados} capacitaciones creadas")


def generar_todos_los_datos():
    """Generar datos para todos los módulos"""
    print()
    print("Iniciando generacion masiva de datos...")
    print()

    # Orden respetando dependencias
    print("1. PROVEEDORES")
    generar_proveedores(25)
    print()

    print("2. TECNICOS")
    generar_tecnicos(20)
    print()

    print("3. EQUIPOS")
    generar_equipos(40)
    print()

    print("4. GARANTIAS")
    generar_garantias(30)
    print()

    print("5. ORDENES DE SERVICIO")
    generar_ordenes_servicio(35)
    print()

    print("6. COMPRAS")
    generar_compras(30)
    print()

    print("7. CAPACITACIONES")
    generar_capacitaciones(20)
    print()

    print("=" * 60)
    print("GENERACION COMPLETADA")
    print("=" * 60)
    print()
    print("Resumen:")
    print(f"   Proveedores: {Proveedor.objects.count()}")
    print(f"   Tecnicos: {Tecnico.objects.count()}")
    print(f"   Equipos: {Equipo.objects.count()}")
    print(f"   Garantias: {Garantia.objects.count()}")
    print(f"   Ordenes Servicio: {OrdenServicio.objects.count()}")
    print(f"   Compras: {Compra.objects.count()}")
    print(f"   Capacitaciones: {Capacitacion.objects.count()}")
    print()


if __name__ == '__main__':
    generar_todos_los_datos()

