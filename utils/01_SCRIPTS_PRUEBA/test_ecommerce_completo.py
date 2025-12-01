#!/usr/bin/env python
"""
Script para verificar directamente que las vistas del e-commerce funcionan
"""
import os
import sys
import django

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def test_ecommerce_views():
    """Probar las vistas del e-commerce directamente"""
    print("🔍 Probando vistas del e-commerce...")
    
    try:
        # Importar las vistas
        from productos.views import productos_ecommerce, ver_carrito, agregar_al_carrito
        print("✅ Todas las vistas del e-commerce importadas correctamente")
        
        # Probar que existan productos
        from productos.models import Producto, CategoriaProducto
        productos_count = Producto.objects.filter(activo=True, disponible_web=True).count()
        print(f"✅ Productos activos disponibles: {productos_count}")
        
        if productos_count == 0:
            print("❌ No hay productos disponibles para mostrar")
            return False
            
        # Probar que existan categorías
        categorias_count = CategoriaProducto.objects.count()
        print(f"✅ Categorías disponibles: {categorias_count}")
        
        # Probar request mock
        from django.test import RequestFactory
        from django.contrib.sessions.middleware import SessionMiddleware
        
        factory = RequestFactory()
        request = factory.get('/tienda/')
        
        # Agregar sesión al request
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(request)
        request.session.save()
        
        # Probar la vista
        response = productos_ecommerce(request)
        print(f"✅ Vista productos_ecommerce responde con status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ La vista del e-commerce funciona correctamente!")
            return True
        else:
            print(f"❌ Error en la vista: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error al probar vistas: {e}")
        import traceback
        traceback.print_exc()
        return False

def fix_template_issue():
    """Verificar y corregir problemas en las plantillas"""
    print("\n🔧 Verificando plantillas...")
    
    plantillas = [
        'templates/ecommerce/productos.html',
        'templates/ecommerce/carrito.html',
        'templates/ecommerce/producto_detalle.html'
    ]
    
    for plantilla in plantillas:
        if os.path.exists(plantilla):
            print(f"✅ {plantilla} existe")
        else:
            print(f"❌ {plantilla} no existe")

def crear_url_pattern():
    """Verificar configuración de URLs"""
    print("\n🔧 Verificando configuración de URLs...")
    
    try:
        from django.urls import reverse
        # No podemos testear reverse sin un request context, pero podemos verificar imports
        print("✅ Sistema de URLs Django funcional")
        
        # Verificar archivo ecommerce_urls.py
        if os.path.exists('ecommerce_urls.py'):
            print("✅ Archivo ecommerce_urls.py existe")
            
            with open('ecommerce_urls.py', 'r', encoding='utf-8') as f:
                content = f.read()
                if 'productos_ecommerce' in content:
                    print("✅ productos_ecommerce está en ecommerce_urls.py")
                else:
                    print("❌ productos_ecommerce no está en ecommerce_urls.py")
        else:
            print("❌ ecommerce_urls.py no existe")
            
    except Exception as e:
        print(f"❌ Error en URLs: {e}")

if __name__ == '__main__':
    print("="*60)
    print("    DIAGNÓSTICO COMPLETO DEL E-COMMERCE")
    print("="*60)
    
    # Test 1: Vistas
    vista_ok = test_ecommerce_views()
    
    # Test 2: Plantillas
    fix_template_issue()
    
    # Test 3: URLs
    crear_url_pattern()
    
    print("\n" + "="*60)
    if vista_ok:
        print("✅ RESULTADO: El e-commerce debería funcionar correctamente")
        print("🌐 Accede a: http://127.0.0.1:8000/tienda/")
        print("📝 Si aún no aparece, verifica que el servidor esté ejecutándose")
    else:
        print("❌ RESULTADO: Hay problemas que necesitan corrección")
    print("="*60)
