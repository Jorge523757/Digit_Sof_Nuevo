#!/usr/bin/env python3
"""
Script para crear productos de prueba para el sistema de ecommerce
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto
from decimal import Decimal


def crear_categorias():
    """Crear categorías de productos"""
    categorias = [
        {"nombre": "Laptop", "descripcion": "Computadoras portátiles"},
        {"nombre": "Accesorio", "descripcion": "Accesorios y periféricos"},
        {"nombre": "Computadora", "descripcion": "Computadoras de escritorio"},
    ]

    for cat_data in categorias:
        categoria, creado = CategoriaProducto.objects.get_or_create(
            nombre=cat_data["nombre"],
            defaults=cat_data
        )
        if creado:
            print(f"✅ Categoría creada: {categoria.nombre}")
        else:
            print(f"ℹ️ Categoría ya existe: {categoria.nombre}")


def crear_productos():
    """Crear productos de prueba"""
    productos = [
        {
            "nombre_producto": "Laptop Lenovo ThinkPad",
            "codigo_sku": "LAP-001",
            "categoria": "Laptop",
            "marca": "Lenovo",
            "modelo_equipo": "ThinkPad E14",
            "procesador": "Intel Core i5",
            "memoria_ram": "8GB DDR4",
            "memoria_rom": "256GB SSD",
            "descripcion": "Laptop empresarial de alto rendimiento",
            "precio_compra": Decimal("800.00"),
            "precio_venta": Decimal("1099.99"),
            "stock_actual": 15,
            "disponible_web": True,
            "destacado": True,
        },
        {
            "nombre_producto": "Monitor 27\" 4K",
            "codigo_sku": "MON-001",
            "categoria": "Accesorio",
            "marca": "Samsung",
            "modelo_equipo": "UHD 27\"",
            "descripcion": "Monitor 4K para profesionales",
            "precio_compra": Decimal("250.00"),
            "precio_venta": Decimal("349.99"),
            "stock_actual": 8,
            "disponible_web": True,
        },
        {
            "nombre_producto": "Computadora All-in-One",
            "codigo_sku": "PC-001",
            "categoria": "Computadora",
            "marca": "HP",
            "modelo_equipo": "AiO 24\"",
            "procesador": "AMD Ryzen 5",
            "memoria_ram": "16GB DDR4",
            "memoria_rom": "512GB SSD",
            "descripcion": "Computadora todo en uno ideal para oficina",
            "precio_compra": Decimal("600.00"),
            "precio_venta": Decimal("799.99"),
            "stock_actual": 5,
            "disponible_web": True,
        },
        {
            "nombre_producto": "Mouse Inalámbrico",
            "codigo_sku": "MOU-001",
            "categoria": "Accesorio",
            "marca": "Logitech",
            "modelo_equipo": "MX Master 3",
            "descripcion": "Mouse ergonómico inalámbrico",
            "precio_compra": Decimal("20.00"),
            "precio_venta": Decimal("29.99"),
            "stock_actual": 25,
            "disponible_web": True,
        },
        {
            "nombre_producto": "Laptop ASUS VivoBook",
            "codigo_sku": "LAP-002",
            "categoria": "Laptop",
            "marca": "ASUS",
            "modelo_equipo": "VivoBook 15",
            "procesador": "Intel Core i7",
            "memoria_ram": "16GB DDR4",
            "memoria_rom": "512GB SSD",
            "descripcion": "Laptop de alto rendimiento para estudiantes y profesionales",
            "precio_compra": Decimal("650.00"),
            "precio_venta": Decimal("749.99"),
            "stock_actual": 12,
            "disponible_web": True,
            "destacado": True,
        }
    ]

    for prod_data in productos:
        # Obtener la categoría
        categoria_nombre = prod_data.pop("categoria")
        categoria = CategoriaProducto.objects.get(nombre=categoria_nombre)
        prod_data["categoria"] = categoria

        producto, creado = Producto.objects.get_or_create(
            codigo_sku=prod_data["codigo_sku"],
            defaults=prod_data
        )

        if creado:
            print(f"✅ Producto creado: {producto.nombre_producto}")
        else:
            print(f"ℹ️ Producto ya existe: {producto.nombre_producto}")


def main():
    print("🚀 Iniciando creación de productos de prueba...")

    try:
        crear_categorias()
        print("\n" + "="*50)
        crear_productos()
        print("\n✅ ¡Productos de prueba creados exitosamente!")

        # Mostrar resumen
        total_productos = Producto.objects.count()
        productos_web = Producto.objects.filter(disponible_web=True).count()
        print(f"\n📊 Resumen:")
        print(f"   Total de productos: {total_productos}")
        print(f"   Disponibles en web: {productos_web}")
        print(f"   Categorías: {CategoriaProducto.objects.count()}")

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
