"""
Script de diagnóstico del carrito
"""
import json
from django.test import Client
from django.contrib.auth.models import User

# Crear cliente de prueba
client = Client()

# Intentar agregar producto
print("=" * 60)
print("DIAGNÓSTICO DEL CARRITO")
print("=" * 60)

# 1. Verificar que el endpoint responde
response = client.post('/tienda/carrito/agregar/', 
    data=json.dumps({'producto_id': '1', 'cantidad': 1}),
    content_type='application/json'
)

print(f"\n1. Test Agregar al carrito:")
print(f"   Status: {response.status_code}")
print(f"   Respuesta: {response.content.decode()[:200]}")

# 2. Verificar actualizar
response = client.post('/tienda/carrito/actualizar/', 
    data=json.dumps({'producto_id': '1', 'cantidad': 2}),
    content_type='application/json'
)

print(f"\n2. Test Actualizar cantidad:")
print(f"   Status: {response.status_code}")
print(f"   Respuesta: {response.content.decode()[:200]}")

# 3. Verificar eliminar
response = client.post('/tienda/carrito/eliminar/', 
    data=json.dumps({'producto_id': '1'}),
    content_type='application/json'
)

print(f"\n3. Test Eliminar producto:")
print(f"   Status: {response.status_code}")
print(f"   Respuesta: {response.content.decode()[:200]}")

# 4. Verificar limpiar
response = client.post('/tienda/carrito/limpiar/', 
    data=json.dumps({}),
    content_type='application/json'
)

print(f"\n4. Test Limpiar carrito:")
print(f"   Status: {response.status_code}")
print(f"   Respuesta: {response.content.decode()[:200]}")

print("\n" + "=" * 60)
print("DIAGNÓSTICO COMPLETADO")
print("=" * 60)

