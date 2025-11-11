"""
Script Simple para Agregar Datos de Prueba
Ejecutar: python agregar_datos_rapido.py
"""

import os
import django
from datetime import datetime, timedelta
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto
from ventas.models import Venta, DetalleVenta
from facturacion.models import Factura
from capacitaciones.models import Capacitacion
from equipos.models import Equipo
from clientes.models import Cliente

print("=" * 60)
print("   AGREGANDO DATOS DE PRUEBA RÁPIDO")
print("=" * 60)

# 1. PRODUCTOS (LO MÁS IMPORTANTE)
print("\n[1/5] Creando Productos...")
if Producto.objects.count() == 0:
    cat, _ = CategoriaProducto.objects.get_or_create(
        nombre="Electrónica",
        defaults={"descripcion": "Productos electrónicos"}
    )

    productos = [
        Producto(
            nombre_producto="Laptop HP Pavilion 15",
            codigo_sku="LAP-HP-001",
            categoria=cat,
            precio_venta=Decimal("1800000"),
            precio_compra=Decimal("1500000"),
            stock_actual=10,
            stock_minimo=2
        ),
        Producto(
            nombre_producto="Mouse Logitech MX Master",
            codigo_sku="MOU-LOG-001",
            categoria=cat,
            precio_venta=Decimal("180000"),
            precio_compra=Decimal("120000"),
            stock_actual=25,
            stock_minimo=5
        ),
        Producto(
            nombre_producto="Teclado Mecánico Corsair",
            codigo_sku="TEC-COR-001",
            categoria=cat,
            precio_venta=Decimal("350000"),
            precio_compra=Decimal("250000"),
            stock_actual=15,
            stock_minimo=3
        ),
    ]
    Producto.objects.bulk_create(productos)
    print(f"   ✓ {Producto.objects.count()} productos creados")
else:
    print(f"   ✓ Ya existen {Producto.objects.count()} productos")

# 2. VENTAS
print("\n[2/5] Creando Ventas...")
if Venta.objects.count() == 0 and Cliente.objects.exists() and Producto.objects.exists():
    cliente = Cliente.objects.first()
    producto = Producto.objects.first()

    venta = Venta.objects.create(
        cliente=cliente,
        estado='COMPLETADA',
        canal_venta='TIENDA',
        metodo_pago='EFECTIVO',
        pagado=True,
        vendedor="Vendedor Demo"
    )

    DetalleVenta.objects.create(
        venta=venta,
        producto=producto,
        cantidad=1,
        precio_unitario=producto.precio_venta,
        con_garantia=True
    )

    venta.calcular_totales()
    print(f"   ✓ 1 venta creada: {venta.numero_venta}")
else:
    print(f"   ✓ Ya existen {Venta.objects.count()} ventas")

# 3. FACTURAS
print("\n[3/5] Creando Facturas...")
if Factura.objects.count() == 0 and Cliente.objects.exists():
    cliente = Cliente.objects.first()

    Factura.objects.create(
        cliente=cliente,
        tipo_factura='VENTA',
        estado='EMITIDA',
        subtotal=Decimal("1800000"),
        iva=Decimal("342000"),
        total=Decimal("2142000")
    )
    print(f"   ✓ 1 factura creada")
else:
    print(f"   ✓ Ya existen {Factura.objects.count()} facturas")

# 4. CAPACITACIONES
print("\n[4/5] Creando Capacitaciones...")
if Capacitacion.objects.count() == 0:
    fecha_inicio = datetime.now().date() + timedelta(days=7)
    fecha_fin = fecha_inicio + timedelta(days=2)

    Capacitacion.objects.create(
        nombre="Reparación de Laptops Modernas",
        tipo="TECNICA",
        instructor="Ing. Roberto Sánchez",
        descripcion="Curso avanzado de reparación de laptops",
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        duracion_horas=16,
        lugar="Centro de Capacitación DIGT SOFT",
        modalidad="PRESENCIAL",
        estado="PROGRAMADA",
        cupo_maximo=15,
        costo=Decimal("500000")
    )
    print(f"   ✓ 1 capacitación creada")
else:
    print(f"   ✓ Ya existen {Capacitacion.objects.count()} capacitaciones")

# 5. EQUIPOS
print("\n[5/5] Creando Equipos...")
if Equipo.objects.count() == 0:
    Equipo.objects.create(
        nombre="Laptop HP ProBook 450",
        tipo_equipo="LAPTOP",
        marca="HP",
        modelo="ProBook 450 G8",
        numero_serie="HP2021001",
        fecha_adquisicion=datetime.now().date(),
        valor_adquisicion=Decimal("2500000"),
        estado="OPERATIVO",
        ubicacion="Oficina Principal"
    )
    print(f"   ✓ 1 equipo creado")
else:
    print(f"   ✓ Ya existen {Equipo.objects.count()} equipos")

print("\n" + "=" * 60)
print("   ✅ DATOS CREADOS EXITOSAMENTE")
print("=" * 60)
print(f"\nRESUMEN:")
print(f"  • Productos: {Producto.objects.count()}")
print(f"  • Ventas: {Venta.objects.count()}")
print(f"  • Facturas: {Factura.objects.count()}")
print(f"  • Capacitaciones: {Capacitacion.objects.count()}")
print(f"  • Equipos: {Equipo.objects.count()}")
print(f"\n¡Refresca tu navegador para ver los cambios!")
print("=" * 60)

