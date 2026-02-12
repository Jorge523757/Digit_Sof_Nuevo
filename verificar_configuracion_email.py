"""
VERIFICADOR RÁPIDO - Estado del Sistema de Email
"""

import os
from pathlib import Path

print("=" * 80)
print("  🔍 VERIFICANDO CONFIGURACIÓN DE EMAIL")
print("=" * 80)
print()

# 1. Verificar python-dotenv
print("1. Verificando python-dotenv...")
try:
    import dotenv
    print("   ✅ python-dotenv instalado")
except ImportError:
    print("   ❌ python-dotenv NO instalado")
    print("      Solución: pip install python-dotenv")

# 2. Verificar archivo .env
print()
print("2. Verificando archivo .env...")
env_path = Path('.env')
if env_path.exists():
    print("   ✅ Archivo .env existe")

    # Leer configuración
    email = None
    password = None

    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('EMAIL_HOST_USER='):
                email = line.split('=', 1)[1].strip()
            elif line.startswith('EMAIL_HOST_PASSWORD='):
                password = line.split('=', 1)[1].strip()

    print(f"   📧 Email configurado: {email}")

    if password and password != 'AQUI_TU_CONTRASEÑA_DE_APLICACION':
        print(f"   🔑 Contraseña configurada: {'*' * len(password)}")
    else:
        print("   ❌ Contraseña NO configurada")
        print("      Necesitas ejecutar: CONFIGURAR_EMAIL_AHORA.bat")
else:
    print("   ❌ Archivo .env NO existe")

# 3. Verificar settings.py
print()
print("3. Verificando settings.py...")
settings_path = Path('config/settings.py')
if settings_path.exists():
    with open(settings_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'from dotenv import load_dotenv' in content:
        print("   ✅ Importación de dotenv presente")
    else:
        print("   ❌ Falta importación de dotenv")

    if 'load_dotenv' in content:
        print("   ✅ Carga de .env configurada")
    else:
        print("   ❌ No se está cargando el archivo .env")
else:
    print("   ❌ Archivo settings.py NO encontrado")

# 4. Resumen
print()
print("=" * 80)
print("  📊 RESUMEN")
print("=" * 80)
print()

if email and password and password != 'AQUI_TU_CONTRASEÑA_DE_APLICACION':
    print("✅ CONFIGURACIÓN COMPLETA")
    print()
    print("Próximos pasos:")
    print("1. REINICIA el servidor Django (Ctrl+C y python manage.py runserver)")
    print("2. Prueba la función 'Olvidé mi contraseña'")
    print("3. El código debe llegar al email en 5-30 segundos")
else:
    print("⚠️  CONFIGURACIÓN INCOMPLETA")
    print()
    print("Próximos pasos:")
    print("1. Ejecuta: CONFIGURAR_EMAIL_AHORA.bat")
    print("2. Sigue las instrucciones en pantalla")
    print("3. Reinicia Django después de configurar")

print()
print("=" * 80)
print()

input("Presiona Enter para salir...")

