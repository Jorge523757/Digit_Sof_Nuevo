# Script para crear datos de ejemplo en el sistema de pedidos
# Ejecutar con: python manage.py shell

from apps.ventas.models import Producto, Cliente, Pedido, DetallePedido
from decimal import Decimal
from django.utils import timezone

# Crear productos de ejemplo si no existen
productos_ejemplo = [
    {
        'nombre': 'Laptop Dell Inspiron 15',
        'descripcion': 'Laptop Dell Inspiron 15 con procesador Intel Core i5, 8GB RAM, 256GB SSD',
        'precio': Decimal('2500000.00'),
        'stock': 10,
        'categoria': 'laptop',
        'marca': 'Dell'
    },
    {
        'nombre': 'Mouse Gaming Logitech',
        'descripcion': 'Mouse gaming con sensor óptico de alta precisión, 6 botones programables',
        'precio': Decimal('150000.00'),
        'stock': 25,
        'categoria': 'accesorios',
        'marca': 'Logitech'
    },
    {
        'nombre': 'Teclado Mecánico RGB',
        'descripcion': 'Teclado mecánico con iluminación RGB, switches Cherry MX Blue',
        'precio': Decimal('280000.00'),
        'stock': 15,
        'categoria': 'accesorios',
        'marca': 'Razer'
    },
    {
        'nombre': 'Monitor 24" Full HD',
        'descripcion': 'Monitor LED de 24 pulgadas, resolución Full HD 1920x1080, panel IPS',
        'precio': Decimal('650000.00'),
        'stock': 8,
        'categoria': 'monitor',
        'marca': 'Samsung'
    },
    {
        'nombre': 'Smartphone Samsung Galaxy A54',
        'descripcion': 'Smartphone con pantalla de 6.4", 128GB almacenamiento, cámara triple',
        'precio': Decimal('1200000.00'),
        'stock': 12,
        'categoria': 'smartphone',
        'marca': 'Samsung'
    }
]

# Crear los productos
for prod_data in productos_ejemplo:
    producto, created = Producto.objects.get_or_create(
        nombre=prod_data['nombre'],
        defaults=prod_data
    )
    if created:
        print(f"Producto creado: {producto.nombre}")
    else:
        print(f"Producto ya existe: {producto.nombre}")

# Crear cliente de ejemplo
cliente_data = {
    'nombre': 'Juan Carlos Pérez',
    'cedula': '12345678',
    'telefono': '3001234567',
    'correo': 'juan.perez@email.com',
    'direccion': 'Calle 123 # 45-67, Bogotá'
}

cliente, created = Cliente.objects.get_or_create(
    cedula=cliente_data['cedula'],
    defaults=cliente_data
)

if created:
    print(f"Cliente creado: {cliente.nombre}")
else:
    print(f"Cliente ya existe: {cliente.nombre}")

print("\n¡Datos de ejemplo creados exitosamente!")
print("\nPuedes probar el sistema:")
print("1. Ve a http://127.0.0.1:8000/ventas/catalogo/ para ver el catálogo público")
print("2. Ve a http://127.0.0.1:8000/ventas/admin/pedidos/ para el panel de administración")
print("3. Crea un pedido desde el catálogo y luego procésalo desde el panel admin")