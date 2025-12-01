#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script para inicializar datos de prueba del sistema"""

import os
import sys
import django

# Configurar Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from clientes.models import Cliente
from tecnicos.models import Tecnico
from productos.models import Producto

def crear_clientes():
    """Crear clientes de prueba"""
    clientes_prueba = [
        {
            'nombres': 'Juan Carlos',
            'apellidos': 'Perez Gonzalez',
            'numero_documento': '1234567890',
            'telefono': '+57 3201234567',
            'correo': 'juan.perez@example.com',
            'direccion': 'Calle 10 # 15-20, Duitama',
            'activo': True
        },
        {
            'nombres': 'Maria Fernanda',
            'apellidos': 'Rodriguez Lopez',
            'numero_documento': '9876543210',
            'telefono': '+57 3109876543',
            'correo': 'maria.rodriguez@example.com',
            'direccion': 'Carrera 5 # 8-30, Sogamoso',
            'activo': True
        },
        {
            'nombres': 'Carlos Alberto',
            'apellidos': 'Martinez Silva',
            'numero_documento': '5551234567',
            'telefono': '+57 3155551234',
            'correo': 'carlos.martinez@example.com',
            'direccion': 'Avenida Central # 25-10, Tunja',
            'activo': True
        },
        {
            'nombres': 'Laura Cristina',
            'apellidos': 'Gomez Ramirez',
            'numero_documento': '7778889990',
            'telefono': '+57 3207778889',
            'correo': 'laura.gomez@example.com',
            'direccion': 'Calle 20 # 12-45, Duitama',
            'activo': True
        },
        {
            'nombres': 'Andres Felipe',
            'apellidos': 'Torres Medina',
            'numero_documento': '4445556667',
            'telefono': '+57 3144445556',
            'correo': 'andres.torres@example.com',
            'direccion': 'Carrera 8 # 15-32, Paipa',
            'activo': False
        },
    ]

    print("\n" + "=" * 60)
    print("CREANDO CLIENTES DE PRUEBA")
    print("=" * 60)

    creados = 0
    existentes = 0

    for datos in clientes_prueba:
        try:
            if Cliente.objects.filter(numero_documento=datos['numero_documento']).exists():
                print(f"Cliente {datos['nombres']} {datos['apellidos']} ya existe")
                existentes += 1
            else:
                cliente = Cliente.objects.create(**datos)
                print(f"Cliente creado: {cliente.nombre_completo} - Doc: {cliente.numero_documento}")
                creados += 1
        except Exception as e:
            print(f"Error al crear {datos['nombres']}: {str(e)}")

    print(f"\nClientes creados: {creados}")
    print(f"Clientes existentes: {existentes}")
    print(f"Total clientes en BD: {Cliente.objects.count()}")
    print("=" * 60)

def crear_tecnicos():
    """Crear tecnicos de prueba"""
    tecnicos_prueba = [
        {
            'nombres': 'Pedro',
            'apellidos': 'Gutierrez',
            'numero_documento': '1001234567',
            'telefono': '+573101112233',
            'correo': 'pedro.gutierrez@digtsoft.com',
            'profesion': 'Reparacion de computadores',
            'activo': True
        },
        {
            'nombres': 'Sofia',
            'apellidos': 'Morales',
            'numero_documento': '1002345678',
            'telefono': '+573202223344',
            'correo': 'sofia.morales@digtsoft.com',
            'profesion': 'Mantenimiento preventivo',
            'activo': True
        },
        {
            'nombres': 'Miguel',
            'apellidos': 'Vargas',
            'numero_documento': '1003456789',
            'telefono': '+573153334455',
            'correo': 'miguel.vargas@digtsoft.com',
            'profesion': 'Redes y telecomunicaciones',
            'activo': True
        },
    ]

    print("\n" + "=" * 60)
    print("CREANDO TECNICOS DE PRUEBA")
    print("=" * 60)

    creados = 0
    existentes = 0

    for datos in tecnicos_prueba:
        try:
            if Tecnico.objects.filter(numero_documento=datos['numero_documento']).exists():
                print(f"Tecnico {datos['nombres']} {datos['apellidos']} ya existe")
                existentes += 1
            else:
                tecnico = Tecnico.objects.create(**datos)
                print(f"Tecnico creado: {tecnico.nombre_completo} - Doc: {tecnico.numero_documento}")
                creados += 1
        except Exception as e:
            print(f"Error al crear {datos['nombres']}: {str(e)}")

    print(f"\nTecnicos creados: {creados}")
    print(f"Tecnicos existentes: {existentes}")
    print(f"Total tecnicos en BD: {Tecnico.objects.count()}")
    print("=" * 60)

