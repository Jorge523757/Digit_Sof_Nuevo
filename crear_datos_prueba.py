#!/usr/bin/env python
"""
Script para crear datos de prueba en la base de datos
"""
import os
import django
import sys
from datetime import date, datetime
from decimal import Decimal

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitsoft_project.settings')
django.setup()

from main.models import (
    Cliente, Proveedor, Tecnico, Administrador, Marca, 
    Producto, Equipo, OrdenServicio, ServicioTecnico, 
    Ventas, ComprasMercancia, Garantias, Facturacion
)

def crear_datos_prueba():
    print("Creando datos de prueba...")
    
    # Crear Marcas
    marcas_data = [
        {'marca': 'HP', 'descripcion': 'Hewlett-Packard - Equipos de computación'},
        {'marca': 'Dell', 'descripcion': 'Dell Technologies - Computadores y servidores'},
        {'marca': 'Lenovo', 'descripcion': 'Lenovo - Laptops y equipos de oficina'},
        {'marca': 'Canon', 'descripcion': 'Canon - Impresoras y equipos de imagen'},
        {'marca': 'Epson', 'descripcion': 'Epson - Impresoras y proyectores'},
    ]
    
    marcas = []
    for marca_info in marcas_data:
        marca, created = Marca.objects.get_or_create(
            marca=marca_info['marca'],
            defaults={'descripcion': marca_info['descripcion']}
        )
        marcas.append(marca)
        if created:
            print(f"  ✓ Marca creada: {marca.marca}")
    
    # Crear Administradores
    admin_data = [
        {'nombre': 'Juan Pérez', 'contraseña': 'admin123', 'correo_electronico': 'admin@digitsoft.com'},
        {'nombre': 'María García', 'contraseña': 'admin456', 'correo_electronico': 'maria@digitsoft.com'},
    ]
    
    administradores = []
    for admin_info in admin_data:
        admin, created = Administrador.objects.get_or_create(
            correo_electronico=admin_info['correo_electronico'],
            defaults={
                'nombre': admin_info['nombre'],
                'contraseña': admin_info['contraseña']
            }
        )
        administradores.append(admin)
        if created:
            print(f"  ✓ Administrador creado: {admin.nombre}")
    
    # Crear Clientes
    clientes_data = [
        {
            'nombre': 'Carlos Mendoza',
            'numero_documento': '12345678',
            'numero_telefono': '3001234567',
            'correoElectronico': 'carlos@email.com',
            'direccion': 'Calle 123 #45-67'
        },
        {
            'nombre': 'Ana Rodríguez',
            'numero_documento': '87654321',
            'numero_telefono': '3007654321',
            'correoElectronico': 'ana@email.com',
            'direccion': 'Carrera 89 #12-34'
        },
        {
            'nombre': 'Luis Martínez',
            'numero_documento': '11223344',
            'numero_telefono': '3009876543',
            'correoElectronico': 'luis@email.com',
            'direccion': 'Avenida 56 #78-90'
        }
    ]
    
    clientes = []
    for cliente_info in clientes_data:
        cliente, created = Cliente.objects.get_or_create(
            numero_documento=cliente_info['numero_documento'],
            defaults=cliente_info
        )
        clientes.append(cliente)
        if created:
            print(f"  ✓ Cliente creado: {cliente.nombre}")
    
    # Crear Proveedores
    proveedores_data = [
        {
            'nit_proveedor': '900123456-1',
            'nombre': 'TecnoSupplies Ltda',
            'cedula': '12345678',
            'direccion': 'Zona Industrial 123',
            'telefono': '6012345678'
        },
        {
            'nit_proveedor': '900654321-2',
            'nombre': 'CompuWorld S.A.S',
            'cedula': '87654321',
            'direccion': 'Centro Comercial Tech',
            'telefono': '6018765432'
        }
    ]
    
    proveedores = []
    for proveedor_info in proveedores_data:
        proveedor, created = Proveedor.objects.get_or_create(
            nit_proveedor=proveedor_info['nit_proveedor'],
            defaults=proveedor_info
        )
        proveedores.append(proveedor)
        if created:
            print(f"  ✓ Proveedor creado: {proveedor.nombre}")
    
    # Crear Técnicos
    tecnicos_data = [
        {
            'nombre_completo': 'Roberto Silva',
            'numero_documento': '33445566',
            'cedula': '33445566',
            'correo': 'roberto@digitsoft.com',
            'direccion': 'Calle 45 #12-23',
            'especialidad': 'Reparación de Hardware',
            'tipo_tecnico': 'Senior'
        },
        {
            'nombre_completo': 'Sandra López',
            'numero_documento': '77889900',
            'cedula': '77889900',
            'correo': 'sandra@digitsoft.com',
            'direccion': 'Carrera 67 #89-01',
            'especialidad': 'Mantenimiento de Software',
            'tipo_tecnico': 'Junior'
        }
    ]
    
    tecnicos = []
    for tecnico_info in tecnicos_data:
        tecnico, created = Tecnico.objects.get_or_create(
            numero_documento=tecnico_info['numero_documento'],
            defaults=tecnico_info
        )
        tecnicos.append(tecnico)
        if created:
            print(f"  ✓ Técnico creado: {tecnico.nombre_completo}")
    
    # Crear Productos
    productos_data = [
        {
            'nombreProducto': 'Laptop HP Pavilion',
            'modelo_producto': 'HP-PAV-15-2024',
            'cantidad': 15,
            'valor_producto': '2500000',
            'diseño': 'Color Plata',
            'marca': marcas[0]  # HP
        },
        {
            'nombreProducto': 'Impresora Canon',
            'modelo_producto': 'PIXMA-G3020',
            'cantidad': 8,
            'valor_producto': '650000',
            'diseño': 'Multifuncional',
            'marca': marcas[3]  # Canon
        },
        {
            'nombreProducto': 'Desktop Dell OptiPlex',
            'modelo_producto': 'DELL-OPT-3080',
            'cantidad': 5,
            'valor_producto': '1800000',
            'diseño': 'Torre Mini',
            'marca': marcas[1]  # Dell
        }
    ]
    
    productos = []
    for producto_info in productos_data:
        producto, created = Producto.objects.get_or_create(
            modelo_producto=producto_info['modelo_producto'],
            defaults=producto_info
        )
        productos.append(producto)
        if created:
            print(f"  ✓ Producto creado: {producto.nombreProducto}")
    
    # Crear Órdenes de Servicio
    ordenes_data = [
        {
            'cliente': clientes[0],
            'tecnico': tecnicos[0],
            'descripcion_orden': 'Mantenimiento preventivo de laptop empresarial',
            'estado': 'Pendiente'
        },
        {
            'cliente': clientes[1],
            'tecnico': tecnicos[1],
            'descripcion_orden': 'Instalación de software contable',
            'estado': 'Completada'
        },
        {
            'cliente': clientes[2],
            'tecnico': tecnicos[0],
            'descripcion_orden': 'Reparación de impresora Canon',
            'estado': 'Pendiente'
        }
    ]
    
    ordenes = []
    for orden_info in ordenes_data:
        orden = OrdenServicio.objects.create(**orden_info)
        ordenes.append(orden)
        print(f"  ✓ Orden de servicio creada: #{orden.id_ordenServicio}")
    
    # Crear Compras de Mercancía
    compras_data = [
        {
            'producto': productos[0],
            'cantidad_comprada': 10,
            'fecha_compra': date(2024, 9, 15),
            'proveedor': proveedores[0],
            'administrador': administradores[0],
            'precio_compra': '2300000'
        },
        {
            'producto': productos[1],
            'cantidad_comprada': 5,
            'fecha_compra': date(2024, 9, 20),
            'proveedor': proveedores[1],
            'administrador': administradores[1],
            'precio_compra': '600000'
        }
    ]
    
    compras = []
    for compra_info in compras_data:
        compra = ComprasMercancia.objects.create(**compra_info)
        compras.append(compra)
        print(f"  ✓ Compra creada: #{compra.id_compra}")
    
    # Crear Ventas
    ventas_data = [
        {
            'cliente': clientes[0],
            'producto': productos[0],
            'cantidad_vendidas': 2,
            'valor_venta': Decimal('5000000')
        },
        {
            'cliente': clientes[1],
            'producto': productos[1],
            'cantidad_vendidas': 1,
            'valor_venta': Decimal('650000')
        }
    ]
    
    ventas = []
    for venta_info in ventas_data:
        venta = Ventas.objects.create(**venta_info)
        ventas.append(venta)
        print(f"  ✓ Venta creada: #{venta.id_venta}")
    
    # Crear Servicios Técnicos
    for i, orden in enumerate(ordenes[:2]):
        servicio = ServicioTecnico.objects.create(
            cliente=orden.cliente,
            tecnico=orden.tecnico,
            orden_servicio=orden
        )
        print(f"  ✓ Servicio técnico creado: #{servicio.id_servicio_tecnico}")
    
    print(f"\n✅ Datos de prueba creados exitosamente!")
    print(f"📊 Resumen:")
    print(f"   - {Marca.objects.count()} marcas")
    print(f"   - {Cliente.objects.count()} clientes")
    print(f"   - {Proveedor.objects.count()} proveedores")
    print(f"   - {Tecnico.objects.count()} técnicos")
    print(f"   - {Administrador.objects.count()} administradores")
    print(f"   - {Producto.objects.count()} productos")
    print(f"   - {OrdenServicio.objects.count()} órdenes de servicio")
    print(f"   - {ComprasMercancia.objects.count()} compras")
    print(f"   - {Ventas.objects.count()} ventas")
    print(f"   - {ServicioTecnico.objects.count()} servicios técnicos")

if __name__ == '__main__':
    crear_datos_prueba()