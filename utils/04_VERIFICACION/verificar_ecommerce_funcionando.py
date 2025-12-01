#!/usr/bin/env python
"""
Verificar que el E-commerce funciona correctamente
"""
import os
import sys
import requests
from urllib.parse import urljoin

# Configurar el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

def verificar_ecommerce():
    """Verificar que el e-commerce funciona"""
    print("🔍 Verificando E-commerce...")
    
    base_url = "http://127.0.0.1:8000"
    
    urls_a_probar = [
        "/tienda/",
        "/tienda/carrito/",
    ]
    
    for url in urls_a_probar:
        try:
            full_url = urljoin(base_url, url)
            print(f"📡 Probando: {full_url}")
            
            response = requests.get(full_url, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {url} - OK (200)")
            else:
                print(f"❌ {url} - Error {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {url} - Servidor no responde")
        except Exception as e:
            print(f"❌ {url} - Error: {e}")
    
    # Verificar datos
    from productos.models import Producto, CategoriaProducto
    
    productos_count = Producto.objects.filter(activo=True, disponible_web=True).count()
    categorias_count = CategoriaProducto.objects.count()
    
    print(f"\n📊 Datos disponibles:")
    print(f"   Productos activos: {productos_count}")
    print(f"   Categorías: {categorias_count}")
    
    if productos_count > 0:
        print("\n✅ El e-commerce debería funcionar correctamente!")
        print("🌐 Accede a: http://127.0.0.1:8000/tienda/")
    else:
        print("\n⚠️  No hay productos disponibles. Ejecuta el script de datos de prueba.")

if __name__ == '__main__':
    verificar_ecommerce()
