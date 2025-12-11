"""
Script para agregar campos de usuario a Compras y Ventas
"""

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Agrega campos de usuario a los modelos de Compras y Ventas'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            try:
                # Agregar campo usuario a Compras
                self.stdout.write('Agregando campo usuario a Compras...')
                cursor.execute("""
                    ALTER TABLE compras 
                    ADD COLUMN usuario_id INTEGER NULL;
                """)
                self.stdout.write(self.style.SUCCESS('✅ Campo usuario agregado a Compras'))
            except Exception as e:
                if 'duplicate column name' in str(e).lower():
                    self.stdout.write(self.style.WARNING('⚠️  Campo usuario ya existe en Compras'))
                else:
                    self.stdout.write(self.style.ERROR(f'❌ Error en Compras: {e}'))

            try:
                # Agregar campo usuario a Ventas
                self.stdout.write('Agregando campo usuario a Ventas...')
                cursor.execute("""
                    ALTER TABLE ventas 
                    ADD COLUMN usuario_id INTEGER NULL;
                """)
                self.stdout.write(self.style.SUCCESS('✅ Campo usuario agregado a Ventas'))
            except Exception as e:
                if 'duplicate column name' in str(e).lower():
                    self.stdout.write(self.style.WARNING('⚠️  Campo usuario ya existe en Ventas'))
                else:
                    self.stdout.write(self.style.ERROR(f'❌ Error en Ventas: {e}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Proceso completado'))

