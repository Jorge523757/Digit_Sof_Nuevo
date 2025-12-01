            'modelo_equipo': 'LaserJet Pro M404dn',
            'marca': 'HP',
            'descripcion': 'Impresora láser monocromática de alta velocidad para oficina',
            'especificaciones': '38ppm, Duplex automático, Red ethernet',
            'precio_compra': Decimal('250.00'),
            'precio_venta': Decimal('380.00'),
            'precio_mayorista': Decimal('340.00'),
            'stock_actual': 7,
            'stock_minimo': 3,
            'disponible_web': True,
            'destacado': False,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 12,
        },
        {
            'nombre_producto': 'Impresora Multifuncional Epson L3250',
            'codigo_sku': 'IMP-EPS-002',
            'categoria': 'Impresoras',
            'modelo_equipo': 'EcoTank L3250',
            'marca': 'Epson',
            'descripcion': 'Impresora multifuncional con sistema de tanque de tinta, WiFi',
            'especificaciones': 'Imprime, copia, escanea, WiFi, Alta capacidad de tinta',
            'precio_compra': Decimal('180.00'),
            'precio_venta': Decimal('280.00'),
            'precio_mayorista': Decimal('250.00'),
            'stock_actual': 10,
            'stock_minimo': 4,
            'disponible_web': True,
            'destacado': True,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 12,
        },

        # Componentes
        {
            'nombre_producto': 'Memoria RAM Kingston 16GB DDR4',
            'codigo_sku': 'COM-RAM-001',
            'categoria': 'Componentes',
            'marca': 'Kingston',
            'memoria_ram': '16GB DDR4 3200MHz',
            'descripcion': 'Módulo de memoria RAM DDR4 de 16GB a 3200MHz para gaming y productividad',
            'precio_compra': Decimal('45.00'),
            'precio_venta': Decimal('70.00'),
            'precio_mayorista': Decimal('60.00'),
            'stock_actual': 40,
            'stock_minimo': 20,
            'disponible_web': True,
            'destacado': False,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 60,
        },
        {
            'nombre_producto': 'Disco Duro SSD Samsung 1TB',
            'codigo_sku': 'COM-SSD-002',
            'categoria': 'Componentes',
            'marca': 'Samsung',
            'memoria_rom': '1TB NVMe M.2',
            'descripcion': 'Unidad de estado sólido NVMe de 1TB con velocidades de hasta 3500MB/s',
            'especificaciones': 'NVMe PCIe Gen 3.0, 3500MB/s lectura',
            'precio_compra': Decimal('75.00'),
            'precio_venta': Decimal('120.00'),
            'precio_mayorista': Decimal('105.00'),
            'stock_actual': 35,
            'stock_minimo': 15,
            'disponible_web': True,
            'destacado': True,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 60,
        },
    ]

    print("\n" + "=" * 70)
    print("CREANDO PRODUCTOS")
    print("=" * 70)

    productos_creados = 0
    for prod_data in productos:
        categoria_nombre = prod_data.pop('categoria')
        categoria = categorias_creadas[categoria_nombre]

        producto, created = Producto.objects.get_or_create(
            codigo_sku=prod_data['codigo_sku'],
            defaults={**prod_data, 'categoria': categoria}
        )

        if created:
            productos_creados += 1
            status = "✅ CREADO"
        else:
            status = "📌 EXISTENTE"

        print(f"{status} - {producto.nombre_producto} ({producto.categoria.nombre})")

    print("\n" + "=" * 70)
    print("RESUMEN DE DATOS CREADOS")
    print("=" * 70)
    print(f"✅ Categorías totales: {CategoriaProducto.objects.count()}")
    print(f"✅ Productos totales: {Producto.objects.count()}")
    print(f"✅ Productos nuevos creados: {productos_creados}")
    print(f"✅ Productos activos: {Producto.objects.filter(activo=True).count()}")
    print(f"✅ Productos disponibles en web: {Producto.objects.filter(disponible_web=True).count()}")
    print(f"✅ Productos destacados: {Producto.objects.filter(destacado=True).count()}")
    print("=" * 70)
    print("\n🎉 ¡Datos de prueba creados exitosamente!")
    print("🌐 Ahora puedes ver los productos en la página principal: http://127.0.0.1:8000/")
    print("=" * 70)

