"""
DIGIT SOFT - Generador de Datos de Prueba con Faker
Script completo para poblar todos los módulos del sistema
"""
import os
import django
import random
from datetime import datetime, timedelta
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from django.contrib.auth.models import User

# Importar todos los modelos
from clientes.models import Cliente
from productos.models import Producto, CategoriaProducto
from proveedores.models import Proveedor
from equipos.models import Equipo
from tecnicos.models import Tecnico
from ventas.models import Venta, DetalleVenta
from ordenes.models import OrdenServicio, RepuestoOrden
from garantias.models import Garantia
from compras.models import Compra, DetalleCompra
from capacitaciones.models import Capacitacion, ParticipanteCapacitacion

# Inicializar Faker en español
fake = Faker('es_ES')

print("=" * 80)
print("GENERADOR DE DATOS DE PRUEBA - DIGIT SOFT")
print("=" * 80)
print()


def limpiar_datos():
    """Limpiar todos los datos existentes (opcional)"""
    respuesta = input("¿Desea limpiar los datos existentes? (s/n): ")
    if respuesta.lower() == 's':
        print("\n🗑️  Limpiando datos existentes...")
        ParticipanteCapacitacion.objects.all().delete()
        DetalleCompra.objects.all().delete()
        RepuestoOrden.objects.all().delete()
        DetalleVenta.objects.all().delete()
        Capacitacion.objects.all().delete()
        Compra.objects.all().delete()
        Garantia.objects.all().delete()
        OrdenServicio.objects.all().delete()
        Venta.objects.all().delete()
        Equipo.objects.all().delete()
        Tecnico.objects.all().delete()
        Producto.objects.all().delete()
        CategoriaProducto.objects.all().delete()
        Proveedor.objects.all().delete()
        Cliente.objects.all().delete()
        print("✅ Datos limpiados exitosamente")


def crear_clientes(cantidad=30):
    """Crear clientes falsos"""
    print(f"\n👥 Creando {cantidad} clientes...")
    clientes = []

    for i in range(cantidad):
        cliente = Cliente.objects.create(
            nombres=fake.first_name(),
            apellidos=fake.last_name(),
            numero_documento=fake.unique.random_number(digits=10, fix_len=True),
            telefono=fake.phone_number()[:15],
            correo=fake.email(),
            direccion=fake.address(),
            activo=random.choice([True, True, True, False]),  # 75% activos
            observaciones=fake.text(max_nb_chars=200) if random.random() > 0.7 else ""
        )
        clientes.append(cliente)

    print(f"✅ {len(clientes)} clientes creados")
    return clientes


def crear_categorias():
    """Crear categorías de productos"""
    print("\n📦 Creando categorías de productos...")
    categorias_data = [
        ("Laptops", "Computadoras portátiles de todas las marcas"),
        ("Computadores de Escritorio", "PCs de escritorio y estaciones de trabajo"),
        ("Componentes PC", "Procesadores, memorias RAM, discos duros, tarjetas gráficas"),
        ("Periféricos", "Teclados, ratones, monitores, webcams"),
        ("Impresoras", "Impresoras láser, de inyección y multifuncionales"),
        ("Redes", "Routers, switches, cables de red, access points"),
        ("Smartphones", "Teléfonos móviles y accesorios"),
        ("Tablets", "Tabletas y accesorios"),
        ("Accesorios", "Cables, cargadores, fundas, protectores"),
        ("Software", "Licencias y programas"),
    ]

    categorias = []
    for nombre, descripcion in categorias_data:
        categoria, created = CategoriaProducto.objects.get_or_create(
            nombre=nombre,
            defaults={'descripcion': descripcion, 'activo': True}
        )
        categorias.append(categoria)

    print(f"✅ {len(categorias)} categorías creadas")
    return categorias


