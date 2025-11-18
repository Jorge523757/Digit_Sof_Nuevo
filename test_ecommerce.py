#!/usr/bin/env python3
"""
Test rápido del sistema de ecommerce
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto, ReaccionProducto


def test_productos():
    """Test de productos disponibles"""
    print("🧪 Testing productos...")
    
    # Productos totales
    total = Producto.objects.count()
    print(f"   Total productos: {total}")
    
    # Productos web
    web = Producto.objects.filter(disponible_web=True, activo=True).count()
    print(f"   Disponibles en web: {web}")
    
    # Productos con stock
    con_stock = Producto.objects.filter(stock_actual__gt=0).count()
    print(f"   Con stock: {con_stock}")
    
    # Productos destacados
    destacados = Producto.objects.filter(destacado=True).count()
    print(f"   Destacados: {destacados}")
    
    return total > 0


def test_categorias():
    """Test de categorías"""
    print("🧪 Testing categorías...")
    
    categorias = CategoriaProducto.objects.filter(activo=True)
    print(f"   Categorías activas: {categorias.count()}")
    
    for cat in categorias:
        productos_count = cat.productos.filter(disponible_web=True, activo=True).count()
        print(f"   - {cat.nombre}: {productos_count} productos")
    
    return categorias.count() > 0


def test_api_data():
    """Test de datos que devolvería la API"""
    print("🧪 Testing estructura de datos de API...")
    
    productos = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    ).select_related('categoria')[:5]
    
    for producto in productos:
        data = {
            'id': producto.id,
            'nombre': producto.nombre_producto,
            'codigo': producto.codigo_sku,
            'categoria': producto.categoria.nombre if producto.categoria else 'Sin categoría',
            'precio': float(producto.precio_venta),
            'stock': producto.stock_actual,
        }
        print(f"   ✅ {data['nombre']}: ${data['precio']} ({data['stock']} unidades)")
    
    return productos.count() > 0


def main():
    print("🚀 Test del Sistema de E-commerce")
    print("=" * 50)
    
    tests = [
        ("Productos", test_productos),
        ("Categorías", test_categorias),
        ("Datos API", test_api_data),
    ]
    
    resultados = []
    
    for nombre, test_func in tests:
        try:
            print(f"\n{nombre}:")
            resultado = test_func()
            resultados.append((nombre, resultado))
            print(f"   Estado: {'✅ OK' if resultado else '❌ FALLO'}")
        except Exception as e:
            print(f"   Error: {e}")
            resultados.append((nombre, False))
    
    print("\n" + "=" * 50)
    print("📊 RESUMEN:")
    
    todos_ok = True
    for nombre, resultado in resultados:
        estado = "✅ OK" if resultado else "❌ FALLO"
        print(f"   {nombre}: {estado}")
        if not resultado:
            todos_ok = False
    
    if todos_ok:
        print("\n🎉 ¡Todos los tests pasaron! El sistema está listo.")
        print("\n📝 Pasos siguientes:")
        print("   1. Inicia el servidor: python manage.py runserver")
        print("   2. Ve a http://127.0.0.1:8000/#contacto")
        print("   3. Prueba los botones de carrito y detalles")
    else:
        print("\n⚠️ Algunos tests fallaron. Revisa la configuración.")
    
    return 0 if todos_ok else 1


if __name__ == "__main__":
    sys.exit(main())