if __name__ == '__main__':
    crear_datos_productos()
"""
Script para agregar productos de prueba organizados por categorías
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto
from decimal import Decimal

def crear_datos_productos():
    print("=" * 70)
    print("CREANDO CATEGORÍAS Y PRODUCTOS DE PRUEBA")
    print("=" * 70)

    # Limpiar datos existentes (opcional)
    respuesta = input("\n¿Desea limpiar los productos existentes? (s/n): ")
    if respuesta.lower() == 's':
        Producto.objects.all().delete()
        CategoriaProducto.objects.all().delete()
        print("✅ Datos anteriores eliminados")

    # Crear Categorías
    categorias = [
        {
            'nombre': 'Laptops',
            'descripcion': 'Portátiles de alta gama para trabajo y entretenimiento',
            'activo': True
        },
        {
            'nombre': 'Computadoras de Escritorio',
            'descripcion': 'PCs de escritorio potentes para oficina y gaming',
            'activo': True
        },
        {
            'nombre': 'Accesorios',
            'descripcion': 'Teclados, mouse, audífonos y más',
            'activo': True
        },
        {
            'nombre': 'Impresoras',
            'descripcion': 'Impresoras multifuncionales y de alta velocidad',
            'activo': True
        },
        {
            'nombre': 'Componentes',
            'descripcion': 'Memorias RAM, discos duros y procesadores',
            'activo': True
        },
    ]

    categorias_creadas = {}
    for cat_data in categorias:
        categoria, created = CategoriaProducto.objects.get_or_create(
            nombre=cat_data['nombre'],
            defaults=cat_data
        )
        categorias_creadas[cat_data['nombre']] = categoria
        print(f"{'✅ Creada' if created else '📌 Existente'} - Categoría: {categoria.nombre}")

    # Crear Productos
    productos = [
        # Laptops
        {
            'nombre_producto': 'Laptop HP Pavilion 15',
            'codigo_sku': 'LAP-HP-001',
            'categoria': 'Laptops',
            'modelo_equipo': 'Pavilion 15-eh2000',
            'marca': 'HP',
            'procesador': 'AMD Ryzen 5 5500U',
            'memoria_ram': '8GB DDR4',
            'memoria_rom': '512GB SSD',
            'descripcion': 'Laptop ideal para trabajo y estudio con pantalla Full HD de 15.6 pulgadas',
            'especificaciones': 'Pantalla FHD, Windows 11, Batería de larga duración',
            'precio_compra': Decimal('450.00'),
            'precio_venta': Decimal('650.00'),
            'precio_mayorista': Decimal('600.00'),
            'stock_actual': 10,
            'stock_minimo': 3,
            'disponible_web': True,
            'destacado': True,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 12,
        },
        {
            'nombre_producto': 'Laptop Lenovo IdeaPad 3',
            'codigo_sku': 'LAP-LEN-002',
            'categoria': 'Laptops',
            'modelo_equipo': 'IdeaPad 3 15ITL6',
            'marca': 'Lenovo',
            'procesador': 'Intel Core i5 11th Gen',
            'memoria_ram': '8GB DDR4',
            'memoria_rom': '256GB SSD',
            'descripcion': 'Laptop económica perfecta para estudiantes y uso diario',
            'precio_compra': Decimal('400.00'),
            'precio_venta': Decimal('580.00'),
            'precio_mayorista': Decimal('530.00'),
            'stock_actual': 15,
            'stock_minimo': 5,
            'disponible_web': True,
            'destacado': False,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 12,
        },
        {
            'nombre_producto': 'Laptop Dell Inspiron 15',
            'codigo_sku': 'LAP-DEL-003',
            'categoria': 'Laptops',
            'modelo_equipo': 'Inspiron 15 3000',
            'marca': 'Dell',
            'procesador': 'Intel Core i7 11th Gen',
            'memoria_ram': '16GB DDR4',
            'memoria_rom': '1TB SSD',
            'descripcion': 'Laptop profesional con alto rendimiento para multitarea',
            'precio_compra': Decimal('750.00'),
            'precio_venta': Decimal('1050.00'),
            'precio_mayorista': Decimal('950.00'),
            'stock_actual': 8,
            'stock_minimo': 2,
            'disponible_web': True,
            'destacado': True,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 24,
        },

        # Computadoras de Escritorio
        {
            'nombre_producto': 'PC Gamer RGB Master',
            'codigo_sku': 'PC-GAM-001',
            'categoria': 'Computadoras de Escritorio',
            'modelo_equipo': 'Custom Build',
            'marca': 'Ensamblado',
            'procesador': 'AMD Ryzen 7 5800X',
            'memoria_ram': '32GB DDR4',
            'memoria_rom': '1TB NVMe SSD',
            'descripcion': 'PC Gamer de alta gama con iluminación RGB y tarjeta gráfica RTX 3070',
            'especificaciones': 'RTX 3070 8GB, Fuente 750W, Gabinete RGB',
            'precio_compra': Decimal('1200.00'),
            'precio_venta': Decimal('1800.00'),
            'precio_mayorista': Decimal('1600.00'),
            'stock_actual': 5,
            'stock_minimo': 2,
            'disponible_web': True,
            'destacado': True,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 12,
        },
        {
            'nombre_producto': 'PC Oficina Plus',
            'codigo_sku': 'PC-OFI-002',
            'categoria': 'Computadoras de Escritorio',
            'modelo_equipo': 'Business Desktop',
            'marca': 'HP',
            'procesador': 'Intel Core i5 10th Gen',
            'memoria_ram': '8GB DDR4',
            'memoria_rom': '512GB SSD',
            'descripcion': 'Computadora de escritorio ideal para oficina y tareas administrativas',
            'precio_compra': Decimal('400.00'),
            'precio_venta': Decimal('600.00'),
            'precio_mayorista': Decimal('550.00'),
            'stock_actual': 12,
            'stock_minimo': 4,
            'disponible_web': True,
            'destacado': False,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 12,
        },

        # Accesorios
        {
            'nombre_producto': 'Teclado Mecánico RGB K95',
            'codigo_sku': 'ACC-TEC-001',
            'categoria': 'Accesorios',
            'marca': 'Corsair',
            'descripcion': 'Teclado mecánico gaming con switches Cherry MX e iluminación RGB personalizable',
            'precio_compra': Decimal('80.00'),
            'precio_venta': Decimal('130.00'),
            'precio_mayorista': Decimal('110.00'),
            'stock_actual': 25,
            'stock_minimo': 10,
            'disponible_web': True,
            'destacado': True,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 24,
        },
        {
            'nombre_producto': 'Mouse Gamer Logitech G502',
            'codigo_sku': 'ACC-MOU-002',
            'categoria': 'Accesorios',
            'marca': 'Logitech',
            'descripcion': 'Mouse gaming de alta precisión con sensor HERO 25K y pesos ajustables',
            'precio_compra': Decimal('45.00'),
            'precio_venta': Decimal('75.00'),
            'precio_mayorista': Decimal('65.00'),
            'stock_actual': 30,
            'stock_minimo': 15,
            'disponible_web': True,
            'destacado': False,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 12,
        },
        {
            'nombre_producto': 'Audífonos HyperX Cloud II',
            'codigo_sku': 'ACC-AUD-003',
            'categoria': 'Accesorios',
            'marca': 'HyperX',
            'descripcion': 'Audífonos gaming con sonido envolvente 7.1 y micrófono desmontable',
            'precio_compra': Decimal('60.00'),
            'precio_venta': Decimal('95.00'),
            'precio_mayorista': Decimal('85.00'),
            'stock_actual': 20,
            'stock_minimo': 8,
            'disponible_web': True,
            'destacado': True,
            'activo': True,
            'tiene_garantia': True,
            'meses_garantia': 24,
        },

        # Impresoras
        {
            'nombre_producto': 'Impresora HP LaserJet Pro',
            'codigo_sku': 'IMP-HP-001',
            'categoria': 'Impresoras',

