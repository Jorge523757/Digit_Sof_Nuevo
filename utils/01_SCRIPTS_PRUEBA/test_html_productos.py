#!/usr/bin/env python3
"""
Test para verificar el HTML generado por la vista
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from productos.models import Producto


def test_html_generado():
    """Test para verificar el HTML generado"""
    print("🌐 Probando generación de HTML...")
    
    # Verificar productos
    productos_count = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    ).count()
    
    print(f"📦 Productos disponibles en DB: {productos_count}")
    
    if productos_count == 0:
        print("⚠️ No hay productos. Creando productos de prueba...")
        os.system('python crear_productos_ecommerce.py')
    
    # Generar HTML
    client = Client()
    response = client.get('/')
    
    if response.status_code == 200:
        print("✅ Página se genera correctamente")
        
        content = response.content.decode('utf-8')
        
        # Buscar elementos clave
        checks = [
            ('class="product-card"', 'Tarjetas de producto'),
            ('data-producto-id=', 'IDs de productos'),
            ('btn-add-cart', 'Botones de carrito'),
            ('product-name', 'Nombres de productos'),
            ('<!-- Grid de productos reales', 'Comentario de productos reales'),
        ]
        
        print("\n🔍 Verificando elementos en el HTML:")
        for check, desc in checks:
            count = content.count(check)
            if count > 0:
                print(f"   ✅ {desc}: {count} encontrado(s)")
            else:
                print(f"   ❌ {desc}: no encontrado")
        
        # Buscar productos específicos por nombre
        productos = Producto.objects.filter(
            activo=True,
            disponible_web=True,
            stock_actual__gt=0
        )[:5]
        
        print(f"\n📋 Verificando productos específicos en HTML:")
        for producto in productos:
            if producto.nombre_producto in content:
                print(f"   ✅ {producto.nombre_producto}: encontrado")
            else:
                print(f"   ❌ {producto.nombre_producto}: NO encontrado")
        
        # Verificar que no aparezcan productos hardcodeados
        productos_estaticos = [
            "Laptop HP EliteBook",
            "Computadora Dell OptiPlex", 
            "Teclado Mecánico RGB"
        ]
        
        print(f"\n🚫 Verificando que NO aparezcan productos estáticos:")
        for producto_estatico in productos_estaticos:
            if producto_estatico in content:
                print(f"   ⚠️ {producto_estatico}: ENCONTRADO (debería eliminarse)")
            else:
                print(f"   ✅ {producto_estatico}: no encontrado (correcto)")
        
        # Guardar un fragmento para inspección
        start = content.find('<section id="productos"')
        if start != -1:
            end = content.find('</section>', start) + 10
            productos_section = content[start:end]
            
            with open('productos_section_debug.html', 'w', encoding='utf-8') as f:
                f.write(productos_section)
            print(f"\n💾 Sección de productos guardada en: productos_section_debug.html")
            print(f"   Tamaño de la sección: {len(productos_section)} caracteres")
        
        return True
        
    else:
        print(f"❌ Error HTTP: {response.status_code}")
        return False


def main():
    print("🧪 TEST DE GENERACIÓN DE HTML")
    print("=" * 40)
    
    if test_html_generado():
        print("\n🎉 Test completado")
        print("📋 Revisa el archivo productos_section_debug.html para inspeccionar el HTML generado")
        print("🌐 Abre http://127.0.0.1:8000/ y ve a la consola del navegador para más información")
    else:
        print("\n❌ Test falló")


if __name__ == "__main__":
    main()