def crear_productos(categorias, cantidad=50):
    """Crear productos falsos"""
    print(f"\n💻 Creando {cantidad} productos...")
    productos = []

    marcas = ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Samsung', 'Apple', 'Logitech', 'Canon', 'Epson']

    for i in range(cantidad):
        categoria = random.choice(categorias)
        marca = random.choice(marcas)

        precio_compra = Decimal(random.uniform(100000, 5000000)).quantize(Decimal('0.01'))
        margen = Decimal(random.uniform(1.2, 1.8))
        precio_venta = (precio_compra * margen).quantize(Decimal('0.01'))
        precio_mayorista = (precio_venta * Decimal('0.85')).quantize(Decimal('0.01'))

        producto = Producto.objects.create(
            nombre_producto=f"{marca} {fake.word().title()} {random.randint(100, 9999)}",
            codigo_sku=f"SKU-{fake.unique.random_number(digits=8, fix_len=True)}",
            categoria=categoria,
            modelo_equipo=f"{marca}-{random.randint(1000, 9999)}",
            marca=marca,
            procesador=random.choice(['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Ryzen 5', 'AMD Ryzen 7']) if random.random() > 0.5 else "",
            memoria_ram=random.choice(['4GB', '8GB', '16GB', '32GB']) if random.random() > 0.5 else "",
            memoria_rom=random.choice(['256GB SSD', '512GB SSD', '1TB HDD', '1TB SSD', '2TB HDD']) if random.random() > 0.5 else "",
            descripcion=fake.text(max_nb_chars=300),
            especificaciones=fake.text(max_nb_chars=400),
            precio_compra=precio_compra,
            precio_venta=precio_venta,
            precio_mayorista=precio_mayorista,
            stock_actual=random.randint(0, 100),
            stock_minimo=random.randint(5, 15),
            stock_maximo=random.randint(50, 200),
            disponible_web=random.choice([True, True, True, False]),
            destacado=random.choice([True, False, False, False]),
            activo=random.choice([True, True, True, False]),
            tiene_garantia=True,
            meses_garantia=random.choice([6, 12, 24, 36])
        )
        productos.append(producto)

    print(f"✅ {len(productos)} productos creados")
    return productos


def crear_proveedores(cantidad=15):
    """Crear proveedores falsos"""
    print(f"\n🏢 Creando {cantidad} proveedores...")
    proveedores = []

    for i in range(cantidad):
        proveedor = Proveedor.objects.create(
            nombre_empresa=fake.company(),
            nit=f"{fake.random_number(digits=9, fix_len=True)}-{random.randint(0, 9)}",
            nombre_contacto=fake.name(),
            telefono=fake.phone_number()[:15],
            email=fake.company_email(),
            direccion=fake.address(),
            ciudad=fake.city(),
            pais="Colombia",
            productos_servicios=fake.text(max_nb_chars=200),
            condiciones_pago=random.choice(['Contado', '30 días', '60 días', '90 días']),
            tiempo_entrega=f"{random.randint(1, 30)} días",
            calificacion=random.randint(1, 5),
            activo=random.choice([True, True, True, False]),
            observaciones=fake.text(max_nb_chars=150) if random.random() > 0.7 else ""
        )
        proveedores.append(proveedor)

    print(f"✅ {len(proveedores)} proveedores creados")
    return proveedores


def crear_equipos(cantidad=25):
    """Crear equipos de la empresa"""
    print(f"\n🖥️  Creando {cantidad} equipos...")
    equipos = []

    tipos = ['COMPUTADOR', 'LAPTOP', 'IMPRESORA', 'SERVIDOR', 'ROUTER', 'OTRO']
    estados = ['OPERATIVO', 'EN_REPARACION', 'FUERA_SERVICIO', 'ASIGNADO', 'DISPONIBLE']

    for i in range(cantidad):
        tipo = random.choice(tipos)
        equipo = Equipo.objects.create(
            codigo_equipo=f"EQ-{fake.unique.random_number(digits=6, fix_len=True)}",
            nombre=f"{tipo.title()} {fake.word().title()}",
            tipo_equipo=tipo,
            marca=random.choice(['Dell', 'HP', 'Lenovo', 'Cisco', 'Epson', 'Canon']),
            modelo=f"MODEL-{random.randint(1000, 9999)}",
            numero_serie=fake.bothify(text='SN-########'),
            especificaciones=fake.text(max_nb_chars=200),
            fecha_adquisicion=fake.date_between(start_date='-3y', end_date='today'),
            valor_adquisicion=Decimal(random.uniform(500000, 10000000)).quantize(Decimal('0.01')),
            estado=random.choice(estados),
            ubicacion=fake.city() if random.random() > 0.3 else "",
            responsable=fake.name() if random.random() > 0.4 else "",
            observaciones=fake.text(max_nb_chars=150) if random.random() > 0.7 else "",
            activo=random.choice([True, True, True, False])
        )
        equipos.append(equipo)

    print(f"✅ {len(equipos)} equipos creados")
    return equipos


