"""
Script para crear productos de prueba en el sistema
Ejecutar desde DIGTSoft/: python scripts/crear_productos_prueba.py
"""

import os
import sys
import django

# Agregar el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto
from decimal import Decimal

def crear_categorias():
    """Crear categorías de productos"""
    categorias_data = [
        {'nombre': 'Laptops', 'descripcion': 'Computadores portátiles'},
        {'nombre': 'Desktops', 'descripcion': 'Computadores de escritorio'},
        {'nombre': 'Componentes', 'descripcion': 'Componentes de hardware'},
        {'nombre': 'Periféricos', 'descripcion': 'Teclados, mouse, monitores'},
        {'nombre': 'Smartphones', 'descripcion': 'Teléfonos inteligentes'},
        {'nombre': 'Tablets', 'descripcion': 'Tabletas y iPads'},
        {'nombre': 'Accesorios', 'descripcion': 'Cables, cargadores, fundas'},
    ]

    categorias = []
    for cat_data in categorias_data:
        cat, created = CategoriaProducto.objects.get_or_create(
            nombre=cat_data['nombre'],
            defaults={'descripcion': cat_data['descripcion']}
        )
        categorias.append(cat)
        if created:
            print(f"✅ Categoría creada: {cat.nombre}")

    return categorias

def crear_productos(categorias):
    """Crear 20 productos de prueba"""

    productos_data = [
        # Laptops
        {
            'nombre_producto': 'Laptop Dell Inspiron 15 3000',
            'codigo_sku': 'LAPTOP-DELL-001',
            'categoria': categorias[0],
            'modelo_equipo': 'Inspiron 15 3000',
            'marca': 'Dell',
            'procesador': 'Intel Core i5 11va Gen',
            'memoria_ram': '8GB DDR4',
            'memoria_rom': '256GB SSD',
            'descripcion': 'Laptop ideal para trabajo y estudio con procesador Intel Core i5',
            'precio_compra': Decimal('2500000'),
            'precio_venta': Decimal('3200000'),
            'precio_mayorista': Decimal('2900000'),
            'stock_actual': 15,
            'stock_minimo': 5,
            'stock_maximo': 50,
        },
        {
            'nombre_producto': 'Laptop HP Pavilion 14',
            'codigo_sku': 'LAPTOP-HP-001',
            'categoria': categorias[0],
            'modelo_equipo': 'Pavilion 14',
            'marca': 'HP',
            'procesador': 'AMD Ryzen 5',
            'memoria_ram': '16GB DDR4',
            'memoria_rom': '512GB SSD',
            'descripcion': 'Laptop HP con procesador AMD Ryzen 5 y gran capacidad de almacenamiento',
            'precio_compra': Decimal('3000000'),
            'precio_venta': Decimal('3800000'),
            'stock_actual': 10,
            'stock_minimo': 5,
            'stock_maximo': 40,
        },
        {
            'nombre_producto': 'MacBook Air M2',
            'codigo_sku': 'LAPTOP-APPLE-001',
            'categoria': categorias[0],
            'modelo_equipo': 'MacBook Air M2 2023',
            'marca': 'Apple',
            'procesador': 'Apple M2',
            'memoria_ram': '8GB Unified',
            'memoria_rom': '256GB SSD',
            'descripcion': 'MacBook Air con chip M2, ultradelgado y potente',
            'precio_compra': Decimal('5500000'),
            'precio_venta': Decimal('6800000'),
            'stock_actual': 5,
            'stock_minimo': 2,
            'stock_maximo': 20,
        },

        # Desktops
        {
            'nombre_producto': 'PC Gamer AMD Ryzen 7',
            'codigo_sku': 'DESKTOP-GAMER-001',
            'categoria': categorias[1],
            'modelo_equipo': 'Custom Build',
            'marca': 'Ensamblado',
            'procesador': 'AMD Ryzen 7 5800X',
            'memoria_ram': '32GB DDR4',
            'memoria_rom': '1TB NVMe SSD',
            'descripcion': 'PC Gamer de alto rendimiento con RTX 3060',
            'precio_compra': Decimal('4500000'),
            'precio_venta': Decimal('5800000'),
            'stock_actual': 8,
            'stock_minimo': 3,
            'stock_maximo': 25,
        },
        {
            'nombre_producto': 'iMac 24" M1',
            'codigo_sku': 'DESKTOP-APPLE-001',
            'categoria': categorias[1],
            'modelo_equipo': 'iMac 24" 2021',
            'marca': 'Apple',
            'procesador': 'Apple M1',
            'memoria_ram': '8GB Unified',
            'memoria_rom': '256GB SSD',
            'descripcion': 'iMac todo en uno con pantalla Retina 4.5K',
            'precio_compra': Decimal('6000000'),
            'precio_venta': Decimal('7500000'),
            'stock_actual': 3,
            'stock_minimo': 1,
            'stock_maximo': 15,
        },

        # Componentes
        {
            'nombre_producto': 'Memoria RAM Kingston 16GB DDR4',
            'codigo_sku': 'RAM-KING-16GB',
            'categoria': categorias[2],
            'marca': 'Kingston',
            'modelo_equipo': 'DDR4 3200MHz',
            'memoria_ram': '16GB',
            'descripcion': 'Memoria RAM DDR4 de 16GB a 3200MHz',
            'precio_compra': Decimal('250000'),
            'precio_venta': Decimal('350000'),
            'stock_actual': 50,
            'stock_minimo': 20,
            'stock_maximo': 100,
        },
        {
            'nombre_producto': 'SSD Samsung 1TB NVMe',
            'codigo_sku': 'SSD-SAMSUNG-1TB',
            'categoria': categorias[2],
            'marca': 'Samsung',
            'modelo_equipo': '980 PRO',
            'memoria_rom': '1TB NVMe',
            'descripcion': 'SSD NVMe de 1TB con velocidades de lectura de hasta 7000MB/s',
            'precio_compra': Decimal('450000'),
            'precio_venta': Decimal('600000'),
            'stock_actual': 30,
            'stock_minimo': 15,
            'stock_maximo': 80,
        },
        {
            'nombre_producto': 'Tarjeta Gráfica RTX 3060 Ti',
            'codigo_sku': 'GPU-NVIDIA-3060TI',
            'categoria': categorias[2],
            'marca': 'NVIDIA',
            'modelo_equipo': 'GeForce RTX 3060 Ti',
            'descripcion': 'Tarjeta gráfica NVIDIA RTX 3060 Ti con 8GB GDDR6',
            'precio_compra': Decimal('2000000'),
            'precio_venta': Decimal('2600000'),
            'stock_actual': 12,
            'stock_minimo': 5,
            'stock_maximo': 30,
        },

        # Periféricos
        {
            'nombre_producto': 'Monitor LG 27" 4K',
            'codigo_sku': 'MONITOR-LG-27-4K',
            'categoria': categorias[3],
            'marca': 'LG',
            'modelo_equipo': '27UP850-W',
            'descripcion': 'Monitor LG 27 pulgadas con resolución 4K UHD',
            'precio_compra': Decimal('1200000'),
            'precio_venta': Decimal('1600000'),
            'stock_actual': 20,
            'stock_minimo': 8,
            'stock_maximo': 50,
        },
        {
            'nombre_producto': 'Teclado Mecánico Logitech G Pro',
            'codigo_sku': 'TECLADO-LOGI-GPRO',
            'categoria': categorias[3],
            'marca': 'Logitech',
            'modelo_equipo': 'G Pro Mechanical',
            'descripcion': 'Teclado mecánico gaming con switches GX Blue',
            'precio_compra': Decimal('400000'),
            'precio_venta': Decimal('550000'),
            'stock_actual': 25,
            'stock_minimo': 10,
            'stock_maximo': 60,
        },
        {
            'nombre_producto': 'Mouse Razer DeathAdder V2',
            'codigo_sku': 'MOUSE-RAZER-DAV2',
            'categoria': categorias[3],
            'marca': 'Razer',
            'modelo_equipo': 'DeathAdder V2',
            'descripcion': 'Mouse gaming ergonómico con sensor óptico de 20000 DPI',
            'precio_compra': Decimal('180000'),
            'precio_venta': Decimal('260000'),
            'stock_actual': 40,
            'stock_minimo': 15,
            'stock_maximo': 80,
        },

        # Smartphones
        {
            'nombre_producto': 'iPhone 14 Pro 128GB',
            'codigo_sku': 'PHONE-APPLE-14PRO',
            'categoria': categorias[4],
            'marca': 'Apple',
            'modelo_equipo': 'iPhone 14 Pro',
            'procesador': 'A16 Bionic',
            'memoria_ram': '6GB',
            'memoria_rom': '128GB',
            'descripcion': 'iPhone 14 Pro con Dynamic Island y cámara de 48MP',
            'precio_compra': Decimal('4500000'),
            'precio_venta': Decimal('5500000'),
            'stock_actual': 8,
            'stock_minimo': 3,
            'stock_maximo': 25,
        },
        {
            'nombre_producto': 'Samsung Galaxy S23 Ultra',
            'codigo_sku': 'PHONE-SAMSUNG-S23U',
            'categoria': categorias[4],
            'marca': 'Samsung',
            'modelo_equipo': 'Galaxy S23 Ultra',
            'procesador': 'Snapdragon 8 Gen 2',
            'memoria_ram': '12GB',
            'memoria_rom': '256GB',
            'descripcion': 'Samsung Galaxy S23 Ultra con S Pen y cámara de 200MP',
            'precio_compra': Decimal('4800000'),
            'precio_venta': Decimal('5900000'),
            'stock_actual': 6,
            'stock_minimo': 2,
            'stock_maximo': 20,
        },
        {
            'nombre_producto': 'Xiaomi Redmi Note 12 Pro',
            'codigo_sku': 'PHONE-XIAOMI-RN12P',
            'categoria': categorias[4],
            'marca': 'Xiaomi',
            'modelo_equipo': 'Redmi Note 12 Pro',
            'procesador': 'MediaTek Dimensity 1080',
            'memoria_ram': '8GB',
            'memoria_rom': '256GB',
            'descripcion': 'Xiaomi Redmi Note 12 Pro con cámara de 200MP',
            'precio_compra': Decimal('1200000'),
            'precio_venta': Decimal('1600000'),
            'stock_actual': 18,
            'stock_minimo': 8,
            'stock_maximo': 45,
        },

        # Tablets
        {
            'nombre_producto': 'iPad Air M1 64GB',
            'codigo_sku': 'TABLET-APPLE-AIR',
            'categoria': categorias[5],
            'marca': 'Apple',
            'modelo_equipo': 'iPad Air 5ta Gen',
            'procesador': 'Apple M1',
            'memoria_ram': '8GB',
            'memoria_rom': '64GB',
            'descripcion': 'iPad Air con chip M1 y pantalla Liquid Retina de 10.9"',
            'precio_compra': Decimal('2500000'),
            'precio_venta': Decimal('3200000'),
            'stock_actual': 10,
            'stock_minimo': 4,
            'stock_maximo': 30,
        },
        {
            'nombre_producto': 'Samsung Galaxy Tab S8',
            'codigo_sku': 'TABLET-SAMSUNG-S8',
            'categoria': categorias[5],
            'marca': 'Samsung',
            'modelo_equipo': 'Galaxy Tab S8',
            'procesador': 'Snapdragon 8 Gen 1',
            'memoria_ram': '8GB',
            'memoria_rom': '128GB',
            'descripcion': 'Samsung Galaxy Tab S8 con S Pen incluido',
            'precio_compra': Decimal('2200000'),
            'precio_venta': Decimal('2900000'),
            'stock_actual': 12,
            'stock_minimo': 5,
            'stock_maximo': 35,
        },

        # Accesorios
        {
            'nombre_producto': 'Cargador MacBook USB-C 67W',
            'codigo_sku': 'ACC-CARGADOR-MAC67',
            'categoria': categorias[6],
            'marca': 'Apple',
            'modelo_equipo': 'USB-C Power Adapter',
            'descripcion': 'Cargador original Apple USB-C de 67W para MacBook',
            'precio_compra': Decimal('180000'),
            'precio_venta': Decimal('250000'),
            'stock_actual': 35,
            'stock_minimo': 15,
            'stock_maximo': 70,
        },
        {
            'nombre_producto': 'Cable HDMI 4K 2 metros',
            'codigo_sku': 'ACC-CABLE-HDMI4K',
            'categoria': categorias[6],
            'marca': 'Belkin',
            'modelo_equipo': 'HDMI 2.1',
            'descripcion': 'Cable HDMI 2.1 certificado compatible con 4K@120Hz',
            'precio_compra': Decimal('35000'),
            'precio_venta': Decimal('55000'),
            'stock_actual': 60,
            'stock_minimo': 25,
            'stock_maximo': 120,
        },
        {
            'nombre_producto': 'Funda Laptop 15.6"',
            'codigo_sku': 'ACC-FUNDA-LAP156',
            'categoria': categorias[6],
            'marca': 'Case Logic',
            'descripcion': 'Funda acolchada para laptop de hasta 15.6 pulgadas',
            'precio_compra': Decimal('45000'),
            'precio_venta': Decimal('75000'),
            'stock_actual': 45,
            'stock_minimo': 20,
            'stock_maximo': 90,
        },
        {
            'nombre_producto': 'Hub USB-C 7 en 1',
            'codigo_sku': 'ACC-HUB-USBC-7EN1',
            'categoria': categorias[6],
            'marca': 'Anker',
            'modelo_equipo': 'PowerExpand 7-in-1',
            'descripcion': 'Hub USB-C con HDMI, USB 3.0, lector de tarjetas SD y más',
            'precio_compra': Decimal('120000'),
            'precio_venta': Decimal('180000'),
            'stock_actual': 28,
            'stock_minimo': 12,
            'stock_maximo': 60,
        },
    ]

    productos_creados = 0
    for prod_data in productos_data:
        producto, created = Producto.objects.get_or_create(
            codigo_sku=prod_data['codigo_sku'],
            defaults=prod_data
        )
        if created:
            productos_creados += 1
            stock_status = "✅" if producto.stock_disponible else "❌"
            print(f"{stock_status} Producto creado: {producto.nombre_producto} (Stock: {producto.stock_actual})")

    return productos_creados

def main():
    print("=" * 60)
    print("CREANDO PRODUCTOS DE PRUEBA PARA DIGT SOFT")
    print("=" * 60)
    print()

    # Eliminar productos existentes (opcional)
    # Producto.objects.all().delete()
    # CategoriaProducto.objects.all().delete()

    # Crear categorías
    print("📁 Creando categorías de productos...")
    categorias = crear_categorias()
    print(f"✅ {len(categorias)} categorías disponibles\n")

    # Crear productos
    print("📦 Creando productos de prueba...")
    productos_creados = crear_productos(categorias)

    print()
    print("=" * 60)
    print(f"✅ PROCESO COMPLETADO")
    print(f"📦 Total productos creados: {productos_creados}")
    print(f"📁 Total categorías: {CategoriaProducto.objects.count()}")
    print(f"📊 Total productos en sistema: {Producto.objects.count()}")
    print(f"✅ Productos activos: {Producto.objects.filter(activo=True).count()}")
    print(f"⚠️  Productos con bajo stock: {len([p for p in Producto.objects.all() if p.necesita_reposicion])}")
    print("=" * 60)

if __name__ == '__main__':
    main()

