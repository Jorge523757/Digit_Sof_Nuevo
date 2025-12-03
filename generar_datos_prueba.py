"""
DIGT SOFT - Generador de Datos de Prueba con Faker
Script seguro para poblar la base de datos sin dañar datos existentes
"""
import os
import django
import random
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from clientes.models import Cliente
from productos.models import Producto, CategoriaProducto
from ventas.models import Venta, DetalleVenta

# Inicializar Faker en español
fake = Faker('es_ES')

def confirmar_accion():
    """Pide confirmación antes de generar datos"""
    print("\n" + "="*60)
    print("  GENERADOR DE DATOS DE PRUEBA - DIGIT SOFT")
    print("="*60)
    print("\nEste script generará datos de prueba sin afectar datos existentes.")
    print("\n¿Qué se va a crear?")
    print("  • 20 Clientes")
    print("  • 5 Categorías de Productos")
    print("  • 30 Productos")
    print("  • 15 Ventas con sus detalles")
    print("\n" + "="*60)

    respuesta = input("\n¿Deseas continuar? (si/no): ").strip().lower()
    return respuesta in ['si', 'sí', 's', 'yes', 'y']


def generar_clientes(cantidad=20):
    """Genera clientes de prueba"""
    print(f"\n📋 Generando {cantidad} clientes...")
    clientes_creados = []

    for i in range(cantidad):
        try:
            cliente = Cliente.objects.create(
                nombres=fake.first_name(),
                apellidos=fake.last_name(),
                numero_documento=str(fake.unique.random_number(digits=10, fix_len=True)),
                telefono=fake.phone_number()[:15],
                correo=fake.email(),
                direccion=fake.address(),
                activo=random.choice([True, True, True, False]),  # 75% activos
                observaciones=fake.text(max_nb_chars=100) if random.random() > 0.5 else ""
            )
            clientes_creados.append(cliente)
        except Exception as e:
            print(f"  ⚠️  Error al crear cliente {i+1}: {e}")

    print(f"  ✅ {len(clientes_creados)} clientes creados exitosamente")
    return clientes_creados


def generar_categorias():
    """Genera categorías de productos"""
    print("\n📦 Generando categorías de productos...")

    categorias_data = [
        {
            'nombre': 'Laptops',
            'descripcion': 'Computadoras portátiles de diferentes marcas y especificaciones'
        },
        {
            'nombre': 'Smartphones',
            'descripcion': 'Teléfonos inteligentes y accesorios móviles'
        },
        {
            'nombre': 'Tablets',
            'descripcion': 'Tabletas y dispositivos táctiles portátiles'
        },
        {
            'nombre': 'Accesorios',
            'descripcion': 'Accesorios para equipos electrónicos'
        },
        {
            'nombre': 'Componentes PC',
            'descripcion': 'Componentes y piezas para computadoras'
        }
    ]

    categorias_creadas = []
    for cat_data in categorias_data:
        categoria, created = CategoriaProducto.objects.get_or_create(
            nombre=cat_data['nombre'],
            defaults={'descripcion': cat_data['descripcion']}
        )
        categorias_creadas.append(categoria)
        if created:
            print(f"  ✅ Categoría '{categoria.nombre}' creada")
        else:
            print(f"  ℹ️  Categoría '{categoria.nombre}' ya existe")

    return categorias_creadas


def generar_productos(categorias, cantidad=30):
    """Genera productos de prueba"""
    print(f"\n🛍️  Generando {cantidad} productos...")

    marcas_laptop = ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Apple']
    marcas_smartphone = ['Samsung', 'Xiaomi', 'iPhone', 'Huawei', 'Motorola', 'OnePlus']
    procesadores = ['Intel Core i5', 'Intel Core i7', 'AMD Ryzen 5', 'AMD Ryzen 7', 'Apple M1', 'Snapdragon 888']
    ram_options = ['4GB', '8GB', '16GB', '32GB', '6GB', '12GB']
    storage_options = ['128GB', '256GB', '512GB', '1TB', '2TB', '64GB']

    productos_creados = []

    for i in range(cantidad):
        try:
            categoria = random.choice(categorias)
            marca = random.choice(marcas_laptop if 'Laptop' in categoria.nombre else marcas_smartphone)

            precio_compra = Decimal(random.randint(500000, 3000000))
            margen = Decimal(random.uniform(1.3, 1.8))
            precio_venta = (precio_compra * margen).quantize(Decimal('0.01'))
            precio_mayorista = (precio_venta * Decimal('0.85')).quantize(Decimal('0.01'))

            producto = Producto.objects.create(
                nombre_producto=f"{marca} {fake.word().capitalize()} {random.randint(100, 999)}",
                codigo_sku=f"SKU-{fake.unique.random_number(digits=8, fix_len=True)}",
                categoria=categoria,
                modelo_equipo=f"{marca}-{random.randint(1000, 9999)}",
                marca=marca,
                procesador=random.choice(procesadores),
                memoria_ram=random.choice(ram_options),
                memoria_rom=random.choice(storage_options),
                descripcion=fake.text(max_nb_chars=200),
                especificaciones=fake.text(max_nb_chars=150),
                precio_compra=precio_compra,
                precio_venta=precio_venta,
                precio_mayorista=precio_mayorista,
                stock_actual=random.randint(0, 50),
                stock_minimo=random.randint(3, 10),
                stock_maximo=random.randint(50, 200),
                disponible_web=random.choice([True, True, True, False]),  # 75% disponibles
                destacado=random.choice([True, False, False, False]),  # 25% destacados
                activo=True,
                tiene_garantia=True,
                meses_garantia=random.choice([6, 12, 24, 36])
            )
            productos_creados.append(producto)
        except Exception as e:
            print(f"  ⚠️  Error al crear producto {i+1}: {e}")

    print(f"  ✅ {len(productos_creados)} productos creados exitosamente")
    return productos_creados