def crear_tecnicos(cantidad=10):
    """Crear técnicos falsos"""
    print(f"\n👨‍🔧 Creando {cantidad} técnicos...")
    tecnicos = []

    profesiones = [
        'Ingeniero de Sistemas',
        'Técnico en Computación',
        'Ingeniero Electrónico',
        'Técnico en Mantenimiento',
        'Ingeniero en Telecomunicaciones',
        'Especialista en Redes'
    ]

    for i in range(cantidad):
        tecnico = Tecnico.objects.create(
            nombres=fake.first_name(),
            apellidos=fake.last_name(),
            numero_documento=fake.unique.random_number(digits=10, fix_len=True),
            telefono=fake.phone_number()[:15],
            correo=fake.email(),
            profesion=random.choice(profesiones),
            activo=random.choice([True, True, True, False])
        )
        tecnicos.append(tecnico)

    print(f"✅ {len(tecnicos)} técnicos creados")
    return tecnicos


def crear_ventas(clientes, productos, cantidad=40):
    """Crear ventas con sus detalles"""
    print(f"\n🛒 Creando {cantidad} ventas...")
    ventas = []

    # Obtener usuario admin o crear uno
    try:
        usuario = User.objects.get(username='admin')
    except User.DoesNotExist:
        usuario = User.objects.first()

    estados = ['PENDIENTE', 'PROCESANDO', 'COMPLETADA', 'CANCELADA']
    metodos_pago = ['EFECTIVO', 'TARJETA', 'TRANSFERENCIA', 'PSE', 'CREDITO']
    canales = ['TIENDA', 'WEB', 'TELEFONO', 'WHATSAPP']

    for i in range(cantidad):
        fecha_venta = fake.date_time_between(start_date='-6m', end_date='now')

        venta = Venta.objects.create(
            numero_venta=f"VTA-{fake.unique.random_number(digits=8, fix_len=True)}",
            cliente=random.choice(clientes),
            usuario=usuario,
            estado=random.choice(estados),
            canal_venta=random.choice(canales),
            metodo_pago=random.choice(metodos_pago),
            pagado=random.choice([True, True, False]),
            requiere_entrega=random.choice([True, False]),
            direccion_entrega=fake.address() if random.random() > 0.5 else "",
            entregado=random.choice([True, False]),
            vendedor=fake.name() if random.random() > 0.5 else "",
            observaciones=fake.text(max_nb_chars=150) if random.random() > 0.7 else ""
        )

        # Establecer fecha
        venta.fecha_venta = fecha_venta

        # Crear detalles de venta
        num_items = random.randint(1, 5)
        subtotal = Decimal('0')

        productos_vendidos = random.sample(productos, min(num_items, len(productos)))
        for producto in productos_vendidos:
            cantidad = random.randint(1, 3)
            precio_unitario = producto.precio_venta
            subtotal_item = precio_unitario * cantidad

            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                subtotal=subtotal_item
            )
            subtotal += subtotal_item

        # Calcular totales
        descuento = subtotal * Decimal(random.uniform(0, 0.15))
        impuestos = (subtotal - descuento) * Decimal('0.19')  # IVA 19%
        total = subtotal - descuento + impuestos

        venta.subtotal = subtotal
        venta.descuento = descuento.quantize(Decimal('0.01'))
        venta.impuestos = impuestos.quantize(Decimal('0.01'))
        venta.total = total.quantize(Decimal('0.01'))
        venta.save()

        ventas.append(venta)

    print(f"✅ {len(ventas)} ventas creadas")
    return ventas


