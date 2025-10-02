#!/usr/bin/env python
"""
Script para crear datos de prueba del sistema de productos.
Ejecutar: python manage.py shell < create_products_data.py
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitsoft_project.settings')
django.setup()

from main.models import Category, Product
from decimal import Decimal

def create_sample_data():
    """Crear datos de ejemplo para el sistema de productos"""
    
    print("🚀 Creando categorías de productos...")
    
    # Crear categorías
    categories_data = [
        {
            'name': 'laptops',
            'display_name': 'Laptops',
            'description': 'Computadores portátiles para trabajo, estudio y gaming'
        },
        {
            'name': 'escritorio',
            'display_name': 'Computadoras de Escritorio',
            'description': 'Computadores de escritorio y workstations'
        },
        {
            'name': 'accesorios',
            'display_name': 'Accesorios de Computadoras',
            'description': 'Accesorios y periféricos para computadores'
        },
        {
            'name': 'motos_electricas',
            'display_name': 'Motos Eléctricas',
            'description': 'Motos eléctricas para transporte urbano'
        },
        {
            'name': 'scooters',
            'display_name': 'Scooters Eléctricos',
            'description': 'Scooters eléctricos y tradicionales'
        }
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'display_name': cat_data['display_name'],
                'description': cat_data['description']
            }
        )
        categories[cat_data['name']] = category
        if created:
            print(f"✅ Categoría creada: {category.display_name}")
        else:
            print(f"📝 Categoría existente: {category.display_name}")
    
    print("\n💻 Creando productos de ejemplo...")
    
    # Productos de Laptops
    laptops_data = [
        {
            'name': 'Laptop Gaming ASUS ROG Strix G15',
            'description': 'Laptop gaming de alta performance con procesador AMD Ryzen 7, GTX 3060, 16GB RAM, 512GB SSD',
            'price': Decimal('2850000'),
            'original_price': Decimal('3166666'),
            'stock': 5,
            'sku': 'LAP-ASUS-ROG-G15-001',
            'brand': 'ASUS',
            'model': 'ROG Strix G15',
            'specifications': {
                'procesador': 'AMD Ryzen 7 5800H',
                'tarjeta_grafica': 'NVIDIA GeForce RTX 3060 6GB',
                'ram': '16GB DDR4 3200MHz',
                'almacenamiento': '512GB SSD NVMe',
                'pantalla': '15.6" Full HD 144Hz',
                'sistema_operativo': 'Windows 11'
            },
            'is_active': True
        },
        {
            'name': 'Laptop HP Pavilion 15',
            'description': 'Laptop ideal para trabajo y estudio con procesador Intel i5, 8GB RAM, 256GB SSD',
            'price': Decimal('1650000'),
            'stock': 12,
            'sku': 'LAP-HP-PAV-15-001',
            'brand': 'HP',
            'model': 'Pavilion 15',
            'specifications': {
                'procesador': 'Intel Core i5-1135G7',
                'ram': '8GB DDR4',
                'almacenamiento': '256GB SSD',
                'pantalla': '15.6" Full HD IPS',
                'bateria': 'Hasta 8 horas',
                'peso': '1.75kg'
            },
            'is_active': True
        },
        {
            'name': 'MacBook Air M2',
            'description': 'Laptop Apple con chip M2, diseño ultradelgado y gran duración de batería',
            'price': Decimal('4200000'),
            'original_price': Decimal('4421052'),
            'stock': 8,
            'sku': 'LAP-APPLE-MBA-M2-001',
            'brand': 'Apple',
            'model': 'MacBook Air M2',
            'specifications': {
                'chip': 'Apple M2 8-core CPU',
                'ram': '8GB memoria unificada',
                'almacenamiento': '256GB SSD',
                'pantalla': '13.6" Liquid Retina',
                'bateria': 'Hasta 18 horas',
                'peso': '1.24kg'
            },
            'is_active': True
        }
    ]
    
    for product_data in laptops_data:
        product_data['category'] = categories['laptops']
        product, created = Product.objects.get_or_create(
            sku=product_data['sku'],
            defaults=product_data
        )
        if created:
            print(f"✅ Producto creado: {product.name}")
    
    # Productos de Escritorio
    desktop_data = [
        {
            'name': 'PC Gaming Intel i7 RTX 4060',
            'description': 'Computador gaming completo con procesador Intel i7, RTX 4060, 32GB RAM',
            'price': Decimal('3200000'),
            'original_price': Decimal('3764705'),
            'stock': 6,
            'sku': 'PC-GAMING-I7-4060-001',
            'brand': 'Custom Build',
            'model': 'Gaming Pro i7',
            'specifications': {
                'procesador': 'Intel Core i7-13700F',
                'tarjeta_grafica': 'NVIDIA RTX 4060 8GB',
                'ram': '32GB DDR5 5600MHz',
                'almacenamiento': '1TB SSD NVMe + 2TB HDD',
                'motherboard': 'MSI B760 Gaming Plus',
                'fuente': '650W 80+ Gold Modular'
            },
            'is_active': True
        },
        {
            'name': 'PC Oficina Intel i5',
            'description': 'Computador para oficina y tareas cotidianas con Intel i5, 16GB RAM',
            'price': Decimal('1450000'),
            'stock': 15,
            'sku': 'PC-OFFICE-I5-001',
            'brand': 'Custom Build',
            'model': 'Office Pro i5',
            'specifications': {
                'procesador': 'Intel Core i5-12400',
                'ram': '16GB DDR4 3200MHz',
                'almacenamiento': '512GB SSD',
                'graficos': 'Intel UHD 730',
                'conectividad': 'Wi-Fi 6, Bluetooth 5.0'
            },
            'is_active': True
        }
    ]
    
    for product_data in desktop_data:
        product_data['category'] = categories['escritorio']
        product, created = Product.objects.get_or_create(
            sku=product_data['sku'],
            defaults=product_data
        )
        if created:
            print(f"✅ Producto creado: {product.name}")
    
    # Accesorios
    accessories_data = [
        {
            'name': 'Teclado Gaming Mecánico RGB',
            'description': 'Teclado mecánico gaming con switches Blue, retroiluminación RGB',
            'price': Decimal('285000'),
            'stock': 25,
            'sku': 'ACC-KEYBOARD-RGB-001',
            'brand': 'Gaming Pro',
            'model': 'RGB Mechanical K1',
            'specifications': {
                'switches': 'Cherry MX Blue',
                'retroiluminacion': 'RGB personalizable',
                'conectividad': 'USB-C',
                'anti_ghosting': '100% NKRO',
                'software': 'Compatible con software RGB'
            },
            'is_active': True
        },
        {
            'name': 'Monitor 27" 4K IPS',
            'description': 'Monitor profesional 4K de 27 pulgadas con panel IPS y calibración de color',
            'price': Decimal('950000'),
            'original_price': Decimal('1032608'),
            'stock': 8,
            'sku': 'ACC-MONITOR-27-4K-001',
            'brand': 'Professional',
            'model': '27" Pro 4K',
            'specifications': {
                'tamaño': '27 pulgadas',
                'resolucion': '3840 x 2160 (4K UHD)',
                'panel': 'IPS con 99% sRGB',
                'conectividad': 'HDMI 2.1, DisplayPort, USB-C',
                'ajustes': 'Altura, inclinación, rotación'
            },
            'is_active': True
        },
        {
            'name': 'Mouse Gaming Inalámbrico',
            'description': 'Mouse gaming inalámbrico con sensor óptico de alta precisión',
            'price': Decimal('165000'),
            'stock': 30,
            'sku': 'ACC-MOUSE-WIRELESS-001',
            'brand': 'Gaming Pro',
            'model': 'Wireless Pro M1',
            'specifications': {
                'sensor': 'Óptico 25,600 DPI',
                'conectividad': '2.4GHz + Bluetooth',
                'bateria': 'Hasta 70 horas',
                'botones': '8 botones programables',
                'peso': '89g'
            },
            'is_active': True
        }
    ]
    
    for product_data in accessories_data:
        product_data['category'] = categories['accesorios']
        product, created = Product.objects.get_or_create(
            sku=product_data['sku'],
            defaults=product_data
        )
        if created:
            print(f"✅ Producto creado: {product.name}")
    
    # Motos Eléctricas
    motos_data = [
        {
            'name': 'Moto Eléctrica Urban 2000W',
            'description': 'Moto eléctrica para ciudad con motor de 2000W, batería extraíble',
            'price': Decimal('6500000'),
            'original_price': Decimal('7386363'),
            'stock': 3,
            'sku': 'MOTO-URBAN-2000W-001',
            'brand': 'EcoMove',
            'model': 'Urban Pro 2000',
            'specifications': {
                'motor': '2000W brushless',
                'bateria': '60V 20Ah extraíble',
                'velocidad_maxima': '70 km/h',
                'autonomia': '80-100 km',
                'tiempo_carga': '6-8 horas',
                'peso': '85 kg'
            },
            'is_active': True
        },
        {
            'name': 'Moto Eléctrica Delivery Pro',
            'description': 'Moto eléctrica especializada para delivery con gran capacidad de carga',
            'price': Decimal('7200000'),
            'stock': 2,
            'sku': 'MOTO-DELIVERY-PRO-001',
            'brand': 'EcoMove',
            'model': 'Delivery Pro 3000',
            'specifications': {
                'motor': '3000W',
                'bateria': '72V 32Ah',
                'velocidad_maxima': '80 km/h',
                'autonomia': '120 km',
                'capacidad_carga': '150 kg',
                'extras': 'GPS integrado'
            },
            'is_active': True
        }
    ]
    
    for product_data in motos_data:
        product_data['category'] = categories['motos_electricas']
        product, created = Product.objects.get_or_create(
            sku=product_data['sku'],
            defaults=product_data
        )
        if created:
            print(f"✅ Producto creado: {product.name}")
    
    # Scooters
    scooters_data = [
        {
            'name': 'Scooter Eléctrico Plegable',
            'description': 'Scooter eléctrico plegable para transporte urbano, ligero y portátil',
            'price': Decimal('850000'),
            'original_price': Decimal('1062500'),
            'stock': 15,
            'sku': 'SCOOTER-FOLD-350W-001',
            'brand': 'UrbanMove',
            'model': 'Fold Pro 350',
            'specifications': {
                'motor': '350W',
                'bateria': '36V 7.8Ah',
                'velocidad_maxima': '25 km/h',
                'autonomia': '25-30 km',
                'peso': '12.5 kg',
                'tiempo_carga': '3-4 horas'
            },
            'is_active': True
        },
        {
            'name': 'Scooter Pro Max 500W',
            'description': 'Scooter eléctrico de alta gama con suspensión y gran autonomía',
            'price': Decimal('1450000'),
            'stock': 8,
            'sku': 'SCOOTER-PRO-MAX-500W-001',
            'brand': 'UrbanMove',
            'model': 'Pro Max 500',
            'specifications': {
                'motor': '500W dual',
                'bateria': '48V 13Ah',
                'velocidad_maxima': '45 km/h',
                'autonomia': '45-55 km',
                'suspension': 'Delantera y trasera',
                'frenos': 'Disco hidráulicos'
            },
            'is_active': True
        }
    ]
    
    for product_data in scooters_data:
        product_data['category'] = categories['scooters']
        product, created = Product.objects.get_or_create(
            sku=product_data['sku'],
            defaults=product_data
        )
        if created:
            print(f"✅ Producto creado: {product.name}")
    
    print(f"\n🎉 ¡Datos de prueba creados exitosamente!")
    print(f"📊 Resumen:")
    print(f"   - Categorías: {Category.objects.count()}")
    print(f"   - Productos: {Product.objects.count()}")
    print(f"\n🔗 Ahora puedes visitar:")
    print(f"   - Catálogo: http://127.0.0.1:8000/productos/")
    print(f"   - Admin: http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    create_sample_data()