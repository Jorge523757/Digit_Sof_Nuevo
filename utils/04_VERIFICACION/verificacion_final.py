#!/usr/bin/env python
"""
Verificación final y solución de problemas del E-commerce
"""
import os
import sys
import django

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def verificacion_completa():
    """Verificación completa del sistema"""
    print("🔍 VERIFICACIÓN COMPLETA DEL E-COMMERCE")
    print("="*60)

    errores = []

    # 1. Verificar modelos y datos
    print("\n1️⃣ VERIFICANDO DATOS...")
    try:
        from productos.models import Producto, CategoriaProducto
        productos = Producto.objects.filter(activo=True, disponible_web=True)
        categorias = CategoriaProducto.objects.all()

        print(f"✅ Productos activos: {productos.count()}")
        print(f"✅ Categorías: {categorias.count()}")

        if productos.count() == 0:
            errores.append("No hay productos disponibles")

    except Exception as e:
        errores.append(f"Error en modelos: {e}")

    # 2. Verificar vistas
    print("\n2️⃣ VERIFICANDO VISTAS...")
    try:
        from productos.views import productos_ecommerce, ver_carrito, agregar_al_carrito
        from django.test import RequestFactory
        from django.contrib.sessions.middleware import SessionMiddleware

        factory = RequestFactory()
        request = factory.get('/tienda/')
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(request)
        request.session.save()

        response = productos_ecommerce(request)

        if response.status_code == 200:
            print("✅ Vista productos_ecommerce: FUNCIONA")
        else:
            errores.append(f"Vista productos_ecommerce error: {response.status_code}")

        # Test carrito
        response_carrito = ver_carrito(request)
        if response_carrito.status_code == 200:
            print("✅ Vista ver_carrito: FUNCIONA")
        else:
            errores.append(f"Vista ver_carrito error: {response_carrito.status_code}")

    except Exception as e:
        errores.append(f"Error en vistas: {e}")

    # 3. Verificar URLs
    print("\n3️⃣ VERIFICANDO URLs...")
    try:
        import ecommerce_urls
        print("✅ Archivo ecommerce_urls.py existe")

        # Verificar que no hay referencias a 'main:'
        with open('ecommerce_urls.py', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'main:' in content:
                errores.append("URLs contienen referencias a 'main:' namespace")
            else:
                print("✅ URLs sin referencias problemáticas")

    except Exception as e:
        errores.append(f"Error en URLs: {e}")

    # 4. Verificar plantillas
    print("\n4️⃣ VERIFICANDO PLANTILLAS...")
    plantillas = [
        'templates/ecommerce/productos.html',
        'templates/ecommerce/carrito.html',
        'templates/ecommerce/producto_detalle.html'
    ]

    for plantilla in plantillas:
        if os.path.exists(plantilla):
            print(f"✅ {plantilla}")

            # Verificar que no hay 'main:' en las plantillas
            with open(plantilla, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if "{% url 'main:" in content:
                    errores.append(f"{plantilla} contiene URLs 'main:' problemáticas")
        else:
            errores.append(f"{plantilla} no existe")

    # 5. Resultados
    print("\n" + "="*60)
    if errores:
        print("❌ PROBLEMAS ENCONTRADOS:")
        for error in errores:
            print(f"   • {error}")
        print("\n🔧 RECOMENDACIONES:")
        print("   1. Revisa los errores listados arriba")
        print("   2. Ejecuta: python manage.py check")
        print("   3. Reinicia el servidor: python manage.py runserver")
    else:
        print("✅ ¡TODO PERFECTO! El e-commerce está funcionando correctamente")
        print("\n🌐 ACCESO:")
        print("   • Abre tu navegador")
        print("   • Ve a: http://127.0.0.1:8000/tienda/")
        print("   • ¡Disfruta tu tienda online!")

    print("="*60)

if __name__ == '__main__':
    verificacion_completa()
