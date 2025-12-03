            'codigo_sku': 'HP-ORIGINAL-PROT-005',
            'modelo_equipo': 'HP Victus Gaming Series',
            'marca': 'HP Official',
            'descripcion': 'Protector oficial especializado para la línea HP Victus. Diseño ergonómico y materiales de primera calidad.',
            'especificaciones': '''
            • Certificación HP Original
            • Warranty: 12 months
            • Material: Premium polymer
            • Gaming grade protection
            • RGB lighting compatible
            • Professional installation
            ''',
            'precio_compra': Decimal('28000'),
            'precio_venta': Decimal('75000'),
            'precio_mayorista': Decimal('60000'),
            'stock_actual': 8,
            'destacado': True,
        },
        {
            'nombre_producto': 'Kit completo protección HP Victus 15.6"',
            'codigo_sku': 'HP-KIT-COMPLETO-006',
            'modelo_equipo': 'HP Victus 15.6 pulgadas',
            'marca': 'Protection Kit',
            'descripcion': 'Kit completo de protección para HP Victus 15.6". Incluye protector de pantalla, teclado y palm rest.',
            'especificaciones': '''
            • Screen protector anti-glare
            • Keyboard cover TPU
            • Palm rest protector
            • Webcam privacy slider
            • Port dust plugs
            • Cleaning kit included
            ''',
            'precio_compra': Decimal('35000'),
            'precio_venta': Decimal('89990'),
            'precio_mayorista': Decimal('70000'),
            'stock_actual': 24,
            'destacado': False,
        }
    ]

    productos_creados = 0
    productos_actualizados = 0

    for producto_data in productos:
        producto, created = Producto.objects.get_or_create(
            codigo_sku=producto_data['codigo_sku'],
            defaults={
                'categoria': categoria,
                **producto_data
            }
        )

        if created:
            productos_creados += 1
            print(f"✅ Producto creado: {producto.nombre_producto} - ${producto.precio_venta:,.0f}")
        else:
            # Actualizar datos si ya existe
            for key, value in producto_data.items():
                if key != 'codigo_sku':
                    setattr(producto, key, value)
            if producto_data.get('categoria'):
                producto.categoria = categoria
            producto.save()
            productos_actualizados += 1
            print(f"🔄 Producto actualizado: {producto.nombre_producto}")

    print(f"\n📊 Resumen:")
    print(f"   ✅ Productos creados: {productos_creados}")
    print(f"   🔄 Productos actualizados: {productos_actualizados}")
    print(f"   📦 Total en catálogo: {Producto.objects.filter(categoria=categoria).count()}")

    # Estadísticas adicionales
    total_productos = Producto.objects.filter(activo=True, disponible_web=True).count()
    productos_destacados = Producto.objects.filter(destacado=True, activo=True).count()

    print(f"\n🛒 Estadísticas E-commerce:")
    print(f"   📱 Total productos activos: {total_productos}")
    print(f"   ⭐ Productos destacados: {productos_destacados}")
    print(f"   💰 Rango de precios: ${Producto.objects.filter(activo=True).aggregate(min_precio=min('precio_venta'), max_precio=max('precio_venta'))['min_precio']:,.0f} - ${Producto.objects.filter(activo=True).aggregate(min_precio=min('precio_venta'), max_precio=max('precio_venta'))['max_precio']:,.0f}")

if __name__ == '__main__':
    crear_productos_aliexpress()
    print("\n✅ ¡Productos estilo AliExpress creados exitosamente!")
    print("🎉 Ahora puedes ver el catálogo en /tienda/")
"""
Script para crear productos similares a AliExpress (protectores de teclado HP Victus)
"""

import os
import django
import sys

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import CategoriaProducto, Producto
from decimal import Decimal

