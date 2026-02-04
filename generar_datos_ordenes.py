"""
DIGT SOFT - Generador de Datos de Prueba para Órdenes de Servicio
Genera datos usando Faker que se guardan en la base de datos MySQL
"""

import os
import django
import sys

# Configurar Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from datetime import datetime, timedelta
from decimal import Decimal
import random

# Importar modelos
from clientes.models import Cliente
from tecnicos.models import Tecnico
from ordenes.models import OrdenServicio, SeguimientoOrden
from usuarios.models import Notificacion

fake = Faker('es_ES')

print("=" * 80)
print("DIGT SOFT - Generador de Datos para Órdenes de Servicio")
print("=" * 80)
print()

def crear_ordenes_servicio(cantidad=20):
    """Crear órdenes de servicio con datos realistas"""

    print(f"📋 Generando {cantidad} órdenes de servicio...")

    # Obtener clientes y técnicos existentes
    clientes = list(Cliente.objects.filter(activo=True))
    tecnicos = list(Tecnico.objects.filter(activo=True))

    if not clientes:
        print("❌ Error: No hay clientes en la base de datos.")
        print("   Ejecute primero: python generar_datos_faker.py")
        return 0

    if not tecnicos:
        print("⚠️  Advertencia: No hay técnicos en la base de datos.")
        print("   Las órdenes se crearán sin técnico asignado.")

    # Tipos de equipos comunes
    tipos_equipo = [
        'Laptop', 'PC de Escritorio', 'Impresora', 'Monitor',
        'Tablet', 'All-in-One', 'Servidor', 'Router',
        'Switch', 'UPS', 'Scanner', 'Proyector'
    ]

    # Marcas populares
    marcas = {
        'Laptop': ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Apple', 'MSI', 'Toshiba'],
        'PC de Escritorio': ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Compaq'],
        'Impresora': ['HP', 'Epson', 'Canon', 'Brother', 'Samsung', 'Xerox'],
        'Monitor': ['Samsung', 'LG', 'Dell', 'HP', 'Asus', 'AOC', 'BenQ'],
        'Tablet': ['Apple', 'Samsung', 'Huawei', 'Lenovo', 'Amazon'],
    }

    # Fallas comunes por tipo de equipo
    fallas_laptop = [
        'No enciende, luz de carga parpadea',
        'Pantalla rota, muestra líneas verticales',
        'Teclado derrama líquido, varias teclas no funcionan',
        'No carga la batería, se apaga al desconectar',
        'Sobrecalentamiento, se apaga solo',
        'Disco duro hace ruidos extraños, lento',
        'WiFi no detecta redes, problema de conectividad',
        'Pantalla negra, enciende pero no muestra imagen',
        'Ventilador hace mucho ruido',
        'Puerto USB no funciona, no reconoce dispositivos'
    ]

    fallas_pc = [
        'No enciende, luz de encendido no se ilumina',
        'Reinicio constante, pantalla azul',
        'Lentitud extrema, tarda mucho en iniciar',
        'No detecta disco duro',
        'Problemas con tarjeta de video',
        'Memoria RAM defectuosa',
        'Fuente de poder falla',
        'No tiene sonido'
    ]

    fallas_impresora = [
        'No imprime, atasco de papel constante',
        'Imprime con líneas, calidad deficiente',
        'No reconoce cartuchos de tinta',
        'Error de comunicación con PC',
        'No enciende la impresora',
        'Imprime muy lento',
        'Manchas en las impresiones'
    ]

    estados_disponibles = [
        'RECIBIDA', 'EN_DIAGNOSTICO', 'DIAGNOSTICADA',
        'EN_REPARACION', 'REPARADA', 'LISTA_ENTREGA',
        'ENTREGADA', 'EN_ESPERA_REPUESTOS'
    ]

    prioridades = ['BAJA', 'MEDIA', 'ALTA', 'URGENTE']

    ordenes_creadas = 0

    for i in range(cantidad):
        try:
            # Seleccionar tipo de equipo y marca
            tipo_equipo = random.choice(tipos_equipo)
            if tipo_equipo in marcas:
                marca = random.choice(marcas[tipo_equipo])
            else:
                marca = random.choice(marcas['Laptop'])

            # Generar modelo
            modelo = f"{fake.word().upper()}-{random.randint(1000, 9999)}"

            # Seleccionar falla según tipo
            if 'Laptop' in tipo_equipo:
                falla = random.choice(fallas_laptop)
            elif 'PC' in tipo_equipo:
                falla = random.choice(fallas_pc)
            elif 'Impresora' in tipo_equipo:
                falla = random.choice(fallas_impresora)
            else:
                falla = f"{fake.sentence(nb_words=8)} - Requiere revisión técnica"

            # Fechas
            dias_atras = random.randint(1, 90)
            fecha_recepcion = datetime.now() - timedelta(days=dias_atras)
            fecha_compromiso = fecha_recepcion + timedelta(days=random.randint(3, 15))

            # Estado basado en antigüedad
            if dias_atras < 5:
                estado = random.choice(['RECIBIDA', 'EN_DIAGNOSTICO'])
            elif dias_atras < 15:
                estado = random.choice(['EN_DIAGNOSTICO', 'DIAGNOSTICADA', 'EN_REPARACION'])
            elif dias_atras < 30:
                estado = random.choice(['EN_REPARACION', 'REPARADA', 'LISTA_ENTREGA'])
            else:
                estado = random.choice(['LISTA_ENTREGA', 'ENTREGADA'])

            # Costos
            costo_diagnostico = Decimal(str(random.uniform(20, 50)))
            costo_mano_obra = Decimal(str(random.uniform(50, 300)))
            costo_repuestos = Decimal(str(random.uniform(0, 500))) if random.random() > 0.3 else Decimal('0')

            # Crear orden
            orden = OrdenServicio.objects.create(
                cliente=random.choice(clientes),
                tecnico_asignado=random.choice(tecnicos) if tecnicos and random.random() > 0.2 else None,
                tipo_equipo=tipo_equipo,
                marca=marca,
                modelo=modelo,
                serie=fake.bothify(text='SN-####-????-####').upper() if random.random() > 0.3 else '',
                falla_reportada=falla,
                estado_fisico=random.choice([
                    'Buen estado general, sin golpes visibles',
                    'Rayones leves en la carcasa',
                    'Equipo con signos de uso, algunas marcas',
                    'Condición regular, desgaste normal',
                    'Golpes en esquinas, detalles estéticos'
                ]),
                accesorios_incluidos=random.choice([
                    'Cargador original, bolso de transporte',
                    'Solo el equipo, sin accesorios',
                    'Cargador, mouse inalámbrico',
                    'Cargador, cable de red',
                    'Sin accesorios'
                ]),
                diagnostico=fake.paragraph() if estado not in ['RECIBIDA', 'EN_DIAGNOSTICO'] else '',
                solucion_aplicada=fake.paragraph() if estado in ['REPARADA', 'LISTA_ENTREGA', 'ENTREGADA'] else '',
                estado=estado,
                prioridad=random.choice(prioridades),
                costo_diagnostico=costo_diagnostico,
                costo_mano_obra=costo_mano_obra,
                costo_repuestos=costo_repuestos,
                fecha_recepcion=fecha_recepcion,
                fecha_compromiso=fecha_compromiso,
                fecha_entrega=fecha_recepcion + timedelta(days=random.randint(5, 20)) if estado == 'ENTREGADA' else None,
                tiene_garantia=True,
                dias_garantia=random.choice([15, 30, 60, 90]),
                observaciones=fake.sentence() if random.random() > 0.5 else '',
                notas_internas=fake.sentence() if random.random() > 0.7 else ''
            )

            # Crear seguimientos según el estado
            seguimientos_estados = []

            if estado == 'RECIBIDA':
                seguimientos_estados = ['RECIBIDA']
            elif estado == 'EN_DIAGNOSTICO':
                seguimientos_estados = ['RECIBIDA', 'EN_DIAGNOSTICO']
            elif estado == 'DIAGNOSTICADA':
                seguimientos_estados = ['RECIBIDA', 'EN_DIAGNOSTICO', 'DIAGNOSTICADA']
            elif estado == 'EN_REPARACION':
                seguimientos_estados = ['RECIBIDA', 'EN_DIAGNOSTICO', 'DIAGNOSTICADA', 'EN_REPARACION']
            elif estado == 'REPARADA':
                seguimientos_estados = ['RECIBIDA', 'EN_DIAGNOSTICO', 'DIAGNOSTICADA', 'EN_REPARACION', 'REPARADA']
            elif estado == 'LISTA_ENTREGA':
                seguimientos_estados = ['RECIBIDA', 'EN_DIAGNOSTICO', 'EN_REPARACION', 'REPARADA', 'LISTA_ENTREGA']
            elif estado == 'ENTREGADA':
                seguimientos_estados = ['RECIBIDA', 'EN_DIAGNOSTICO', 'EN_REPARACION', 'LISTA_ENTREGA', 'ENTREGADA']

            # Crear seguimientos
            fecha_seguimiento = fecha_recepcion
            for idx, estado_seg in enumerate(seguimientos_estados):
                estado_ant = seguimientos_estados[idx - 1] if idx > 0 else ''

                SeguimientoOrden.objects.create(
                    orden=orden,
                    estado_anterior=estado_ant,
                    estado_nuevo=estado_seg,
                    descripcion=f"Estado cambiado a {dict(OrdenServicio.ESTADO_CHOICES).get(estado_seg, estado_seg)}. {fake.sentence()}",
                    usuario=orden.tecnico_asignado.nombre_completo if orden.tecnico_asignado else 'Sistema',
                    fecha=fecha_seguimiento
                )

                # Avanzar fecha para siguiente seguimiento
                fecha_seguimiento += timedelta(days=random.randint(1, 3), hours=random.randint(1, 8))

            ordenes_creadas += 1
            print(f"  ✓ Orden {orden.numero_orden}: {tipo_equipo} {marca} - Estado: {orden.get_estado_display()}")

        except Exception as e:
            print(f"  ✗ Error creando orden {i+1}: {str(e)}")

    print()
    print(f"✅ {ordenes_creadas} órdenes de servicio creadas exitosamente")
    print()
    return ordenes_creadas


