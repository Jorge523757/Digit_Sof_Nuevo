#!/usr/bin/env python3
"""
Test específico para la página de productos ecommerce
"""

import os
import sys
import django
import requests
import time

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto


def test_datos_productos():
    """Test de datos disponibles para la página"""
    print("🧪 Testing datos de productos...")

    # Productos activos y disponibles para web
    productos_web = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    ).select_related('categoria')

    print(f"   ✅ Productos disponibles: {productos_web.count()}")

    # Categorías con productos
    categorias = CategoriaProducto.objects.filter(
        activo=True,
        productos__activo=True,
        productos__disponible_web=True
    ).distinct()

    print(f"   ✅ Categorías con productos: {categorias.count()}")

    # Productos destacados
    destacados = productos_web.filter(destacado=True)
    print(f"   ✅ Productos destacados: {destacados.count()}")

    # Mostrar algunos productos de ejemplo
    print("\n   📦 Productos de ejemplo:")
    for producto in productos_web[:5]:
        print(f"      - {producto.nombre_producto}: ${producto.precio_venta}")

    return productos_web.count() > 0


def test_pagina_productos():
    """Test de la página web de productos"""
    print("🌐 Testing página de productos...")

    try:
        response = requests.get("http://127.0.0.1:8000/main/productos/", timeout=10)

        if response.status_code == 200:
            print("   ✅ Página responde correctamente")

            # Verificar contenido clave
            content = response.text
            checks = [
                ("Tienda DigitSoft", "Título de la tienda"),
                ("btn-add-cart-ecommerce", "Botones de carrito"),
                ("btn-ver-detalle-ecommerce", "Botones de detalles"),
                ("reaction-btn-ecommerce", "Botones de reacciones"),
                ("products-grid-ecommerce", "Grid de productos"),
                ("cart-button-main", "Botón principal del carrito"),
            ]

            for check, description in checks:
                if check in content:
                    print(f"   ✅ {description}: encontrado")
                else:
                    print(f"   ⚠️ {description}: no encontrado")

            return True
        else:
            print(f"   ❌ Error HTTP: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"   ❌ Error de conexión: {e}")
        return False


def test_vista_django():
    """Test de la vista de Django"""
    print("🐍 Testing vista de Django...")

    try:
        from main.productos.views import index
        from django.test import RequestFactory

        factory = RequestFactory()
        request = factory.get('/main/productos/')

        response = index(request)

        if hasattr(response, 'status_code') and response.status_code == 200:
            print("   ✅ Vista responde correctamente")
            return True
        else:
            print("   ❌ Vista no responde correctamente")
            return False

    except Exception as e:
        print(f"   ❌ Error en vista: {e}")
        return False


def main():
    print("🛍️ TEST COMPLETO - PÁGINA DE PRODUCTOS ECOMMERCE")
    print("=" * 60)

    tests = [
        ("Datos de productos", test_datos_productos),
        ("Vista Django", test_vista_django),
        ("Página web", test_pagina_productos),
    ]

    resultados = []

    for nombre, test_func in tests:
        print(f"\n{nombre}:")
        try:
            resultado = test_func()
            resultados.append((nombre, resultado))
        except Exception as e:
            print(f"   ❌ Error: {e}")
            resultados.append((nombre, False))

    print("\n" + "=" * 60)
    print("📊 RESUMEN FINAL:")

    todos_ok = True
    for nombre, resultado in resultados:
        status = "✅ OK" if resultado else "❌ FALLO"
        print(f"   {nombre}: {status}")
        if not resultado:
            todos_ok = False

    if todos_ok:
        print("\n🎉 ¡TODOS LOS TESTS PASARON!")
        print("\n📝 Para probar la página:")
        print("   1. Asegúrate de que el servidor esté corriendo:")
        print("      python manage.py runserver")
        print("   2. Ve a: http://127.0.0.1:8000/main/productos/")
        print("   3. Prueba los botones de carrito (🛒)")
        print("   4. Prueba los botones de detalles (ℹ️)")
        print("   5. Prueba las reacciones (👍👎)")
        print("   6. Prueba los filtros por categoría")
    else:
        print("\n⚠️ Algunos tests fallaron. Revisa la configuración.")

    return 0 if todos_ok else 1


if __name__ == "__main__":
    sys.exit(main())