def crear_productos_aliexpress():
    """Crear productos similares a los de AliExpress"""

    print("🔧 Creando productos estilo AliExpress...")

    # Crear categoría si no existe
    categoria, created = CategoriaProducto.objects.get_or_create(
        nombre="Accesorios para Laptops",
        defaults={
            'descripcion': "Accesorios y protectores para laptops y notebooks",
            'activo': True
        }
    )

    if created:
        print(f"✅ Categoría creada: {categoria.nombre}")
    else:
        print(f"📂 Categoría existente: {categoria.nombre}")

    # Productos similares a los de AliExpress
    productos = [
        {
            'nombre_producto': 'Funda de silicona para teclado de portátil HP Victus 15 2022 2021',
            'codigo_sku': 'HP-VICTUS-15-SILICONA-001',
            'modelo_equipo': 'HP Victus 15-fb0019ax 15-fa0000ni 15-fa0006ni 15-fa 15.6 pulgadas',
            'marca': 'Compatible HP',
            'descripcion': 'Nueva funda superior para ordenador portátil, funda superior con reposama... Protector de teclado transparente TPU para HP Victus Gaming Laptop',
            'especificaciones': '''
            • Material: TPU (Poliuretano termoplástico)
            • Compatibilidad: HP Victus 15/16 series
            • Color: Transparente
            • Protección contra polvo, líquidos y desgaste
            • Fácil instalación y remoción
            • No interfiere con el tipeo
            ''',
            'precio_compra': Decimal('15000'),
            'precio_venta': Decimal('23965'),
            'precio_mayorista': Decimal('19000'),
            'stock_actual': 95,
            'destacado': True,
        },
        {
            'nombre_producto': 'Nueva funda superior para ordenador portátil HP Victus 16.1',
            'codigo_sku': 'HP-VICTUS-16-FUNDA-002',
            'modelo_equipo': 'HP Victus 16.1 pulgadas',
            'marca': 'OEM Compatible',
            'descripcion': 'Funda protectora superior de alta calidad para laptop HP Victus 16.1 pulgadas. Material premium que protege contra rayones y golpes.',
            'especificaciones': '''
            • Material: PC+ABS de alta calidad
            • Tamaño: 16.1 pulgadas
            • Diseño: Ultra delgado
            • Colores disponibles: Varios
            • Protección 360 grados
            • Ventilación optimizada
            ''',
            'precio_compra': Decimal('45000'),
            'precio_venta': Decimal('107212'),
            'precio_mayorista': Decimal('85000'),
            'stock_actual': 16,
            'destacado': True,
        },
        {
            'nombre_producto': 'Para HP Victus 16.1 Cubierta de silicona colorida',
            'codigo_sku': 'HP-VICTUS-CUBIERTA-003',
            'modelo_equipo': 'HP Victus 16.1',
            'marca': 'Generic',
            'descripcion': 'Cubierta protectora de silicona en múltiples colores para HP Victus 16.1. Diseño moderno y protección efectiva.',
            'especificaciones': '''
            • Material: Silicona premium
            • Colores: Negro, Azul, Rosa, Verde, Transparente
            • Anti-slip texture
            • Easy snap-on design
            • Heat dissipation holes
            • Lightweight protection
            ''',
            'precio_compra': Decimal('8000'),
            'precio_venta': Decimal('12154'),
            'precio_mayorista': Decimal('9500'),
            'stock_actual': 412,
            'destacado': False,
        },
        {
            'nombre_producto': 'Funda de teclado TPU para HP Victus 15/16',
            'codigo_sku': 'HP-TPU-KEYBOARD-004',
            'modelo_equipo': 'HP Victus 15/16 Gaming Laptop',
            'marca': 'Universal',
            'descripcion': 'Protector de teclado TPU ultra-delgado para laptops gaming HP Victus. Protección contra derrames y polvo.',
            'especificaciones': '''
            • Material: TPU medical grade
            • Thickness: 0.1mm
            • Transparency: 95%+
            • Keyboard layout: Spanish/English
            • Gaming optimized
            • Dishwasher safe
            ''',
            'precio_compra': Decimal('12000'),
            'precio_venta': Decimal('31755'),
            'precio_mayorista': Decimal('25000'),
            'stock_actual': 16,
            'destacado': True,
        },
        {
            'nombre_producto': 'Protector original especializado para HP Victus',
