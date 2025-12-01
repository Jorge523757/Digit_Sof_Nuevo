#!/usr/bin/env python3
"""
Script de prueba para verificar productos en la página principal
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto
from core.views import home
from django.test import RequestFactory


def test_productos_disponibles():
    """Verificar productos disponibles"""
    print("📦 Verificando productos disponibles...")

    productos = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    ).select_related('categoria')

    print(f"   ✅ Total productos activos: {productos.count()}")

    if productos.count() == 0:
        print("   ⚠️ No hay productos. Ejecutando script de creación...")
        os.system('python crear_productos_ecommerce.py')
        productos = Producto.objects.filter(
            activo=True,
            disponible_web=True,
            stock_actual__gt=0
        ).select_related('categoria')
        print(f"   ✅ Productos después de creación: {productos.count()}")

    # Mostrar algunos productos
    print("\n   📋 Productos que deberían aparecer:")
    for i, producto in enumerate(productos[:6], 1):
        print(f"      {i}. {producto.nombre_producto} - ${producto.precio_venta} - {producto.categoria.nombre if producto.categoria else 'Sin categoría'}")

    return productos.count() > 0


def test_vista_contexto():
    """Verificar que la vista envía el contexto correctamente"""
    print("\n🐍 Verificando contexto de la vista...")

    factory = RequestFactory()
    request = factory.get('/')

    try:
        response = home(request)
        print("   ✅ Vista ejecutada correctamente")

        # Verificar contexto
        context = response.context_data
        categorias_con_productos = context.get('categorias_con_productos', [])

        print(f"   ✅ Categorías en contexto: {len(categorias_con_productos)}")

        total_productos = 0
        for categoria_data in categorias_con_productos:
            productos_count = len(categoria_data['productos'])
            total_productos += productos_count
            print(f"      - {categoria_data['categoria'].nombre}: {productos_count} productos")

        print(f"   ✅ Total productos en contexto: {total_productos}")

        return total_productos > 0

    except Exception as e:
        print(f"   ❌ Error en la vista: {e}")
        return False


def main():
    print("🔍 VERIFICACIÓN DE PRODUCTOS EN PÁGINA PRINCIPAL")
    print("=" * 55)

    # Test 1: Productos disponibles
    productos_ok = test_productos_disponibles()

    # Test 2: Contexto de vista
    contexto_ok = test_vista_contexto()

    print("\n" + "=" * 55)
    print("📊 RESUMEN:")
    print(f"   Productos disponibles: {'✅ OK' if productos_ok else '❌ FALLO'}")
    print(f"   Contexto de vista: {'✅ OK' if contexto_ok else '❌ FALLO'}")

    if productos_ok and contexto_ok:
        print("\n🎉 ¡TODO ESTÁ CORRECTO!")
        print("Los productos de tu base de datos deberían aparecer en:")
        print("👉 http://127.0.0.1:8000/#productos")
        print("\n💡 Si aún no aparecen, recarga la página (Ctrl+F5)")
        print("   y verifica que no haya errores en la consola del navegador.")
    else:
        print("\n⚠️ Hay problemas que necesitan atención.")
        if not productos_ok:
            print("   - Ejecuta: python crear_productos_ecommerce.py")
        if not contexto_ok:
            print("   - Revisa el archivo core/views.py")


if __name__ == "__main__":
    main()
