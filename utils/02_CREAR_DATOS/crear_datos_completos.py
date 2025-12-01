"""
DIGT SOFT - Script para crear datos de prueba profesionales
Ejecutar: python crear_datos_completos.py
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
from ventas.models import Venta, DetalleVenta
from ordenes.models import OrdenServicio
from compras.models import Compra, DetalleCompra
from facturacion.models import Factura
from equipos.models import Equipo
from capacitaciones.models import Capacitacion, ParticipanteCapacitacion
from garantias.models import Garantia

print("=" * 60)
print("   CREANDO DATOS DE PRUEBA PROFESIONALES")
print("=" * 60)

# 1. VERIFICAR Y CREAR CLIENTES
print("\n[1/10] Verificando Clientes...")
if Cliente.objects.count() < 5:
    clientes_data = [
        {"nombres": "Juan Carlos", "apellidos": "Pérez González", "tipo_documento": "CC", "numero_documento": "1234567890", "email": "juan.perez@email.com", "telefono": "3001234567", "direccion": "Calle 123 #45-67", "ciudad": "Bogotá"},
        {"nombres": "María Fernanda", "apellidos": "Rodríguez López", "tipo_documento": "CC", "numero_documento": "9876543210", "email": "maria.rodriguez@email.com", "telefono": "3109876543", "direccion": "Carrera 45 #12-34", "ciudad": "Medellín"},
        {"nombres": "Carlos Alberto", "apellidos": "Martínez Silva", "tipo_documento": "CC", "numero_documento": "5551234567", "email": "carlos.martinez@email.com", "telefono": "3205551234", "direccion": "Avenida 67 #89-01", "ciudad": "Cali"},
    ]
    for data in clientes_data:
        Cliente.objects.get_or_create(numero_documento=data['numero_documento'], defaults=data)
    print(f"   ✓ {Cliente.objects.count()} clientes creados")
else:
    print(f"   ✓ Ya existen {Cliente.objects.count()} clientes")

# 2. VERIFICAR Y CREAR TÉCNICOS
print("\n[2/10] Verificando Técnicos...")
if Tecnico.objects.count() < 3:
    tecnicos_data = [
        {"nombres": "Pedro", "apellidos": "Gutiérrez", "numero_documento": "1001234567", "correo": "pedro.gutierrez@digtsoft.com", "telefono": "3001112233", "profesion": "Ingeniero en Sistemas", "activo": True},
        {"nombres": "Sofía", "apellidos": "Morales", "numero_documento": "1002345678", "correo": "sofia.morales@digtsoft.com", "telefono": "3102223344", "profesion": "Técnico en Electrónica", "activo": True},
    ]
    for data in tecnicos_data:
        try:
            Tecnico.objects.get_or_create(numero_documento=data['numero_documento'], defaults=data)
        except:
            pass
    print(f"   ✓ {Tecnico.objects.count()} técnicos creados")
else:
    print(f"   ✓ Ya existen {Tecnico.objects.count()} técnicos")

# 3. CREAR CATEGORÍAS Y PRODUCTOS
print("\n[3/10] Verificando Productos...")
if Producto.objects.count() < 5:
    cat_electronica, _ = CategoriaProducto.objects.get_or_create(nombre="Electrónica", defaults={"descripcion": "Productos electrónicos"})
    cat_accesorios, _ = CategoriaProducto.objects.get_or_create(nombre="Accesorios", defaults={"descripcion": "Accesorios de computador"})

    productos_data = [
        {"nombre_producto": "Laptop HP Pavilion 15", "sku": "LAP-HP-001", "categoria": cat_electronica, "precio_venta": Decimal("1800000"), "precio_compra": Decimal("1500000"), "stock_actual": 10, "stock_minimo": 2},
        {"nombre_producto": "Mouse Logitech MX Master", "sku": "MOU-LOG-001", "categoria": cat_accesorios, "precio_venta": Decimal("180000"), "precio_compra": Decimal("120000"), "stock_actual": 25, "stock_minimo": 5},
        {"nombre_producto": "Teclado Mecánico Corsair", "sku": "TEC-COR-001", "categoria": cat_accesorios, "precio_venta": Decimal("350000"), "precio_compra": Decimal("250000"), "stock_actual": 15, "stock_minimo": 3},
        {"nombre_producto": "Monitor LG 27 pulgadas", "sku": "MON-LG-001", "categoria": cat_electronica, "precio_venta": Decimal("900000"), "precio_compra": Decimal("700000"), "stock_actual": 8, "stock_minimo": 2},
        {"nombre_producto": "Impresora HP LaserJet", "sku": "IMP-HP-001", "categoria": cat_electronica, "precio_venta": Decimal("1200000"), "precio_compra": Decimal("950000"), "stock_actual": 5, "stock_minimo": 1},
    ]
    for data in productos_data:
        Producto.objects.get_or_create(sku=data['sku'], defaults=data)
    print(f"   ✓ {Producto.objects.count()} productos creados")
else:
    print(f"   ✓ Ya existen {Producto.objects.count()} productos")

# 4. CREAR PROVEEDORES
print("\n[4/10] Verificando Proveedores...")
if Proveedor.objects.count() < 3:
    proveedores_data = [
        {"nombre_empresa": "Tecnología Global S.A.", "nit": "900123456-7", "nombre_contacto": "Roberto García", "email": "ventas@tecnologiaglobal.com", "telefono": "6013334455", "calificacion": 5},
        {"nombre_empresa": "Distribuciones TechMax", "nit": "800234567-8", "nombre_contacto": "Ana Martínez", "email": "contacto@techmax.com", "telefono": "6015556677", "calificacion": 4},
        {"nombre_empresa": "Importaciones Digitales", "nit": "700345678-9", "nombre_contacto": "Luis Fernández", "email": "info@importacionesdigitales.com", "telefono": "6017778899", "calificacion": 5},
    ]
    for data in proveedores_data:
        Proveedor.objects.get_or_create(nit=data['nit'], defaults=data)
    print(f"   ✓ {Proveedor.objects.count()} proveedores creados")
else:
    print(f"   ✓ Ya existen {Proveedor.objects.count()} proveedores")

# 5. CREAR VENTAS
print("\n[5/10] Creando Ventas...")
if Venta.objects.count() == 0:
    clientes = list(Cliente.objects.all()[:3])
    productos = list(Producto.objects.all()[:3])

    for i, cliente in enumerate(clientes):
        venta = Venta.objects.create(
            cliente=cliente,
            estado='COMPLETADA',
            canal_venta='TIENDA',
            metodo_pago='EFECTIVO',
            pagado=True,
            vendedor="Vendedor Demo"
        )

        # Agregar productos a la venta
        for producto in productos[:2]:
            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=1,
                precio_unitario=producto.precio_venta,
                con_garantia=True
            )

        venta.calcular_totales()

    print(f"   ✓ {Venta.objects.count()} ventas creadas")
else:
    print(f"   ✓ Ya existen {Venta.objects.count()} ventas")

# 6. CREAR ÓRDENES DE SERVICIO
print("\n[6/10] Creando Órdenes de Servicio...")
if OrdenServicio.objects.count() == 0:
    clientes = list(Cliente.objects.all()[:3])
    tecnicos = list(Tecnico.objects.all()[:2])

    ordenes_data = [
        {"cliente": clientes[0], "tecnico_asignado": tecnicos[0], "tipo_equipo": "Laptop", "marca": "HP", "modelo": "Pavilion 15", "falla_reportada": "No enciende, pantalla negra", "estado": "EN_REPARACION", "prioridad": "ALTA"},
        {"cliente": clientes[1], "tecnico_asignado": tecnicos[1] if len(tecnicos) > 1 else tecnicos[0], "tipo_equipo": "PC Escritorio", "marca": "Dell", "modelo": "Optiplex 7010", "falla_reportada": "Lentitud extrema", "estado": "EN_DIAGNOSTICO", "prioridad": "MEDIA"},
        {"cliente": clientes[2], "tecnico_asignado": tecnicos[0], "tipo_equipo": "Impresora", "marca": "Epson", "modelo": "L3150", "falla_reportada": "No imprime colores", "estado": "RECIBIDA", "prioridad": "BAJA"},
    ]

    for data in ordenes_data:
        OrdenServicio.objects.create(**data)

    print(f"   ✓ {OrdenServicio.objects.count()} órdenes creadas")
else:
    print(f"   ✓ Ya existen {OrdenServicio.objects.count()} órdenes")

# 7. CREAR COMPRAS
print("\n[7/10] Creando Compras...")
if Compra.objects.count() == 0:
    proveedores = list(Proveedor.objects.all()[:2])
    productos = list(Producto.objects.all()[:3])

    for proveedor in proveedores:
        compra = Compra.objects.create(
            proveedor=proveedor,
            estado='COMPLETADA',
            metodo_pago='TRANSFERENCIA',
            pagado=True,
            responsable="Administrador"
        )

        for producto in productos[:2]:
            DetalleCompra.objects.create(
                compra=compra,
                producto=producto,
                cantidad=10,
                precio_unitario=producto.precio_compra,
                recibido=True
            )

        compra.calcular_totales()

    print(f"   ✓ {Compra.objects.count()} compras creadas")
else:
    print(f"   ✓ Ya existen {Compra.objects.count()} compras")

# 8. CREAR FACTURAS
print("\n[8/10] Creando Facturas...")
if Factura.objects.count() == 0:
    ventas = list(Venta.objects.all()[:3])

    for venta in ventas:
        Factura.objects.create(
            cliente=venta.cliente,
            venta=venta,
            tipo_factura='VENTA',
            estado='EMITIDA',
            subtotal=venta.subtotal,
            iva=venta.subtotal * Decimal('0.19'),
            total=venta.total
        )

    print(f"   ✓ {Factura.objects.count()} facturas creadas")
else:
    print(f"   ✓ Ya existen {Factura.objects.count()} facturas")

# 9. CREAR EQUIPOS
print("\n[9/10] Creando Equipos...")
if Equipo.objects.count() == 0:
    equipos_data = [
        {"nombre": "Laptop HP ProBook 450", "tipo_equipo": "LAPTOP", "marca": "HP", "modelo": "ProBook 450 G8", "numero_serie": "HP2021001", "fecha_adquisicion": datetime.now().date(), "valor_adquisicion": Decimal("2500000"), "estado": "OPERATIVO", "ubicacion": "Oficina Principal"},
        {"nombre": "PC Escritorio Dell", "tipo_equipo": "COMPUTADOR", "marca": "Dell", "modelo": "OptiPlex 7090", "numero_serie": "DELL2021002", "fecha_adquisicion": datetime.now().date(), "valor_adquisicion": Decimal("3000000"), "estado": "ASIGNADO", "ubicacion": "Oficina Administración"},
        {"nombre": "Impresora Multifuncional", "tipo_equipo": "IMPRESORA", "marca": "Epson", "modelo": "L3150", "numero_serie": "EPS2021003", "fecha_adquisicion": datetime.now().date(), "valor_adquisicion": Decimal("800000"), "estado": "OPERATIVO", "ubicacion": "Área Común"},
    ]

    for data in equipos_data:
        Equipo.objects.create(**data)

    print(f"   ✓ {Equipo.objects.count()} equipos creados")
else:
    print(f"   ✓ Ya existen {Equipo.objects.count()} equipos")

# 10. CREAR CAPACITACIONES
print("\n[10/10] Creando Capacitaciones...")
if Capacitacion.objects.count() == 0:
    fecha_inicio = datetime.now().date() + timedelta(days=7)
    fecha_fin = fecha_inicio + timedelta(days=2)

    capacitaciones_data = [
        {"nombre": "Reparación de Laptops Modernas", "tipo": "TECNICA", "instructor": "Ing. Roberto Sánchez", "descripcion": "Curso avanzado de reparación de laptops de última generación", "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin, "duracion_horas": 16, "lugar": "Centro de Capacitación DIGT SOFT", "modalidad": "PRESENCIAL", "estado": "PROGRAMADA", "cupo_maximo": 15, "costo": Decimal("500000")},
        {"nombre": "Atención al Cliente Excelente", "tipo": "ATENCION_CLIENTE", "instructor": "Lic. María González", "descripcion": "Técnicas profesionales de atención y servicio al cliente", "fecha_inicio": fecha_inicio + timedelta(days=14), "fecha_fin": fecha_inicio + timedelta(days=15), "duracion_horas": 8, "lugar": "Virtual - Zoom", "modalidad": "VIRTUAL", "estado": "PROGRAMADA", "cupo_maximo": 25, "costo": Decimal("200000")},
    ]

    for data in capacitaciones_data:
        Capacitacion.objects.create(**data)

    # Inscribir técnicos
    capacitacion = Capacitacion.objects.first()
    tecnicos = Tecnico.objects.all()[:2]
    for tecnico in tecnicos:
        ParticipanteCapacitacion.objects.create(
            capacitacion=capacitacion,
            tecnico=tecnico,
            asistio=False,
            aprobado=False
        )

    print(f"   ✓ {Capacitacion.objects.count()} capacitaciones creadas")
else:
    print(f"   ✓ Ya existen {Capacitacion.objects.count()} capacitaciones")

print("\n" + "=" * 60)
print("   ✅ DATOS DE PRUEBA CREADOS EXITOSAMENTE")
print("=" * 60)
print(f"\nRESUMEN:")
print(f"  • Clientes: {Cliente.objects.count()}")
print(f"  • Técnicos: {Tecnico.objects.count()}")
print(f"  • Productos: {Producto.objects.count()}")
print(f"  • Proveedores: {Proveedor.objects.count()}")
print(f"  • Ventas: {Venta.objects.count()}")
print(f"  • Órdenes: {OrdenServicio.objects.count()}")
print(f"  • Compras: {Compra.objects.count()}")
print(f"  • Facturas: {Factura.objects.count()}")
print(f"  • Equipos: {Equipo.objects.count()}")
print(f"  • Capacitaciones: {Capacitacion.objects.count()}")
print("\nPuedes ver todo en: http://127.0.0.1:8000/admin/")
print("=" * 60)