def crear_ordenes_servicio(clientes, tecnicos, productos, cantidad=30):
    """Crear órdenes de servicio técnico"""
    print(f"\n🔧 Creando {cantidad} órdenes de servicio...")
    ordenes = []

    estados = ['RECIBIDA', 'EN_DIAGNOSTICO', 'DIAGNOSTICADA', 'EN_REPARACION',
               'REPARADA', 'EN_ESPERA_REPUESTOS', 'LISTA_ENTREGA', 'ENTREGADA']
    prioridades = ['BAJA', 'MEDIA', 'ALTA', 'URGENTE']
    tipos_equipo = ['Laptop', 'PC Escritorio', 'Impresora', 'Tablet', 'Smartphone']

    for i in range(cantidad):
        fecha_ingreso = fake.date_time_between(start_date='-3m', end_date='now')

        orden = OrdenServicio.objects.create(
            numero_orden=f"ORD-{fake.unique.random_number(digits=8, fix_len=True)}",
            cliente=random.choice(clientes),
            tecnico_asignado=random.choice(tecnicos) if random.random() > 0.2 else None,
            tipo_equipo=random.choice(tipos_equipo),
            marca=random.choice(['Dell', 'HP', 'Lenovo', 'Samsung', 'Apple']),
            modelo=f"MODEL-{random.randint(1000, 9999)}",
            serie=fake.bothify(text='SN-########') if random.random() > 0.3 else "",
            falla_reportada=fake.text(max_nb_chars=200),
            estado_fisico=fake.text(max_nb_chars=150) if random.random() > 0.5 else "",
            accesorios_incluidos=random.choice(['Cargador', 'Cargador, bolso', 'Ninguno', 'Cargador, mouse']),
            diagnostico=fake.text(max_nb_chars=200) if random.random() > 0.6 else "",
            solucion_aplicada=fake.text(max_nb_chars=200) if random.random() > 0.5 else "",
            estado=random.choice(estados),
            prioridad=random.choice(prioridades),
            costo_diagnostico=Decimal(random.uniform(20000, 50000)).quantize(Decimal('0.01')),
            costo_mano_obra=Decimal(random.uniform(50000, 300000)).quantize(Decimal('0.01')),
            pagado=random.choice([True, True, False]),
            tiene_garantia=random.choice([True, False]),
            dias_garantia=random.choice([15, 30, 60, 90]),
            observaciones=fake.text(max_nb_chars=150) if random.random() > 0.7 else ""
        )

        # Establecer fechas
        orden.fecha_recepcion = fecha_ingreso
        orden.fecha_compromiso = fecha_ingreso + timedelta(days=random.randint(3, 15))
        orden.save()

        # Agregar repuestos (opcional)
        if random.random() > 0.5:
            num_repuestos = random.randint(1, 3)
            repuestos_usados = random.sample(productos[:20], min(num_repuestos, 20))

            for repuesto in repuestos_usados:
                cantidad = random.randint(1, 2)
                RepuestoOrden.objects.create(
                    orden=orden,
                    producto=repuesto,
                    cantidad=cantidad,
                    precio_unitario=repuesto.precio_venta
                )

        ordenes.append(orden)

    print(f"✅ {len(ordenes)} órdenes de servicio creadas")
    return ordenes


def crear_garantias(clientes, productos, cantidad=25):
    """Crear garantías de productos"""
    print(f"\n📜 Creando {cantidad} garantías...")
    garantias = []

    estados = ['ACTIVA', 'VENCIDA', 'EN_REVISION', 'APROBADA', 'RECHAZADA', 'FINALIZADA']

    for i in range(cantidad):
        producto = random.choice(productos)
        fecha_compra = fake.date_between(start_date='-2y', end_date='today')
        fecha_inicio = fecha_compra
        meses = producto.meses_garantia
        fecha_vencimiento = fecha_inicio + timedelta(days=meses * 30)

        garantia = Garantia.objects.create(
            nombre_comprador=fake.name(),
            cedula=fake.random_number(digits=10, fix_len=True),
            telefono=fake.phone_number()[:15],
            correo_electronico=fake.email(),
            producto=producto,
            nombre_producto=producto.nombre_producto,
            numero_serie=fake.bothify(text='SN-########'),
            modelo=producto.modelo_equipo,
            fecha_compra=fecha_compra,
            factura_compra=f"FACT-{fake.random_number(digits=8)}" if random.random() > 0.3 else "",
            lugar_compra="Digit Soft",
            fecha_inicio=fecha_inicio,
            fecha_vencimiento=fecha_vencimiento,
            meses_garantia=meses,
            estado=random.choice(estados),
            motivo_reclamacion=fake.text(max_nb_chars=150) if random.random() > 0.5 else "",
            descripcion_problema=fake.text(max_nb_chars=200) if random.random() > 0.5 else "",
            solucion=fake.text(max_nb_chars=200) if random.random() > 0.4 else "",
            fecha_resolucion=fake.date_between(start_date=fecha_inicio, end_date='today') if random.random() > 0.6 else None,
            observaciones=fake.text(max_nb_chars=150) if random.random() > 0.7 else "",
            cliente=random.choice(clientes) if random.random() > 0.3 else None
        )
        garantias.append(garantia)

    print(f"✅ {len(garantias)} garantías creadas")
    return garantias


