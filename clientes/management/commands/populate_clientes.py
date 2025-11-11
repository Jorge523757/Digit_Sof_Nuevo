"""
DIGT SOFT - Comando de Gestión para Poblar Clientes
Genera datos de prueba realistas usando Faker
"""

import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from clientes.models import Cliente


class Command(BaseCommand):
    help = 'Pobla la base de datos con clientes de prueba usando Faker'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            default=30,
            nargs='?',
            help='Número de clientes a crear (por defecto: 30)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Eliminar todos los clientes existentes antes de crear nuevos'
        )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        count = kwargs['count']
        clear = kwargs['clear']
        fake = Faker('es_CO')

        # Colores para el output
        self.stdout.write(self.style.WARNING('=' * 60))
        self.stdout.write(self.style.WARNING('👥 DIGIT SOFT - Generador de Clientes'))
        self.stdout.write(self.style.WARNING('=' * 60))

        # Limpiar datos existentes si se especifica
        if clear:
            Cliente.objects.all().delete()
            self.stdout.write(self.style.WARNING('\n🗑️  Clientes existentes eliminados'))

        self.stdout.write(self.style.WARNING(f'\n👤 Creando {count} clientes...'))

        clientes_to_create = []
        documentos_usados = set()

        for i in range(count):
            # Generar documento único
            tipo_doc = random.choice(['CC', 'CE', 'NIT'])
            if tipo_doc == 'NIT':
                numero_documento = fake.unique.numerify(text='##########')
            else:
                numero_documento = fake.unique.numerify(text='##########')

            # Asegurar que sea único
            while numero_documento in documentos_usados or Cliente.objects.filter(numero_documento=numero_documento).exists():
                numero_documento = fake.unique.numerify(text='##########')

            documentos_usados.add(numero_documento)

            # Generar nombres colombianos
            nombres = fake.first_name()
            apellidos = fake.last_name()

            # Teléfonos colombianos
            telefono = fake.phone_number()

            # Email basado en nombre
            email_base = f"{nombres.lower()}.{apellidos.lower()}"
            email = fake.email().replace(fake.email().split('@')[0], email_base.replace(' ', ''))

            # Dirección colombiana
            direccion = f"{fake.street_name()} #{random.randint(10, 99)}-{random.randint(10, 99)}, {fake.city()}"

            # Observaciones aleatorias
            observaciones_options = [
                '',
                'Cliente frecuente',
                'Solicita factura electrónica',
                'Cliente corporativo',
                'Requiere garantía extendida',
                'Mayorista',
                'Comprador ocasional'
            ]

            cliente = Cliente(
                nombres=nombres,
                apellidos=apellidos,
                numero_documento=numero_documento,
                telefono=telefono,
                correo=email,
                direccion=direccion,
                activo=random.choice([True, True, True, False]),  # 75% activos
                observaciones=random.choice(observaciones_options)
            )

            clientes_to_create.append(cliente)

            # Mostrar progreso cada 10 clientes
            if (i + 1) % 10 == 0:
                self.stdout.write(f'  ⏳ Progreso: {i + 1}/{count} clientes preparados...')

        # Inserción masiva
        Cliente.objects.bulk_create(clientes_to_create)

        self.stdout.write(self.style.SUCCESS(f'\n✅ {count} clientes creados exitosamente!'))
        self.stdout.write(self.style.SUCCESS(f'📊 Estadísticas:'))
        self.stdout.write(f'   - Total clientes: {Cliente.objects.count()}')
        self.stdout.write(f'   - Clientes activos: {Cliente.objects.filter(activo=True).count()}')
        self.stdout.write(f'   - Clientes inactivos: {Cliente.objects.filter(activo=False).count()}')
        self.stdout.write(self.style.WARNING('\n' + '=' * 60))

