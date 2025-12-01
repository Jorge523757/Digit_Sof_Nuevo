"""
DIGT SOFT - Script para crear datos de prueba rápidos
Ejecutar: python agregar_datos_prueba_rapido.py
"""

import os
import django
from datetime import datetime, timedelta
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from clientes.models import Cliente
from tecnicos.models import Tecnico
from productos.models import Producto, CategoriaProducto
from proveedores.models import Proveedor

print("=" * 60)
print("   CREANDO DATOS DE PRUEBA")
print("=" * 60)

# 1. CLIENTES
print("\n[1/4] Creando Clientes...")
clientes_data = [
    {
        "nombres": "Juan Carlos",
        "apellidos": "Pérez González",
        "numero_documento": "1234567890",
        "correo": "juan.perez@email.com",
        "telefono": "3001234567",
        "direccion": "Calle 123 #45-67, Bogotá",
        "activo": True
    },
    {
        "nombres": "María Fernanda",
        "apellidos": "Rodríguez López",
        "numero_documento": "9876543210",
        "correo": "maria.rodriguez@email.com",
        "telefono": "3109876543",
        "direccion": "Carrera 45 #12-34, Medellín",
        "activo": True
    },
    {
        "nombres": "Carlos Alberto",
        "apellidos": "Martínez Silva",
        "numero_documento": "5551234567",
        "correo": "carlos.martinez@email.com",
        "telefono": "3205551234",
        "direccion": "Avenida 67 #89-01, Cali",
        "activo": True
    },
    {
        "nombres": "Ana Patricia",
        "apellidos": "Gómez Torres",
        "numero_documento": "7778889990",
        "correo": "ana.gomez@email.com",
        "telefono": "3157778888",
        "direccion": "Diagonal 22 #33-44, Barranquilla",
        "activo": True
    },
    {
        "nombres": "Luis Fernando",
        "apellidos": "Sánchez Ruiz",
        "numero_documento": "1112223334",
        "correo": "luis.sanchez@email.com",
        "telefono": "3001112222",
        "direccion": "Calle 89 #12-23, Cartagena",
        "activo": True
    },
    {
        "nombres": "Diana Carolina",
        "apellidos": "López Vargas",
        "numero_documento": "4445556667",
        "correo": "diana.lopez@email.com",
        "telefono": "3104445555",
        "direccion": "Carrera 34 #56-78, Bucaramanga",
        "activo": False
    },
    {
        "nombres": "Jorge Andrés",
        "apellidos": "Ramírez Castro",
        "numero_documento": "8889990001",
        "correo": "jorge.ramirez@email.com",
        "telefono": "3208889999",
        "direccion": "Avenida 12 #34-56, Pereira",
        "activo": True
    },
    {
        "nombres": "Sandra Milena",
        "apellidos": "Hernández Díaz",
        "numero_documento": "3334445556",
        "correo": "sandra.hernandez@email.com",
        "telefono": "3153334444",
        "direccion": "Calle 45 #67-89, Manizales",
        "activo": True
    },
]

for data in clientes_data:
    try:
        cliente, created = Cliente.objects.get_or_create(
            numero_documento=data['numero_documento'],
            defaults=data
        )
        if created:
            print(f"   ✓ Cliente creado: {cliente.nombre_completo}")
        else:
            print(f"   → Cliente existente: {cliente.nombre_completo}")
    except Exception as e:
        print(f"   ✗ Error al crear cliente: {e}")

print(f"\n   Total de clientes: {Cliente.objects.count()}")

