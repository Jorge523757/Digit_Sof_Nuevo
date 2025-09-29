import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.ventas.models import Producto, Cliente
from decimal import Decimal

# Crear productos
productos = [
    {
        'nombre': 'Laptop Dell Inspiron 15',
        'descripcion': 'Laptop Dell con procesador Intel i5, 8GB RAM, 256GB SSD',
        'precio': Decimal('2500000.00'),
        'stock': 10,
        'categoria': 'laptop',
        'marca': 'Dell'
    },
    {
        'nombre': 'Mouse Gaming Logitech',
        'descripcion': 'Mouse gaming con sensor óptico de alta precisión',
        'precio': Decimal('150000.00'),
        'stock': 25,
        'categoria': 'accesorios',
        'marca': 'Logitech'
    },
    {
        'nombre': 'Teclado Mecánico RGB',
        'descripcion': 'Teclado mecánico con iluminación RGB',
        'precio': Decimal('280000.00'),
        'stock': 15,
        'categoria': 'accesorios',
        'marca': 'Razer'
    },
    {
        'nombre': 'Monitor 24 Full HD',
        'descripcion': 'Monitor LED 24 pulgadas Full HD',
        'precio': Decimal('650000.00'),
        'stock': 8,
        'categoria': 'monitor',
        'marca': 'Samsung'
    }
]

for prod_data in productos:
    producto, created = Producto.objects.get_or_create(
        nombre=prod_data['nombre'],
        defaults=prod_data
    )
    if created:
        print(f"✓ Producto creado: {producto.nombre}")
    else:
        print(f"○ Producto ya existe: {producto.nombre}")

print("\n¡Datos creados exitosamente!")
print("Ahora puedes probar el sistema en:")
print("• http://127.0.0.1:8000/ventas/catalogo/ (para clientes)")
print("• http://127.0.0.1:8000/ventas/admin/pedidos/ (para administradores)")