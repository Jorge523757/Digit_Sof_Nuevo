"""
Comando de management que ejecuta el generador de datos de prueba existente
Sin modificar el diseño de salida; llama a las funciones del script
"""
import importlib
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Ejecuta el generador de datos de prueba definido en generar_datos_prueba.py'

    def add_arguments(self, parser):
        parser.add_argument(
            '--yes', '-y',
            action='store_true',
            help='No preguntar confirmación y ejecutar directamente (útil para CI)'
        )

    def handle(self, *args, **options):
        yes = options.get('yes', False)

        try:
            gen = importlib.import_module('generar_datos_prueba')
        except Exception as e:
            self.stderr.write(f"Error al importar módulo 'generar_datos_prueba': {e}")
            raise

        # Si se solicita bypass de confirmación, evitamos la función main (que pide input())
        # y llamamos directamente a las funciones de generación para conservar la salida.
        try:
            if yes:
                clientes = gen.generar_clientes(20)
                categorias = gen.generar_categorias()
                productos = gen.generar_productos(categorias, 30)
                ventas = gen.generar_ventas(clientes, productos, 15)
                gen.mostrar_resumen(clientes, productos, ventas)
            else:
                # Para preservar el comportamiento original (incluida la confirmación),
                # llamamos a main() del script — este imprimirá y pedirá confirmación.
                if hasattr(gen, 'main'):
                    gen.main()
                else:
                    # Fallback: llamar a las funciones si main no existe
                    clientes = gen.generar_clientes(20)
                    categorias = gen.generar_categorias()
                    productos = gen.generar_productos(categorias, 30)
                    ventas = gen.generar_ventas(clientes, productos, 15)
                    gen.mostrar_resumen(clientes, productos, ventas)

        except Exception as e:
            self.stderr.write(f"Error al ejecutar el generador: {e}")
            raise