# 2. TÉCNICOS
print("\n[2/4] Creando Técnicos...")
tecnicos_data = [
    {
        "nombres": "Pedro",
        "apellidos": "Gutiérrez Moreno",
        "numero_documento": "1001234567",
        "correo": "pedro.gutierrez@digtsoft.com",
        "telefono": "3001112233",
        "profesion": "Ingeniero en Sistemas",
        "activo": True
    },
    {
        "nombres": "Sofía",
        "apellidos": "Morales Rincón",
        "numero_documento": "1002345678",
        "correo": "sofia.morales@digtsoft.com",
        "telefono": "3102223344",
        "profesion": "Técnico en Electrónica",
        "activo": True
    },
    {
        "nombres": "Andrés",
        "apellidos": "Velásquez Ortiz",
        "numero_documento": "1003456789",
        "correo": "andres.velasquez@digtsoft.com",
        "telefono": "3203334455",
        "profesion": "Ingeniero Electrónico",
        "activo": True
    },
    {
        "nombres": "Carolina",
        "apellidos": "Jiménez Parra",
        "numero_documento": "1004567890",
        "correo": "carolina.jimenez@digtsoft.com",
        "telefono": "3154445566",
        "profesion": "Técnico en Redes",
        "activo": True
    },
    {
        "nombres": "Miguel Ángel",
        "apellidos": "Rojas Soto",
        "numero_documento": "1005678901",
        "correo": "miguel.rojas@digtsoft.com",
        "telefono": "3005556677",
        "profesion": "Ingeniero de Software",
        "activo": False
    },
]

for data in tecnicos_data:
    try:
        tecnico, created = Tecnico.objects.get_or_create(
            numero_documento=data['numero_documento'],
            defaults=data
        )
        if created:
            print(f"   ✓ Técnico creado: {tecnico.nombres} {tecnico.apellidos}")
        else:
            print(f"   → Técnico existente: {tecnico.nombres} {tecnico.apellidos}")
    except Exception as e:
        print(f"   ✗ Error al crear técnico: {e}")

print(f"\n   Total de técnicos: {Tecnico.objects.count()}")

# 3. CATEGORÍAS Y PRODUCTOS
print("\n[3/4] Creando Productos...")

# Categorías
cat_electronica, _ = CategoriaProducto.objects.get_or_create(
    nombre="Electrónica",
    defaults={"descripcion": "Productos electrónicos y computadores"}
)
cat_accesorios, _ = CategoriaProducto.objects.get_or_create(
    nombre="Accesorios",
    defaults={"descripcion": "Accesorios de computador y periféricos"}
)
cat_componentes, _ = CategoriaProducto.objects.get_or_create(
    nombre="Componentes",
    defaults={"descripcion": "Componentes internos de computador"}
)

productos_data = [
    {
        "nombre_producto": "Laptop HP Pavilion 15",
        "codigo_sku": "LAP-HP-001",
        "categoria": cat_electronica,
        "precio_venta": Decimal("1800000"),
        "precio_compra": Decimal("1500000"),
        "stock_actual": 10,
        "stock_minimo": 2,
        "descripcion": "Laptop HP Pavilion 15, Intel Core i5, 8GB RAM, 256GB SSD"
    },
    {
        "nombre_producto": "Mouse Logitech MX Master 3",
        "codigo_sku": "MOU-LOG-001",
        "categoria": cat_accesorios,
        "precio_venta": Decimal("180000"),
        "precio_compra": Decimal("120000"),
        "stock_actual": 25,
        "stock_minimo": 5,
        "descripcion": "Mouse inalámbrico Logitech MX Master 3, ergonómico"
    },
    {
        "nombre_producto": "Teclado Mecánico Corsair K70",
        "codigo_sku": "TEC-COR-001",
        "categoria": cat_accesorios,
        "precio_venta": Decimal("350000"),
        "precio_compra": Decimal("250000"),
        "stock_actual": 15,
        "stock_minimo": 3,
        "descripcion": "Teclado mecánico RGB Corsair K70, switches Cherry MX"
    },
    {
        "nombre_producto": "Monitor LG 27 pulgadas 4K",
        "codigo_sku": "MON-LG-001",
        "categoria": cat_electronica,
        "precio_venta": Decimal("900000"),
        "precio_compra": Decimal("700000"),
        "stock_actual": 8,
        "stock_minimo": 2,
        "descripcion": "Monitor LG 27 pulgadas, resolución 4K UHD, IPS"
    },
    {
        "nombre_producto": "Impresora HP LaserJet Pro",
        "codigo_sku": "IMP-HP-001",
        "categoria": cat_electronica,
        "precio_venta": Decimal("1200000"),
        "precio_compra": Decimal("950000"),
        "stock_actual": 5,
        "stock_minimo": 1,
        "descripcion": "Impresora láser HP LaserJet Pro, WiFi, dúplex automático"
    },
    {
        "nombre_producto": "Memoria RAM Kingston 16GB DDR4",
        "codigo_sku": "RAM-KIN-001",
        "categoria": cat_componentes,
        "precio_venta": Decimal("280000"),
        "precio_compra": Decimal("200000"),
        "stock_actual": 30,
        "stock_minimo": 10,
        "descripcion": "Memoria RAM Kingston 16GB DDR4 3200MHz"
    },
    {
        "nombre_producto": "SSD Samsung 1TB NVMe",
        "codigo_sku": "SSD-SAM-001",
        "categoria": cat_componentes,
        "precio_venta": Decimal("420000"),
        "precio_compra": Decimal("320000"),
        "stock_actual": 20,
        "stock_minimo": 5,
        "descripcion": "Disco SSD Samsung 1TB NVMe M.2, lectura 3500MB/s"
    },
    {
        "nombre_producto": "Webcam Logitech C920",
        "codigo_sku": "WEB-LOG-001",
        "categoria": cat_accesorios,
        "precio_venta": Decimal("250000"),
        "precio_compra": Decimal("180000"),
        "stock_actual": 12,
        "stock_minimo": 3,
        "descripcion": "Webcam Logitech C920 Full HD 1080p, micrófono integrado"
    },
]