def crear_productos():
    """Crear productos de prueba"""
    from productos.models import CategoriaProducto

    # Crear categorías primero
    cat_computadores, _ = CategoriaProducto.objects.get_or_create(
        nombre='Computadores',
        defaults={'descripcion': 'Computadores y laptops', 'activo': True}
    )
    cat_accesorios, _ = CategoriaProducto.objects.get_or_create(
        nombre='Accesorios',
        defaults={'descripcion': 'Accesorios de computacion', 'activo': True}
    )

    productos_prueba = [
        {
            'nombre_producto': 'Laptop HP Pavilion',
            'codigo_sku': 'LAP-HP-001',
            'descripcion': 'Laptop HP Pavilion 15.6 pulgadas',
            'marca': 'HP',
            'modelo_equipo': 'Pavilion 15-eh2000',
            'procesador': 'Intel Core i5-1235U',
            'memoria_ram': '8GB DDR4',
            'memoria_rom': '512GB SSD',
            'precio_compra': 1500000,
            'precio_venta': 1800000,
            'precio_mayorista': 1650000,
            'stock_actual': 10,
            'stock_minimo': 3,
            'stock_maximo': 50,
            'categoria': cat_computadores,
            'disponible_web': True,
            'destacado': True,
            'activo': True
        },
        {
            'nombre_producto': 'Mouse Logitech',
            'codigo_sku': 'MOU-LOG-001',
            'descripcion': 'Mouse inalambrico Logitech',
            'marca': 'Logitech',
            'modelo_equipo': 'M185',
            'precio_compra': 50000,
            'precio_venta': 75000,
            'precio_mayorista': 60000,
            if Producto.objects.filter(codigo_sku=datos['codigo_sku']).exists():
                print(f"Producto {datos['nombre_producto']} ya existe")
            'stock_maximo': 100,
            'categoria': cat_accesorios,
            'disponible_web': True,
                print(f"Producto creado: {producto.nombre_producto} - Codigo: {producto.codigo_sku}")
        },
        {
            print(f"Error al crear {datos['nombre_producto']}: {str(e)}")
            'codigo_sku': 'TEC-MEC-001',
            'descripcion': 'Teclado mecanico RGB',
            'marca': 'Redragon',
            'modelo_equipo': 'K552',
            'precio_compra': 150000,
            'precio_venta': 200000,
            'precio_mayorista': 175000,
            'stock_actual': 15,
            'stock_minimo': 5,
            'stock_maximo': 50,
            'categoria': cat_accesorios,
            'disponible_web': True,
            'destacado': True,
            'activo': True
        },
    ]

    print("\n" + "=" * 60)
    print("CREANDO PRODUCTOS DE PRUEBA")
    print("=" * 60)

    creados = 0
    existentes = 0

    for datos in productos_prueba:
        try:
            if Producto.objects.filter(codigo=datos['codigo']).exists():
                print(f"Producto {datos['nombre']} ya existe")
                existentes += 1
            else:
                producto = Producto.objects.create(**datos)
                print(f"Producto creado: {producto.nombre} - Codigo: {producto.codigo}")
                creados += 1
        except Exception as e:
            print(f"Error al crear {datos['nombre']}: {str(e)}")

    print(f"\nProductos creados: {creados}")
    print(f"Productos existentes: {existentes}")
    print(f"Total productos en BD: {Producto.objects.count()}")
    print("=" * 60)

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("INICIALIZANDO DATOS DE PRUEBA - DIGT SOFT")
    print("=" * 60)

    crear_clientes()
    crear_tecnicos()
    crear_productos()

    print("\n" + "=" * 60)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print("=" * 60)
    print("\nPuedes acceder al sistema con:")
    print("  Usuario: admin")
    print("  Contrasena: admin123")
    print("\nURL: http://127.0.0.1:8000/admin/")
    print("=" * 60 + "\n")

