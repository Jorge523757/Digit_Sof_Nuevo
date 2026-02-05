"""
Script para probar el filtro de pesos colombianos
"""
import os
import sys
import django

# Configurar Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from utils.templatetags.currency_filters import peso_colombiano, peso_colombiano_decimal

print("="*60)
print("PRUEBA DE FILTROS DE MONEDA COLOMBIANA")
print("="*60)

# Casos de prueba
test_cases = [
    50000,
    50000.50,
    1234567,
    1234567.89,
    999.99,
    0,
    None,
    "50000",
    "50000.50",
]

print("\n🔹 Pruebas con peso_colombiano (sin decimales):")
print("-" * 60)
for value in test_cases:
    result = peso_colombiano(value)
    print(f"Valor: {str(value):20} → Resultado: {result}")

print("\n🔹 Pruebas con peso_colombiano_decimal (con decimales):")
print("-" * 60)
for value in test_cases:
    result = peso_colombiano_decimal(value, 2)
    print(f"Valor: {str(value):20} → Resultado: {result}")

print("\n" + "="*60)
print("✅ Pruebas completadas")
print("="*60)
print("\nEjemplos de uso en templates:")
print("  {{ valor|peso_colombiano }}           → Sin decimales")
print("  {{ valor|peso_colombiano_decimal:2 }} → Con 2 decimales")
print("="*60)