def main():
    """Función principal"""
    print("Iniciando generación de datos de órdenes de servicio...")
    print()

    # Verificar que existan clientes
    total_clientes = Cliente.objects.count()
    total_tecnicos = Tecnico.objects.count()

    print(f"📊 Estado actual de la base de datos:")
    print(f"   - Clientes: {total_clientes}")
    print(f"   - Técnicos: {total_tecnicos}")
    print(f"   - Órdenes existentes: {OrdenServicio.objects.count()}")
    print()

    if total_clientes == 0:
        print("❌ No hay clientes en la base de datos.")
        print("   Por favor ejecute primero: python generar_datos_faker.py")
        return

    # Preguntar cantidad
    cantidad = 20
    print(f"🔧 Se crearán {cantidad} órdenes de servicio de ejemplo")
    print()

    # Generar datos
    crear_ordenes_servicio(cantidad)

    # Resumen final
    print()
    print("=" * 80)
    print("✅ PROCESO COMPLETADO")
    print("=" * 80)
    print()
    print("📊 Resumen final:")
    print(f"   - Total de órdenes: {OrdenServicio.objects.count()}")
    print(f"   - Total de seguimientos: {SeguimientoOrden.objects.count()}")
    print()
    print("🎉 Los datos se han guardado en la base de datos MySQL")
    print("   y permanecerán guardados incluso si reinicia el servidor.")
    print()
    print("Para ver las órdenes, inicie el servidor y visite:")
    print("   http://localhost:8000/ordenes/")
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("❌ Proceso interrumpido por el usuario")
    except Exception as e:
        print()
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

