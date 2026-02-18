"""
Script para matar TODOS los procesos de Python/Django y verificar
"""

import subprocess
import sys

print("=" * 80)
print("🔪 MATANDO TODOS LOS PROCESOS DE PYTHON/DJANGO")
print("=" * 80)

# Intentar matar todos los procesos de Python
print("\n⚠️ Intentando detener todos los procesos de Python...")

try:
    # En Windows, matar procesos de python.exe
    result = subprocess.run(
        ['taskkill', '/F', '/IM', 'python.exe'],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✅ Procesos de Python detenidos")
        print(result.stdout)
    else:
        print("⚠️ No se encontraron procesos de Python corriendo")
        print(result.stderr)
        
except Exception as e:
    print(f"❌ Error al intentar matar procesos: {e}")

print("\n" + "=" * 80)
print("📋 SIGUIENTE PASO:")
print("=" * 80)
print("\n1. Ejecuta la limpieza nuclear:")
print("   python limpieza_nuclear_google.py")
print("\n2. Inicia el servidor:")
print("   python manage.py runserver")
print("\n3. Prueba en modo incógnito (Ctrl+Shift+N)")
print("\n" + "=" * 80)

