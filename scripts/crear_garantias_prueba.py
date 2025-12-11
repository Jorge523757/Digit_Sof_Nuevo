"""
Script para crear garantías de prueba en el sistema
Ejecutar desde DIGTSoft/: python scripts/crear_garantias_prueba.py
"""

import os
import sys
import django
from datetime import date, timedelta
from random import choice, randint

# Agregar el directorio padre al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from garantias.models import Garantia
from productos.models import Producto
from clientes.models import Cliente

def crear_garantias():
    """Crear 15 garantías de prueba con diferentes estados"""

    # Obtener productos disponibles
    productos = list(Producto.objects.all()[:10])
    if not productos:
        print("❌ No hay productos en el sistema. Ejecuta primero crear_productos_prueba.py")
        return 0

    # Obtener clientes (opcional)
    clientes = list(Cliente.objects.all()[:5])

    # Datos de compradores de prueba
    compradores = [
        {'nombre': 'Carlos Rodríguez', 'cedula': '1234567890', 'telefono': '3001234567', 'email': 'carlos.r@email.com'},
        {'nombre': 'María González', 'cedula': '9876543210', 'telefono': '3109876543', 'email': 'maria.g@email.com'},
        {'nombre': 'Juan Pérez', 'cedula': '5555555555', 'telefono': '3205555555', 'email': 'juan.p@email.com'},
        {'nombre': 'Ana Martínez', 'cedula': '4444444444', 'telefono': '3154444444', 'email': 'ana.m@email.com'},
        {'nombre': 'Luis Torres', 'cedula': '7777777777', 'telefono': '3007777777', 'email': 'luis.t@email.com'},
        {'nombre': 'Sandra López', 'cedula': '8888888888', 'telefono': '3208888888', 'email': 'sandra.l@email.com'},
        {'nombre': 'Pedro Ramírez', 'cedula': '6666666666', 'telefono': '3106666666', 'email': 'pedro.r@email.com'},
        {'nombre': 'Laura Castro', 'cedula': '3333333333', 'telefono': '3153333333', 'email': 'laura.c@email.com'},
        {'nombre': 'Diego Vargas', 'cedula': '2222222222', 'telefono': '3002222222', 'email': 'diego.v@email.com'},
        {'nombre': 'Patricia Silva', 'cedula': '1111111111', 'telefono': '3201111111', 'email': 'patricia.s@email.com'},
    ]

    lugares_compra = ['DIGIT SOFT Sede Principal', 'Tienda Online', 'Distribuidor Autorizado', 'Amazon', 'Mercado Libre']

    estados = ['ACTIVA', 'ACTIVA', 'ACTIVA', 'ACTIVA', 'EN_REVISION', 'APROBADA', 'FINALIZADA']

    garantias_creadas = 0

    for i in range(15):
        comprador = compradores[i % len(compradores)]
        producto = productos[i % len(productos)]

        # Fechas
        dias_atras_compra = randint(30, 365)
        fecha_compra = date.today() - timedelta(days=dias_atras_compra)
        fecha_inicio = fecha_compra
        meses_garantia = producto.meses_garantia if producto.tiene_garantia else 12
        fecha_vencimiento = fecha_inicio + timedelta(days=meses_garantia * 30)

        # Estado basado en las fechas
        if fecha_vencimiento < date.today():
            estado = 'VENCIDA'
        else:
            estado = choice(estados)

        # Datos de la garantía
        garantia_data = {
            'nombre_comprador': comprador['nombre'],
            'cedula': comprador['cedula'],
            'telefono': comprador['telefono'],
            'correo_electronico': comprador['email'],
            'producto': producto,
            'nombre_producto': producto.nombre_producto,
            'numero_serie': f'SN{producto.codigo_sku}{randint(1000, 9999)}',
            'modelo': producto.modelo_equipo if producto.modelo_equipo else '',
            'fecha_compra': fecha_compra,
            'factura_compra': f'FAC-{randint(10000, 99999)}',
            'lugar_compra': choice(lugares_compra),
            'fecha_inicio': fecha_inicio,
            'fecha_vencimiento': fecha_vencimiento,
            'meses_garantia': meses_garantia,
            'estado': estado,
        }

        # Si tiene cliente asociado
        if clientes and i < len(clientes):
            garantia_data['cliente'] = clientes[i]

        # Si está en revisión, agregar motivo
        if estado == 'EN_REVISION':
            garantia_data['motivo_reclamacion'] = 'Producto con defecto de fábrica'
            garantia_data['descripcion_problema'] = 'El producto presenta fallas intermitentes y no funciona correctamente.'
        elif estado == 'FINALIZADA':
            garantia_data['motivo_reclamacion'] = 'Producto defectuoso'
            garantia_data['descripcion_problema'] = 'El producto dejó de funcionar después de 2 meses.'
            garantia_data['solucion'] = 'Se realizó el cambio del producto por uno nuevo.'
            garantia_data['fecha_resolucion'] = fecha_inicio + timedelta(days=15)

        # Crear garantía
        garantia = Garantia.objects.create(**garantia_data)
        garantias_creadas += 1

        # Emoji según estado
        if garantia.esta_vigente and estado == 'ACTIVA':
            emoji = "✅"
        elif estado == 'EN_REVISION':
            emoji = "⏳"
        elif estado == 'FINALIZADA':
            emoji = "✔️"
        elif estado == 'VENCIDA' or fecha_vencimiento < date.today():
            emoji = "❌"
        else:
            emoji = "📝"

        print(f"{emoji} Garantía #{garantia.id} creada: {garantia.nombre_producto} - {garantia.nombre_comprador} ({garantia.get_estado_display()})")

    return garantias_creadas

def main():
    print("=" * 60)
    print("CREANDO GARANTÍAS DE PRUEBA PARA DIGT SOFT")
    print("=" * 60)
    print()

    # Crear garantías
    print("🛡️  Creando garantías de prueba...")
    garantias_creadas = crear_garantias()

    print()
    print("=" * 60)
    print(f"✅ PROCESO COMPLETADO")
    print(f"🛡️  Total garantías creadas: {garantias_creadas}")
    print(f"📊 Total garantías en sistema: {Garantia.objects.count()}")

    # Estadísticas
    total = Garantia.objects.count()
    activas = Garantia.objects.filter(estado='ACTIVA', fecha_vencimiento__gte=date.today()).count()
    vencidas = Garantia.objects.filter(fecha_vencimiento__lt=date.today()).count()
    en_revision = Garantia.objects.filter(estado='EN_REVISION').count()

    print(f"✅ Garantías activas: {activas}")
    print(f"❌ Garantías vencidas: {vencidas}")
    print(f"⏳ En revisión: {en_revision}")
    print("=" * 60)

if __name__ == '__main__':
    main()