for data in productos_data:
    try:
        producto, created = Producto.objects.get_or_create(
            codigo_sku=data['codigo_sku'],
            defaults=data
        )
        if created:
            print(f"   ✓ Producto creado: {producto.nombre_producto}")
        else:
            print(f"   → Producto existente: {producto.nombre_producto}")
    except Exception as e:
        print(f"   ✗ Error al crear producto: {e}")

print(f"\n   Total de productos: {Producto.objects.count()}")

# 4. PROVEEDORES
print("\n[4/4] Creando Proveedores...")
proveedores_data = [
    {
        "nombre_empresa": "Tecnología Global S.A.",
        "nit": "900123456-7",
        "nombre_contacto": "Roberto García Martínez",
        "email": "ventas@tecnologiaglobal.com",
        "telefono": "6013334455",
        "direccion": "Calle 100 #15-20, Bogotá",
        "calificacion": 5,
        "activo": True
    },
    {
        "nombre_empresa": "Distribuciones TechMax Ltda",
        "nit": "800234567-8",
        "nombre_contacto": "Ana Martínez López",
        "email": "contacto@techmax.com",
        "telefono": "6015556677",
        "direccion": "Carrera 50 #45-30, Medellín",
        "calificacion": 4,
        "activo": True
    },
    {
        "nombre_empresa": "Importaciones Digitales S.A.S",
        "nit": "700345678-9",
        "nombre_contacto": "Luis Fernández Castro",
        "email": "info@importacionesdigitales.com",
        "telefono": "6017778899",
        "direccion": "Avenida 5N #24-50, Cali",
        "calificacion": 5,
        "activo": True
    },
    {
        "nombre_empresa": "Suministros Tecnológicos del Caribe",
        "nit": "600456789-0",
        "nombre_contacto": "María Elena Pérez",
        "email": "ventas@sumintechcaribe.com",
        "telefono": "6059990011",
        "direccion": "Calle 72 #54-23, Barranquilla",
        "calificacion": 4,
        "activo": True
    },
]

for data in proveedores_data:
    try:
        proveedor, created = Proveedor.objects.get_or_create(
            nit=data['nit'],
            defaults=data
        )
        if created:
            print(f"   ✓ Proveedor creado: {proveedor.nombre_empresa}")
        else:
            print(f"   → Proveedor existente: {proveedor.nombre_empresa}")
    except Exception as e:
        print(f"   ✗ Error al crear proveedor: {e}")

print(f"\n   Total de proveedores: {Proveedor.objects.count()}")

# RESUMEN FINAL
print("\n" + "=" * 60)
print("   RESUMEN DE DATOS CREADOS")
print("=" * 60)
print(f"   📋 Clientes:     {Cliente.objects.count()}")
print(f"   👷 Técnicos:     {Tecnico.objects.count()}")
print(f"   📦 Productos:    {Producto.objects.count()}")
print(f"   🏢 Proveedores:  {Proveedor.objects.count()}")
print("=" * 60)
print("   ✅ DATOS DE PRUEBA CREADOS EXITOSAMENTE")
print("=" * 60)