def crear_compras(proveedores, productos, cantidad=20):
    """Crear compras a proveedores"""
    print(f"\n📦 Creando {cantidad} compras...")
    compras = []

    try:
        usuario = User.objects.get(username='admin')
    except User.DoesNotExist:
        usuario = User.objects.first()

    estados = ['PENDIENTE', 'APROBADA', 'RECIBIDA', 'COMPLETADA', 'CANCELADA']
    metodos_pago = ['EFECTIVO', 'TRANSFERENCIA', 'CHEQUE', 'CREDITO']

    for i in range(cantidad):
        fecha_compra = fake.date_time_between(start_date='-4m', end_date='now')

        compra = Compra.objects.create(
            numero_compra=f"COMP-{fake.unique.random_number(digits=8, fix_len=True)}",
            proveedor=random.choice(proveedores),
            usuario=usuario,
            fecha_entrega_esperada=fake.date_between(start_date='today', end_date='+30d'),
            fecha_entrega_real=fake.date_between(start_date='today', end_date='+15d') if random.random() > 0.5 else None,
            estado=random.choice(estados),
            metodo_pago=random.choice(metodos_pago),
            pagado=random.choice([True, False]),
            responsable=fake.name() if random.random() > 0.5 else "",
            observaciones=fake.text(max_nb_chars=150) if random.random() > 0.7 else ""
        )

        compra.fecha_compra = fecha_compra

        # Crear detalles de compra
        num_items = random.randint(1, 8)
        subtotal = Decimal('0')

        productos_comprados = random.sample(productos, min(num_items, len(productos)))
        for producto in productos_comprados:
            cantidad = random.randint(5, 50)
            precio_unitario = producto.precio_compra
            subtotal_item = precio_unitario * cantidad

            DetalleCompra.objects.create(
                compra=compra,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                subtotal=subtotal_item
            )
            subtotal += subtotal_item

        # Calcular totales
        impuestos = subtotal * Decimal('0.19')
        descuento = subtotal * Decimal(random.uniform(0, 0.05))
        total = subtotal + impuestos - descuento

        compra.subtotal = subtotal
        compra.impuestos = impuestos.quantize(Decimal('0.01'))
        compra.descuento = descuento.quantize(Decimal('0.01'))
        compra.total = total.quantize(Decimal('0.01'))
        compra.save()

        compras.append(compra)

    print(f"✅ {len(compras)} compras creadas")
    return compras


