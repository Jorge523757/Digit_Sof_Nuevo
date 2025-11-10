"""
DIGT SOFT - Script de Configuracion Completa del Sistema
Este script configura todos los modulos con tablas dinamicas
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from productos.models import CategoriaProducto, Producto
from clientes.models import Cliente

def crear_categorias():
    print("=" * 60)
    print("CREANDO CATEGORIAS DE PRODUCTOS")
    print("=" * 60)
    
    categorias = [
        ('Laptops', 'Computadoras portatiles'),
        ('Computadoras', 'PCs de escritorio'),
        ('Componentes', 'Partes de PC'),
        ('Perifericos', 'Mouse, teclados, etc'),
        ('Redes', 'Routers, switches'),
        ('Almacenamiento', 'Discos, SSDs'),
    ]
    
    for nombre, desc in categorias:
        cat, created = CategoriaProducto.objects.get_or_create(
            nombre=nombre,
            defaults={'descripcion': desc}
        )
        if created:
            print(f"Categoria creada: {nombre}")
        else:
            print(f"Categoria existe: {nombre}")


def crear_productos():
    print("\n" + "=" * 60)
    print("CREANDO PRODUCTOS DE DEMOSTRACION")
    print("=" * 60)
    
    cat_laptops = CategoriaProducto.objects.filter(nombre='Laptops').first()
    
    productos = [
        {
            'nombre_producto': 'Laptop Dell Inspiron 15',
            'codigo_sku': 'DELL-001',
            'categoria': cat_laptops,
            'marca': 'Dell',
            'precio_compra': 450.00,
            'precio_venta': 599.00,
            'descripcion': 'Laptop Dell Inspiron',
            'stock_actual': 10,
        },
        {
            'nombre_producto': 'Laptop HP Pavilion',
            'codigo_sku': 'HP-001',
            'categoria': cat_laptops,
            'marca': 'HP',
            'precio_compra': 500.00,
            'precio_venta': 650.00,
            'descripcion': 'Laptop HP Pavilion',
            'stock_actual': 8,
        },
    ]
    
    for data in productos:
        prod, created = Producto.objects.get_or_create(
            codigo_sku=data['codigo_sku'],
            defaults=data
        )
        if created:
            print(f"Producto creado: {data['nombre_producto']}")
        else:
            print(f"Producto existe: {data['nombre_producto']}")


def mostrar_resumen():
    print("\n" + "=" * 60)
    print("RESUMEN DEL SISTEMA")
    print("=" * 60)
    print(f"Usuarios: {User.objects.count()}")
    print(f"Productos: {Producto.objects.count()}")
    print(f"Categorias: {CategoriaProducto.objects.count()}")
    print(f"Clientes: {Cliente.objects.count()}")
    print("\nSistema configurado correctamente!")


if __name__ == '__main__':
    try:
        print("\nConfigurando sistema DIGT SOFT...\n")
        crear_categorias()
        crear_productos()
        mostrar_resumen()
    except Exception as e:
        print(f"Error: {e}")

