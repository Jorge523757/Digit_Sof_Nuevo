"""
Script simplificado para crear productos vía manage.py shell
"""

# Importaciones
from productos.models import CategoriaProducto, Producto
from decimal import Decimal

# Crear categoría
categoria, created = CategoriaProducto.objects.get_or_create(
    nombre="Accesorios para Laptops",
    defaults={
        'descripcion': "Accesorios y protectores para laptops y notebooks",
        'activo': True
    }
)

print(f"Categoría: {categoria.nombre} ({'creada' if created else 'existente'})")

# Crear productos
productos_data = [
    {
        'nombre_producto': 'Funda de silicona para teclado HP Victus 15 2022 2021',
        'codigo_sku': 'HP-VICTUS-15-SILICONA-001',
        'modelo_equipo': 'HP Victus 15-fb0019ax 15-fa0000ni',
        'marca': 'Compatible HP',
        'descripcion': 'Protector de teclado transparente TPU para HP Victus Gaming Laptop. Material premium que protege contra polvo, líquidos y desgaste.',
        'especificaciones': 'Material: TPU, Color: Transparente, Compatible: HP Victus 15/16',
        'precio_compra': Decimal('15000'),
        'precio_venta': Decimal('23965'),
        'precio_mayorista': Decimal('19000'),
        'stock_actual': 95,
        'destacado': True,
        'categoria': categoria,
        'activo': True,
        'disponible_web': True,
    },
    {
        'nombre_producto': 'Nueva funda superior para ordenador portátil HP Victus 16.1',
        'codigo_sku': 'HP-VICTUS-16-FUNDA-002',
        'modelo_equipo': 'HP Victus 16.1 pulgadas',
        'marca': 'OEM Compatible',
        'descripcion': 'Funda protectora superior de alta calidad para laptop HP Victus 16.1 pulgadas. Material premium PC+ABS.',
        'especificaciones': 'Material: PC+ABS, Tamaño: 16.1", Diseño: Ultra delgado, Protección 360 grados',
        'precio_compra': Decimal('45000'),
        'precio_venta': Decimal('107212'),
        'precio_mayorista': Decimal('85000'),
        'stock_actual': 16,
        'destacado': True,
        'categoria': categoria,
        'activo': True,
        'disponible_web': True,
    },
    {
        'nombre_producto': 'Para HP Victus 16.1 Cubierta de silicona colorida',
        'codigo_sku': 'HP-VICTUS-CUBIERTA-003',
        'modelo_equipo': 'HP Victus 16.1',
        'marca': 'Generic',
        'descripcion': 'Cubierta protectora de silicona en múltiples colores para HP Victus 16.1. Diseño moderno y protección efectiva.',
        'especificaciones': 'Material: Silicona premium, Colores: Negro/Azul/Rosa/Verde/Transparente',
        'precio_compra': Decimal('8000'),
        'precio_venta': Decimal('12154'),
        'precio_mayorista': Decimal('9500'),
        'stock_actual': 412,
        'destacado': False,
        'categoria': categoria,
        'activo': True,
        'disponible_web': True,
    },
]

# Crear cada producto
for prod_data in productos_data:
    producto, created = Producto.objects.get_or_create(
        codigo_sku=prod_data['codigo_sku'],
        defaults=prod_data
    )
    
    if created:
        print(f"✅ Creado: {producto.nombre_producto} - ${producto.precio_venta:,.0f}")
    else:
        print(f"📦 Ya existe: {producto.nombre_producto}")

print(f"\n📊 Total productos activos: {Producto.objects.filter(activo=True, disponible_web=True).count()}")
print("✅ ¡Productos creados exitosamente!")
