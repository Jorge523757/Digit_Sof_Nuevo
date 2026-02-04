"""
Comando personalizado para crear superusuario automáticamente
Uso: python manage.py crear_superusuario
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Crea un superusuario predeterminado si no existe'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Nombre de usuario (default: admin)'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@digitsoft.com',
            help='Email del superusuario (default: admin@digitsoft.com)'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='Contraseña del superusuario (default: admin123)'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        # Verificar si ya existe un superusuario
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(
                self.style.WARNING(
                    f'⚠️  Ya existe al menos un superusuario en la base de datos.'
                )
            )

            # Mostrar superusuarios existentes
            superusers = User.objects.filter(is_superuser=True)
            self.stdout.write(self.style.SUCCESS('\n📋 Superusuarios existentes:'))
            for su in superusers:
                self.stdout.write(
                    self.style.SUCCESS(f'   - {su.username} ({su.email})')
                )
            return

        # Crear el superusuario
        try:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'\n✅ Superusuario creado exitosamente!\n'
                )
            )
            self.stdout.write(
                self.style.SUCCESS(f'   👤 Usuario: {username}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'   📧 Email: {email}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'   🔑 Contraseña: {password}')
            )
            self.stdout.write(
                self.style.WARNING(
                    f'\n⚠️  IMPORTANTE: Cambia la contraseña después del primer login!\n'
                )
            )

        except IntegrityError:
            self.stdout.write(
                self.style.ERROR(
                    f'❌ Error: El usuario "{username}" ya existe.'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f'❌ Error al crear superusuario: {str(e)}'
                )
            )