def generar_ventas(clientes, productos, cantidad=15):
    """Genera ventas de prueba"""
    print(f"\n💰 Generando {cantidad} ventas...")

    if not clientes or not productos:
        print("  ⚠️  No hay clientes o productos para generar ventas")
        return []

    ventas_creadas = []

    for i in range(cantidad):
        try:
            cliente = random.choice(clientes)
            estado = random.choice(['PENDIENTE', 'PROCESANDO', 'COMPLETADA', 'COMPLETADA', 'COMPLETADA'])
            metodo_pago = random.choice(['EFECTIVO', 'TARJETA', 'TRANSFERENCIA', 'PSE'])
            canal = random.choice(['TIENDA', 'WEB', 'WEB', 'TELEFONO'])

            # Crear la venta
            venta = Venta.objects.create(
                cliente=cliente,
                estado=estado,
                metodo_pago=metodo_pago,
                canal_venta=canal,
                observaciones=fake.text(max_nb_chars=100) if random.random() > 0.7 else ""
            )

            # Agregar productos a la venta (entre 1 y 5 productos)
            num_productos = random.randint(1, 5)
            productos_venta = random.sample(productos, min(num_productos, len(productos)))

            subtotal = Decimal('0.00')

            for producto in productos_venta:
                cantidad_item = random.randint(1, 3)
                precio_unitario = producto.precio_venta
                descuento_item = Decimal(random.choice([0, 0, 0, 5000, 10000]))  # Mayoría sin descuento

                # Solo crear detalle si hay stock o es venta online
                if producto.stock_actual >= cantidad_item or canal == 'WEB':
                    detalle = DetalleVenta.objects.create(
                        venta=venta,
                        producto=producto,
                        cantidad=cantidad_item,
                        precio_unitario=precio_unitario,
                        descuento_item=descuento_item,
                        con_garantia=producto.tiene_garantia
                    )
                    subtotal += detalle.subtotal

                    # Actualizar stock si está completada
                    if estado == 'COMPLETADA' and producto.stock_actual >= cantidad_item:
                        producto.stock_actual -= cantidad_item
                        producto.save()

            # Actualizar totales de la venta
            venta.subtotal = subtotal
            venta.descuento = (subtotal * Decimal('0.02')).quantize(Decimal('0.01'))  # 2% descuento adicional
            venta.impuestos = ((subtotal - venta.descuento) * Decimal('0.19')).quantize(Decimal('0.01'))  # IVA 19%
            venta.total = subtotal - venta.descuento + venta.impuestos
            venta.save()

            ventas_creadas.append(venta)

        except Exception as e:
            print(f"  ⚠️  Error al crear venta {i+1}: {e}")

    print(f"  ✅ {len(ventas_creadas)} ventas creadas exitosamente")
    return ventas_creadas


def mostrar_resumen(clientes, productos, ventas):
    """Muestra un resumen de los datos generados"""
    print("\n" + "="*60)
    print("  RESUMEN DE DATOS GENERADOS")
    print("="*60)
    print(f"\n📊 Estadísticas:")
    print(f"  • Total de clientes: {Cliente.objects.count()}")
    print(f"  • Total de categorías: {CategoriaProducto.objects.count()}")
    print(f"  • Total de productos: {Producto.objects.count()}")
    print(f"  • Total de ventas: {Venta.objects.count()}")

    if ventas:
        total_ventas = sum(v.total for v in ventas if v.total)
        print(f"  • Total en ventas generadas: ${total_ventas:,.2f} COP")

    print("\n" + "="*60)
    print("  ✅ DATOS DE PRUEBA GENERADOS EXITOSAMENTE")
    print("="*60)
    print("\n💡 Puedes ver los datos en el panel de administración:")
    print("   http://127.0.0.1:8000/admin/")
    print("\n💡 O en la tienda online:")
    print("   http://127.0.0.1:8000/tienda/")
    print("\n" + "="*60 + "\n")


def main():
    """Función principal"""

    # Confirmar antes de ejecutar
    if not confirmar_accion():
        print("\n❌ Operación cancelada por el usuario.\n")
        return

    print("\n🚀 Iniciando generación de datos de prueba...\n")

    try:
        # Generar datos
        clientes = generar_clientes(20)
        categorias = generar_categorias()
        productos = generar_productos(categorias, 30)
        ventas = generar_ventas(clientes, productos, 15)

        # Mostrar resumen
        mostrar_resumen(clientes, productos, ventas)

    except Exception as e:
        print(f"\n❌ Error durante la generación de datos: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()

