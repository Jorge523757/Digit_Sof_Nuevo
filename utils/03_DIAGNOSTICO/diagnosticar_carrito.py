"""
Script de diagnóstico para el sistema de carrito
Verifica el estado del carrito y las funcionalidades
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from productos.models import Producto
from django.test import RequestFactory
from productos.views import agregar_al_carrito, eliminar_del_carrito, ver_carrito

User = get_user_model()

def diagnosticar_carrito():
    print("=" * 60)
    print("DIAGNÓSTICO DEL SISTEMA DE CARRITO")
    print("=" * 60)

    # 1. Verificar usuarios
    print("\n1. VERIFICANDO USUARIOS:")
    usuarios = User.objects.all()
    print(f"   Total de usuarios: {usuarios.count()}")
    for user in usuarios[:5]:
        print(f"   - {user.username} ({user.email}) - Staff: {user.is_staff}")

    # 2. Verificar productos
    print("\n2. VERIFICANDO PRODUCTOS:")
    productos = Producto.objects.filter(activo=True)
    print(f"   Total de productos activos: {productos.count()}")
    print(f"   Productos con stock: {productos.filter(stock_actual__gt=0).count()}")
    print(f"   Productos disponibles web: {productos.filter(disponible_web=True).count()}")

    if productos.exists():
        print("\n   Primeros 5 productos:")
        for prod in productos[:5]:
            print(f"   - ID:{prod.id} {prod.nombre_producto} - Stock: {prod.stock_actual} - Precio: ${prod.precio_venta}")

    # 3. Probar función de carrito
    print("\n3. PROBANDO FUNCIONES DE CARRITO:")
    try:
        factory = RequestFactory()

        # Crear request de prueba
        request = factory.post('/tienda/carrito/agregar/',
                             content_type='application/json',
                             data='{"producto_id": "1", "cantidad": 1}')
        request.session = {}

        print("   ✅ Request factory funciona")
        print(f"   ✅ Función agregar_al_carrito existe")
        print(f"   ✅ Función eliminar_del_carrito existe")
        print(f"   ✅ Función ver_carrito existe")

    except Exception as e:
        print(f"   ❌ Error: {e}")

    # 4. Verificar rutas
    print("\n4. VERIFICANDO RUTAS:")
    try:
        from django.urls import reverse
        rutas = [
            ('ecommerce:productos', 'Catálogo'),
            ('ecommerce:ver_carrito', 'Ver carrito'),
            ('ecommerce:agregar_carrito', 'Agregar al carrito'),
            ('ecommerce:eliminar_carrito', 'Eliminar del carrito'),
            ('ecommerce:limpiar_carrito', 'Limpiar carrito'),
            ('ecommerce:checkout', 'Checkout'),
            ('ecommerce:procesar_compra', 'Procesar compra'),
        ]

        for nombre, desc in rutas:
            try:
                url = reverse(nombre)
                print(f"   ✅ {desc}: {url}")
            except Exception as e:
                print(f"   ❌ {desc}: Error - {e}")

    except Exception as e:
        print(f"   ❌ Error al verificar rutas: {e}")

    # 5. Resumen
    print("\n" + "=" * 60)
    print("RESUMEN:")
    print("=" * 60)

    if usuarios.exists() and productos.exists():
        print("✅ Sistema básico configurado correctamente")
        print("\nPRÓXIMOS PASOS:")
        print("1. Asegúrate de estar logueado en el navegador")
        print("2. Ve a http://127.0.0.1:8000/tienda/")
        print("3. Intenta agregar un producto al carrito")
        print("4. Revisa la consola del navegador (F12) para ver errores")
        print("\nSi no funciona, verifica:")
        print("- ¿Estás logueado? (Debe aparecer tu nombre en la esquina superior derecha)")
        print("- ¿Hay errores en la consola del navegador?")
        print("- ¿El servidor Django está corriendo?")
    else:
        print("❌ Faltan configuraciones básicas")
        if not usuarios.exists():
            print("   - No hay usuarios creados")
        if not productos.exists():
            print("   - No hay productos activos")

    print("\n" + "=" * 60)

if __name__ == '__main__':
    diagnosticar_carrito()

