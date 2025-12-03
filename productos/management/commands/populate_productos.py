"""
DIGT SOFT - Comando de Gestión para Poblar Productos
Genera datos de prueba realistas usando Faker
"""

import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from productos.models import Producto, CategoriaProducto


class Command(BaseCommand):
    help = 'Pobla la base de datos con productos y categorías de prueba usando Faker'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            default=50,
            nargs='?',
            help='Número de productos a crear (por defecto: 50)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Eliminar todos los productos existentes antes de crear nuevos'
        )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        count = kwargs['count']
        clear = kwargs['clear']
        fake = Faker('es_CO')

        # Colores para el output
        self.stdout.write(self.style.WARNING('=' * 60))
        self.stdout.write(self.style.WARNING('🚀 DIGIT SOFT - Generador de Datos de Prueba'))
        self.stdout.write(self.style.WARNING('=' * 60))

        # Limpiar datos existentes si se especifica
        if clear:
            Producto.objects.all().delete()
            CategoriaProducto.objects.all().delete()
            self.stdout.write(self.style.WARNING('\n🗑️  Datos existentes eliminados'))

        # Crear categorías si no existen
        categorias_data = [
            {'nombre': 'Computadores y Laptops', 'descripcion': 'Equipos de cómputo portátiles y de escritorio'},
            {'nombre': 'Componentes de Hardware', 'descripcion': 'Procesadores, memorias RAM, discos duros, tarjetas gráficas'},
            {'nombre': 'Periféricos', 'descripcion': 'Teclados, mouse, monitores, impresoras'},
            {'nombre': 'Smartphones y Tablets', 'descripcion': 'Dispositivos móviles y tablets'},
            {'nombre': 'Accesorios Tecnológicos', 'descripcion': 'Cables, adaptadores, fundas, cargadores'},
            {'nombre': 'Redes y Comunicaciones', 'descripcion': 'Routers, switches, access points'},
            {'nombre': 'Audio y Video', 'descripcion': 'Auriculares, parlantes, cámaras web'},
        ]

        categorias = []
        for cat_data in categorias_data:
            categoria, created = CategoriaProducto.objects.get_or_create(
                nombre=cat_data['nombre'],
                defaults={'descripcion': cat_data['descripcion']}
            )
            categorias.append(categoria)

        self.stdout.write(self.style.SUCCESS(f'\n✅ {len(categorias)} categorías preparadas'))
        self.stdout.write(self.style.WARNING(f'\n📦 Creando {count} productos...'))

        # Datos para productos tecnológicos realistas
        marcas_computadores = ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Apple', 'MSI', 'Samsung']
        marcas_smartphones = ['Samsung', 'Apple', 'Xiaomi', 'Huawei', 'Motorola', 'OPPO', 'Realme']
        procesadores = ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Intel Core i9', 'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7', 'AMD Ryzen 9']
        ram_options = ['4GB', '8GB', '16GB', '32GB', '64GB']
        storage_options = ['128GB SSD', '256GB SSD', '512GB SSD', '1TB SSD', '1TB HDD', '2TB HDD']

        productos_to_create = []

        for i in range(count):
            categoria = random.choice(categorias)
            marca = random.choice(marcas_computadores if 'Computador' in categoria.nombre or 'Hardware' in categoria.nombre else marcas_smartphones)

            # Generar nombre de producto realista
            if 'Computador' in categoria.nombre:
                modelo = f"{marca} {random.choice(['Pavilion', 'Inspiron', 'ThinkPad', 'VivoBook', 'Aspire', 'MacBook'])}"
                nombre = f"{modelo} {random.choice(procesadores)}"
            elif 'Smartphone' in categoria.nombre:
                serie = random.choice(['Galaxy S', 'Galaxy A', 'iPhone', 'Redmi', 'P', 'Moto G'])
                nombre = f"{marca} {serie}{random.randint(10, 50)}"
            else:
                nombre = f"{marca} {fake.word().title()} {random.choice(['Pro', 'Plus', 'Max', 'Ultra', 'Lite', ''])}"

            # Generar SKU único
            codigo_sku = f"PROD-{marca[:3].upper()}-{random.randint(10000, 99999)}"

            # Asegurar SKU único
            while Producto.objects.filter(codigo_sku=codigo_sku).exists() or any(p.codigo_sku == codigo_sku for p in productos_to_create):
                codigo_sku = f"PROD-{marca[:3].upper()}-{random.randint(10000, 99999)}"

            # Precios realistas
            precio_compra = random.uniform(100000, 5000000)
            margen = random.uniform(1.15, 1.40)  # 15% a 40% de margen
            precio_venta = precio_compra * margen
            precio_mayorista = precio_venta * 0.90  # 10% menos que precio de venta

            # Crear producto
            producto = Producto(
                nombre_producto=nombre,
                codigo_sku=codigo_sku,
                categoria=categoria,
                modelo_equipo=f"{marca}-{random.randint(100, 999)}",
                marca=marca,
                procesador=random.choice(procesadores) if 'Computador' in categoria.nombre else '',
                memoria_ram=random.choice(ram_options) if 'Computador' in categoria.nombre or 'Smartphone' in categoria.nombre else '',
                memoria_rom=random.choice(storage_options),
                descripcion=fake.paragraph(nb_sentences=4),
                especificaciones=self._generar_especificaciones(categoria.nombre),
                precio_compra=round(precio_compra, 2),
                precio_venta=round(precio_venta, 2),
                precio_mayorista=round(precio_mayorista, 2),
                stock_actual=random.randint(0, 100),
                stock_minimo=random.randint(5, 15),
                stock_maximo=random.randint(50, 200),
                disponible_web=random.choice([True, True, True, False]),  # 75% disponible en web
                destacado=random.choice([True, False, False, False]),  # 25% destacados
                activo=True,
                tiene_garantia=True,
                meses_garantia=random.choice([3, 6, 12, 24])
            )

            productos_to_create.append(producto)

            # Mostrar progreso cada 10 productos
            if (i + 1) % 10 == 0:
                self.stdout.write(f'  ⏳ Progreso: {i + 1}/{count} productos preparados...')

        # Inserción masiva
        Producto.objects.bulk_create(productos_to_create)

        self.stdout.write(self.style.SUCCESS(f'\n✅ {count} productos creados exitosamente!'))
        self.stdout.write(self.style.SUCCESS(f'📊 Estadísticas:'))
        self.stdout.write(f'   - Total categorías: {CategoriaProducto.objects.count()}')
        self.stdout.write(f'   - Total productos: {Producto.objects.count()}')
        self.stdout.write(f'   - Productos destacados: {Producto.objects.filter(destacado=True).count()}')
        self.stdout.write(f'   - Productos disponibles web: {Producto.objects.filter(disponible_web=True).count()}')
        self.stdout.write(self.style.WARNING('\n' + '=' * 60))

    def _generar_especificaciones(self, categoria_nombre):
        """Genera especificaciones técnicas realistas según la categoría"""
        specs = []

        if 'Computador' in categoria_nombre:
            specs = [
                f"• Sistema Operativo: {random.choice(['Windows 11', 'Windows 10', 'macOS', 'Linux Ubuntu'])}",
                f"• Pantalla: {random.choice(['13.3', '14', '15.6', '17.3'])}\" {random.choice(['HD', 'Full HD', '4K'])}",
                f"• Conectividad: WiFi 6, Bluetooth 5.0",
                f"• Puertos: {random.randint(2, 4)} USB, HDMI, Audio",
                f"• Batería: {random.randint(4, 10)} horas"
            ]
        elif 'Smartphone' in categoria_nombre:
            specs = [
                f"• Pantalla: {random.uniform(5.5, 6.8):.1f}\" {random.choice(['AMOLED', 'IPS LCD', 'Super AMOLED'])}",
                f"• Cámara: {random.choice(['12MP', '48MP', '64MP', '108MP'])} principal",
                f"• Batería: {random.randint(3000, 5000)}mAh",
                f"• Sistema: {random.choice(['Android 13', 'Android 14', 'iOS 17', 'iOS 16'])}",
                f"• Conectividad: 4G/5G, WiFi, Bluetooth"
            ]
        else:
            specs = [
                f"• Material: {random.choice(['Plástico', 'Metal', 'Aluminio', 'Fibra de carbono'])}",
                f"• Peso: {random.randint(100, 2000)}g",
                f"• Dimensiones: {random.randint(10, 50)} x {random.randint(10, 50)} x {random.randint(1, 10)} cm",
                f"• Garantía: {random.choice([3, 6, 12, 24])} meses"
            ]

        return '\n'.join(specs)
# Management module for productos app

