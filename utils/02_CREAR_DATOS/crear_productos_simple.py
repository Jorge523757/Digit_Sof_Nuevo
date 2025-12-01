import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto
from decimal import Decimal

# Crear categorías
cat1, _ = CategoriaProducto.objects.get_or_create(
    nombre='Laptops',
    defaults={'descripcion': 'Portátiles de alta gama', 'activo': True}
)

cat2, _ = CategoriaProducto.objects.get_or_create(
    nombre='Computadoras de Escritorio',
    defaults={'descripcion': 'PCs de escritorio potentes', 'activo': True}
)

cat3, _ = CategoriaProducto.objects.get_or_create(
    nombre='Accesorios',
    defaults={'descripcion': 'Teclados, mouse, audífonos y más', 'activo': True}
)

print("Categorías creadas!")

# Crear productos
Producto.objects.get_or_create(
    codigo_sku='LAP-HP-001',
    defaults={
        'nombre_producto': 'Laptop HP Pavilion 15',
        'categoria': cat1,
        'marca': 'HP',
        'procesador': 'AMD Ryzen 5',
        'memoria_ram': '8GB',
        'memoria_rom': '512GB SSD',
        'descripcion': 'Laptop ideal para trabajo y estudio',
        'precio_compra': Decimal('450.00'),
        'precio_venta': Decimal('650.00'),
        'precio_mayorista': Decimal('600.00'),
        'stock_actual': 10,
        'disponible_web': True,
        'destacado': True,
        'activo': True,
    }
)

Producto.objects.get_or_create(
    codigo_sku='LAP-LEN-002',
    defaults={
        'nombre_producto': 'Laptop Lenovo IdeaPad 3',
        'categoria': cat1,
        'marca': 'Lenovo',
        'procesador': 'Intel Core i5',
        'memoria_ram': '8GB',
        'memoria_rom': '256GB SSD',
        'descripcion': 'Laptop económica para estudiantes',
        'precio_compra': Decimal('400.00'),
        'precio_venta': Decimal('580.00'),
        'precio_mayorista': Decimal('530.00'),
        'stock_actual': 15,
        'disponible_web': True,
        'activo': True,
    }
)

Producto.objects.get_or_create(
    codigo_sku='PC-GAM-001',
    defaults={
        'nombre_producto': 'PC Gamer RGB Master',
        'categoria': cat2,
        'marca': 'Ensamblado',
        'procesador': 'AMD Ryzen 7',
        'memoria_ram': '32GB',
        'memoria_rom': '1TB SSD',
        'descripcion': 'PC Gamer de alta gama con RTX 3070',
        'precio_compra': Decimal('1200.00'),
        'precio_venta': Decimal('1800.00'),
        'precio_mayorista': Decimal('1600.00'),
        'stock_actual': 5,
        'disponible_web': True,
        'destacado': True,
        'activo': True,
    }
)

Producto.objects.get_or_create(
    codigo_sku='ACC-TEC-001',
    defaults={
        'nombre_producto': 'Teclado Mecánico RGB K95',
        'categoria': cat3,
        'marca': 'Corsair',
        'descripcion': 'Teclado mecánico gaming con switches Cherry MX',
        'precio_compra': Decimal('80.00'),
        'precio_venta': Decimal('130.00'),
        'precio_mayorista': Decimal('110.00'),
        'stock_actual': 25,
        'disponible_web': True,
        'destacado': True,
        'activo': True,
    }
)

Producto.objects.get_or_create(
    codigo_sku='ACC-MOU-002',
    defaults={
        'nombre_producto': 'Mouse Gamer Logitech G502',
        'categoria': cat3,
        'marca': 'Logitech',
        'descripcion': 'Mouse gaming de alta precisión',
        'precio_compra': Decimal('45.00'),
        'precio_venta': Decimal('75.00'),
        'precio_mayorista': Decimal('65.00'),
        'stock_actual': 30,
        'disponible_web': True,
        'activo': True,
    }
)

print(f"Productos creados! Total: {Producto.objects.count()}")
print("¡Listo! Ahora puedes ver los productos en http://127.0.0.1:8000/")

