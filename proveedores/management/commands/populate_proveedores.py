"""
DIGT SOFT - Comando de Gestión para Poblar Proveedores
Genera datos de prueba realistas usando Faker
"""

import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from proveedores.models import Proveedor


class Command(BaseCommand):
    help = 'Pobla la base de datos con proveedores de prueba usando Faker'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            default=15,
            nargs='?',
            help='Número de proveedores a crear (por defecto: 15)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Eliminar todos los proveedores existentes antes de crear nuevos'
        )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        count = kwargs['count']
        clear = kwargs['clear']
        fake = Faker('es_CO')

        # Colores para el output
        self.stdout.write(self.style.WARNING('=' * 60))
        self.stdout.write(self.style.WARNING('🏢 DIGIT SOFT - Generador de Proveedores'))
        self.stdout.write(self.style.WARNING('=' * 60))

        # Limpiar datos existentes si se especifica
        if clear:
            Proveedor.objects.all().delete()
            self.stdout.write(self.style.WARNING('\n🗑️  Proveedores existentes eliminados'))

        self.stdout.write(self.style.WARNING(f'\n🏭 Creando {count} proveedores...'))

        # Sufijos para nombres de empresas tecnológicas
        sufijos_empresa = [
            'Technology', 'Systems', 'Solutions', 'Tech', 'Computers',
            'Electronics', 'Digital', 'Innovation', 'Software', 'Hardware',
            'Networks', 'Data', 'Cloud', 'Security', 'Services'
        ]

        tipos_productos = [
            'Computadores y equipos de cómputo',
            'Componentes electrónicos y hardware',
            'Periféricos y accesorios tecnológicos',
            'Smartphones y tablets',
            'Equipos de redes y comunicaciones',
            'Servicios de mantenimiento y soporte técnico',
            'Software y licencias',
            'Equipos de seguridad y videovigilancia',
            'Impresoras y consumibles',
            'Servidores y almacenamiento'
        ]

        condiciones_pago_options = [
            'Contado',
            '30 días',
            '45 días',
            '60 días',
            '15 días',
            'Contra entrega',
            '50% anticipo, 50% contra entrega'
        ]

        proveedores_to_create = []
        nits_usados = set()

        for i in range(count):
            # Generar NIT único
            nit = fake.unique.numerify(text='#########-#')

            # Asegurar que sea único
            while nit in nits_usados or Proveedor.objects.filter(nit=nit).exists():
                nit = fake.unique.numerify(text='#########-#')

            nits_usados.add(nit)

            # Nombre de empresa tecnológica
            nombre_empresa = f"{fake.company().split()[0]} {random.choice(sufijos_empresa)}"

            # Contacto
            nombre_contacto = fake.name()
            telefono = fake.phone_number()
            email = f"contacto@{nombre_empresa.lower().replace(' ', '')}.com"

            # Ubicación
            ciudades_colombia = [
                'Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena',
                'Bucaramanga', 'Pereira', 'Manizales', 'Cúcuta', 'Ibagué'
            ]
            ciudad = random.choice(ciudades_colombia)
            direccion = f"Calle {random.randint(1, 200)} #{random.randint(1, 99)}-{random.randint(1, 99)}"

            proveedor = Proveedor(
                nombre_empresa=nombre_empresa,
                nit=nit,
                nombre_contacto=nombre_contacto,
                telefono=telefono,
                email=email,
                direccion=direccion,
                ciudad=ciudad,
                pais='Colombia',
                productos_servicios=random.choice(tipos_productos),
                condiciones_pago=random.choice(condiciones_pago_options),
                tiempo_entrega=f"{random.choice([1, 2, 3, 5, 7, 10, 15])} días",
                activo=random.choice([True, True, True, False]),  # 75% activos
                calificacion=random.choice([3, 4, 5]),
                observaciones=fake.paragraph(nb_sentences=2) if random.choice([True, False]) else ''
            )

            proveedores_to_create.append(proveedor)

            # Mostrar progreso cada 5 proveedores
            if (i + 1) % 5 == 0:
                self.stdout.write(f'  ⏳ Progreso: {i + 1}/{count} proveedores preparados...')

        # Inserción masiva
        Proveedor.objects.bulk_create(proveedores_to_create)

        self.stdout.write(self.style.SUCCESS(f'\n✅ {count} proveedores creados exitosamente!'))
        self.stdout.write(self.style.SUCCESS(f'📊 Estadísticas:'))
        self.stdout.write(f'   - Total proveedores: {Proveedor.objects.count()}')
        self.stdout.write(f'   - Proveedores activos: {Proveedor.objects.filter(activo=True).count()}')
        self.stdout.write(f'   - Proveedores inactivos: {Proveedor.objects.filter(activo=False).count()}')
        self.stdout.write(self.style.WARNING('\n' + '=' * 60))

