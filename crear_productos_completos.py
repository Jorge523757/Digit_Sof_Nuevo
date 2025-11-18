"""
Script para crear productos de prueba con todos los campos necesarios
"""
from productos.models import Producto, CategoriaProducto
from decimal import Decimal

# Crear categorías
categorias_data = [
    {"nombre": "Laptops", "descripcion": "Computadoras portátiles"},
    {"nombre": "Monitores", "descripcion": "Pantallas y monitores"},
    {"nombre": "Accesorios", "descripcion": "Periféricos y accesorios"},
    {"nombre": "Computadoras de Escritorio", "descripcion": "PCs de escritorio"},
]

categorias = {}
for cat_data in categorias_data:
    cat, created = CategoriaProducto.objects.get_or_create(
        nombre=cat_data["nombre"],
        defaults={"descripcion": cat_data["descripcion"], "activo": True}
    )
    categorias[cat_data["nombre"]] = cat
    print(f"{'Creada' if created else 'Existente'} categoría: {cat.nombre}")

# Crear productos
productos_data = [
    {
        "nombre_producto": "Laptop Gamer Nitro 5",
        "codigo_sku": "LAP-NIT-001",
        "categoria": "Laptops",
        "modelo_equipo": "AN515-57",
        "marca": "Acer",
        "procesador": "Intel Core i7-11800H",
        "memoria_ram": "16GB DDR4",
        "memoria_rom": "512GB SSD NVMe",
        "descripcion": "Laptop gaming de alto rendimiento con tarjeta gráfica NVIDIA RTX 3060",
        "precio_venta": Decimal("1099.99"),
        "precio_compra": Decimal("900.00"),
        "stock_actual": 8,
        "stock_minimo": 2,
        "disponible_web": True,
        "destacado": True,
    },
    {
        "nombre_producto": "Monitor 27\" 4K",
        "codigo_sku": "MON-4K-001",
        "categoria": "Monitores",
        "modelo_equipo": "U2720Q",
        "marca": "Dell",
        "descripcion": "Monitor profesional 4K UHD con tecnología IPS y puerto USB-C",
        "precio_venta": Decimal("349.99"),
        "precio_compra": Decimal("280.00"),
        "stock_actual": 15,
        "stock_minimo": 3,
        "disponible_web": True,
        "destacado": False,
    },
    {
        "nombre_producto": "Computadora All-In-One",
        "codigo_sku": "PC-AIO-001",
        "categoria": "Computadoras de Escritorio",
        "modelo_equipo": "Pavilion 24",
        "marca": "HP",
        "procesador": "AMD Ryzen 7",
        "memoria_ram": "32GB",
        "memoria_rom": "1TB SSD",
        "descripcion": "PC todo en uno con pantalla táctil de 24 pulgadas y excelente rendimiento",
        "precio_venta": Decimal("799.99"),
        "precio_compra": Decimal("650.00"),
        "stock_actual": 5,
        "stock_minimo": 2,
        "disponible_web": True,
        "destacado": True,
    },
    {
        "nombre_producto": "Mouse Inalámbrico",
        "codigo_sku": "ACC-MOU-001",
        "categoria": "Accesorios",
        "modelo_equipo": "MX Master 3S",
        "marca": "Logitech",
        "descripcion": "Mouse ergonómico inalámbrico con sensor de alta precisión y batería de larga duración",
        "precio_venta": Decimal("29.99"),
        "precio_compra": Decimal("20.00"),
        "stock_actual": 25,
        "stock_minimo": 5,
        "disponible_web": True,
        "destacado": False,
    },
    {
        "nombre_producto": "Laptop ASUS VivoBook",
        "codigo_sku": "LAP-VIV-001",
        "categoria": "Laptops",
        "modelo_equipo": "VivoBook 15",
        "marca": "ASUS",
        "procesador": "Intel Core i5-1135G7",
        "memoria_ram": "8GB DDR4",
        "memoria_rom": "256GB SSD",
        "descripcion": "Laptop ultradelgada ideal para trabajo y estudio",
        "precio_venta": Decimal("749.99"),
        "precio_compra": Decimal("600.00"),
        "stock_actual": 12,
        "stock_minimo": 3,
        "disponible_web": True,
        "destacado": False,
    },
]

created_count = 0
updated_count = 0

for prod_data in productos_data:
    categoria_nombre = prod_data.pop("categoria")
    categoria = categorias[categoria_nombre]
    
    producto, created = Producto.objects.update_or_create(
        codigo_sku=prod_data["codigo_sku"],
        defaults={
            **prod_data,
            "categoria": categoria,
            "activo": True,
            "tiene_garantia": True,
            "meses_garantia": 12,
        }
    )
    
    if created:
        created_count += 1
        print(f"✅ Creado: {producto.nombre_producto}")
    else:
        updated_count += 1
        print(f"🔄 Actualizado: {producto.nombre_producto}")

print(f"\n✅ Proceso completado!")
print(f"📦 Productos creados: {created_count}")
print(f"🔄 Productos actualizados: {updated_count}")
print(f"📊 Total de productos: {Producto.objects.filter(disponible_web=True, activo=True).count()}")

