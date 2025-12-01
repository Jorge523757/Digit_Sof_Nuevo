#!/usr/bin/env python
"""
Prueba final del e-commerce con navegador
"""
import requests
import time

def test_final_ecommerce():
    """Prueba final del e-commerce"""
    print("🔥 PRUEBA FINAL DEL E-COMMERCE")
    print("="*50)
    
    base_url = "http://127.0.0.1:8000"
    urls_test = [
        "/",  # Home
        "/tienda/",  # E-commerce principal
        "/tienda/carrito/",  # Carrito
    ]
    
    for url in urls_test:
        try:
            print(f"📡 Probando: {base_url}{url}")
            response = requests.get(f"{base_url}{url}", timeout=10)
            
            if response.status_code == 200:
                print(f"✅ {url} - FUNCIONA PERFECTAMENTE (200)")
                print(f"   Tamaño de respuesta: {len(response.content)} bytes")
            else:
                print(f"❌ {url} - Error {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {url} - No se puede conectar (servidor no responde)")
        except Exception as e:
            print(f"❌ {url} - Error: {e}")
    
    print("\n🌐 PARA ACCEDER:")
    print(f"   1. Abre tu navegador web")
    print(f"   2. Ve a: {base_url}/tienda/")
    print(f"   3. ¡Disfruta tu e-commerce!")

if __name__ == '__main__':
    test_final_ecommerce()
