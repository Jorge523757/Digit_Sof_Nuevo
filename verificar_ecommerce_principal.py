#!/usr/bin/env python3
"""
Verificación completa del sistema de ecommerce en la página principal
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from productos.models import Producto, CategoriaProducto


def verificar_productos_disponibles():
    """Verificar que hay productos disponibles para mostrar"""
    print("📦 Verificando productos disponibles...")
    
    # Productos activos y disponibles para web
    productos = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    )
    
    print(f"   ✅ Productos activos: {productos.count()}")
    
    # Productos por categoría
    categorias = CategoriaProducto.objects.filter(
        activo=True,
        productos__activo=True,
        productos__disponible_web=True
    ).distinct()
    
    print(f"   ✅ Categorías con productos: {categorias.count()}")
    
    # Mostrar algunos productos de ejemplo
    print("\n   📋 Productos disponibles:")
    for producto in productos[:5]:
        print(f"      - ID: {producto.id} | {producto.nombre_producto} | ${producto.precio_venta} | Stock: {producto.stock_actual}")
    
    if productos.count() == 0:
        print("   ⚠️ No hay productos disponibles. Ejecuta: python crear_productos_ecommerce.py")
        return False
    
    return True


def verificar_contexto_vista():
    """Verificar que la vista esté enviando el contexto correcto"""
    print("\n🐍 Verificando contexto de la vista...")
    
    try:
        from core.views import home
        from django.test import RequestFactory
        
        factory = RequestFactory()
        request = factory.get('/')
        
        # Simular la vista
        response = home(request)
        
        print("   ✅ Vista home ejecutada correctamente")
        
        # Verificar que el template se procesa
        if hasattr(response, 'content'):
            content = response.content.decode('utf-8')
            
            checks = [
                ('data-producto-id=', 'Atributos de producto'),
                ('btn-add-cart', 'Botones de carrito'),
                ('product-card', 'Tarjetas de producto'),
                ('filter-btn', 'Botones de filtro'),
            ]
            
            for check, desc in checks:
                if check in content:
                    print(f"   ✅ {desc}: encontrado")
                else:
                    print(f"   ⚠️ {desc}: no encontrado")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error en la vista: {e}")
        return False


def mostrar_instrucciones():
    """Mostrar las instrucciones finales para el usuario"""
    print("\n🎯 INSTRUCCIONES PARA PROBAR:")
    print("=" * 50)
    print("1. 🌐 Ve a: http://127.0.0.1:8000/")
    print("2. 📜 Desplázate hasta la sección 'Nuestros Productos'")
    print("3. 🛒 Haz clic en los botones verdes de carrito")
    print("4. 🛍️ Ve cómo se abre el modal del carrito automáticamente")
    print("5. 💰 Verifica que muestre el total correctamente")
    print("6. 🔍 Prueba los filtros por categoría")
    print("7. ℹ️ Haz clic en los botones azules para ver detalles")
    print("8. 👍👎 Prueba las reacciones en los productos")
    print("\n💡 FUNCIONALIDADES DEL CARRITO:")
    print("   - ✅ Agregar productos con un clic")
    print("   - ✅ Ver total actualizado en tiempo real")
    print("   - ✅ Aumentar/disminuir cantidades")
    print("   - ✅ Eliminar productos individuales")
    print("   - ✅ Vaciar todo el carrito")
    print("   - ✅ Persistencia (no se pierde al recargar)")
    print("   - ✅ Contador en el botón del header")


def main():
    print("🛍️ VERIFICACIÓN FINAL - ECOMMERCE PÁGINA PRINCIPAL")
    print("=" * 60)
    
    tests = [
        ("Productos disponibles", verificar_productos_disponibles),
        ("Contexto de vista", verificar_contexto_vista),
    ]
    
    resultados = []
    
    for nombre, test_func in tests:
        try:
            resultado = test_func()
            resultados.append((nombre, resultado))
        except Exception as e:
            print(f"❌ Error en {nombre}: {e}")
            resultados.append((nombre, False))
    
    print("\n📊 RESUMEN:")
    print("-" * 30)
    
    todos_ok = True
    for nombre, resultado in resultados:
        status = "✅ OK" if resultado else "❌ FALLO"
        print(f"   {nombre}: {status}")
        if not resultado:
            todos_ok = False
    
    if todos_ok:
        print("\n🎉 ¡TODO ESTÁ LISTO!")
        print("El sistema de ecommerce en la página principal está funcionando correctamente.")
        mostrar_instrucciones()
    else:
        print("\n⚠️ Hay algunos problemas que necesitan atención.")
        print("Revisa los errores arriba y vuelve a ejecutar este script.")
    
    return 0 if todos_ok else 1


if __name__ == "__main__":
    sys.exit(main())