def crear_capacitaciones(tecnicos, cantidad=15):
    """Crear capacitaciones y sus participantes"""
    print(f"\n🎓 Creando {cantidad} capacitaciones...")
    capacitaciones = []

    tipos = ['TECNICA', 'SOFTWARE', 'ATENCION_CLIENTE', 'SEGURIDAD', 'OTRA']
    estados = ['PROGRAMADA', 'EN_CURSO', 'COMPLETADA', 'CANCELADA']
    modalidades = ['PRESENCIAL', 'VIRTUAL', 'HIBRIDA']

    temas = [
        'Reparación de Laptops Avanzada',
        'Mantenimiento Preventivo',
        'Diagnóstico de Hardware',
        'Instalación de Redes',
        'Seguridad Informática',
        'Atención al Cliente',
        'Gestión de Inventarios',
        'Soporte Técnico Nivel 2',
        'Configuración de Servidores',
        'Cloud Computing'
    ]

    for i in range(cantidad):
        fecha_inicio = fake.date_between(start_date='-3m', end_date='+3m')
        duracion_dias = random.randint(1, 5)
        duracion_horas = duracion_dias * random.randint(4, 8)

        capacitacion = Capacitacion.objects.create(
            codigo_capacitacion=f"CAP-{fake.unique.random_number(digits=6, fix_len=True)}",
            nombre=random.choice(temas),
            tipo=random.choice(tipos),
            descripcion=fake.text(max_nb_chars=300),
            instructor=fake.name(),
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_inicio + timedelta(days=duracion_dias),
            duracion_horas=duracion_horas,
            lugar=fake.city() if random.random() > 0.5 else "Virtual",
            modalidad=random.choice(modalidades),
            estado=random.choice(estados),
            cupo_maximo=random.randint(10, 30),
            costo=Decimal(random.uniform(0, 500000)).quantize(Decimal('0.01')),
            certificado=random.choice([True, True, False]),
            observaciones=fake.text(max_nb_chars=150) if random.random() > 0.7 else ""
        )
        capacitaciones.append(capacitacion)

        # Inscribir técnicos
        num_participantes = random.randint(3, min(len(tecnicos), capacitacion.cupo_maximo))
        participantes = random.sample(tecnicos, num_participantes)

        for tecnico in participantes:
            ParticipanteCapacitacion.objects.create(
                capacitacion=capacitacion,
                tecnico=tecnico,
                asistio=random.choice([True, True, False]),
                aprobado=random.choice([True, True, False]),
                calificacion=Decimal(random.uniform(3.0, 5.0)).quantize(Decimal('0.01')) if random.random() > 0.3 else None,
                observaciones=fake.text(max_nb_chars=100) if random.random() > 0.8 else ""
            )

    print(f"✅ {len(capacitaciones)} capacitaciones creadas")
    return capacitaciones


def main():
    """Función principal"""
    print("Este script generará datos de prueba para todos los módulos del sistema.")
    print()

    # Preguntar si desea limpiar datos
    limpiar_datos()

    print("\n" + "=" * 80)
    print("INICIANDO GENERACIÓN DE DATOS")
    print("=" * 80)

    # Generar datos en orden de dependencias
    clientes = crear_clientes(30)
    categorias = crear_categorias()
    productos = crear_productos(categorias, 50)
    proveedores = crear_proveedores(15)
    equipos = crear_equipos(25)
    tecnicos = crear_tecnicos(10)
    ventas = crear_ventas(clientes, productos, 40)
    ordenes = crear_ordenes_servicio(clientes, tecnicos, productos, 30)
    garantias = crear_garantias(clientes, productos, 25)
    compras = crear_compras(proveedores, productos, 20)
    capacitaciones = crear_capacitaciones(tecnicos, 15)

    print("\n" + "=" * 80)
    print("✅ GENERACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 80)
    print("\n📊 RESUMEN DE DATOS GENERADOS:")
    print(f"   • {Cliente.objects.count()} Clientes")
    print(f"   • {CategoriaProducto.objects.count()} Categorías de Productos")
    print(f"   • {Producto.objects.count()} Productos")
    print(f"   • {Proveedor.objects.count()} Proveedores")
    print(f"   • {Equipo.objects.count()} Equipos")
    print(f"   • {Tecnico.objects.count()} Técnicos")
    print(f"   • {Venta.objects.count()} Ventas")
    print(f"   • {DetalleVenta.objects.count()} Detalles de Venta")
    print(f"   • {OrdenServicio.objects.count()} Órdenes de Servicio")
    print(f"   • {RepuestoOrden.objects.count()} Repuestos en Órdenes")
    print(f"   • {Garantia.objects.count()} Garantías")
    print(f"   • {Compra.objects.count()} Compras")
    print(f"   • {DetalleCompra.objects.count()} Detalles de Compra")
    print(f"   • {Capacitacion.objects.count()} Capacitaciones")
    print(f"   • {ParticipanteCapacitacion.objects.count()} Participantes en Capacitaciones")
    print("\n🎉 ¡Todos los módulos han sido poblados con datos de prueba!")
    print("=" * 80)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

