"""
Script de Verificación Completa del Sistema
Verifica que todas las dependencias y configuraciones estén correctas
"""
import sys
import os

print("\n" + "="*80)
print("🔍 VERIFICACIÓN COMPLETA DEL SISTEMA - DIGIT SOFT")
print("="*80)

# ============================================================================
# 1. VERIFICAR VERSIÓN DE PYTHON
# ============================================================================
print("\n[1] Verificando versión de Python...")
python_version = sys.version_info
if python_version.major == 3 and python_version.minor >= 8:
    print(f"   ✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
else:
    print(f"   ⚠️  Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    print("   Recomendado: Python 3.8+")

# ============================================================================
# 2. VERIFICAR PAQUETES INSTALADOS
# ============================================================================
print("\n[2] Verificando paquetes instalados...")

paquetes_requeridos = {
    'django': 'Django',
    'allauth': 'django-allauth',
    'django_recaptcha': 'django-recaptcha'
}

paquetes_ok = True
for modulo, nombre in paquetes_requeridos.items():
    try:
        __import__(modulo)
        if modulo == 'django':
            import django
            print(f"   ✅ {nombre} ({django.get_version()})")
        elif modulo == 'allauth':
            import allauth
            print(f"   ✅ {nombre} ({allauth.__version__})")
        else:
            print(f"   ✅ {nombre}")
    except ImportError:
        print(f"   ❌ {nombre} NO instalado")
        print(f"      Ejecuta: pip install {nombre}")
        paquetes_ok = False

# ============================================================================
# 3. CONFIGURAR DJANGO
# ============================================================================
if paquetes_ok:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        import django
        django.setup()
        print("\n[3] Django configurado correctamente ✅")
    except Exception as e:
        print(f"\n[3] Error al configurar Django: {e}")
        sys.exit(1)
else:
    print("\n⚠️  Instala los paquetes faltantes antes de continuar")
    sys.exit(1)

# ============================================================================
# 4. VERIFICAR CONFIGURACIÓN DE SETTINGS
# ============================================================================
print("\n[4] Verificando configuración en settings.py...")

from django.conf import settings

# Verificar reCAPTCHA
if hasattr(settings, 'RECAPTCHA_PUBLIC_KEY'):
    print("   ✅ RECAPTCHA_PUBLIC_KEY configurado")
else:
    print("   ❌ RECAPTCHA_PUBLIC_KEY NO configurado")

if hasattr(settings, 'RECAPTCHA_PRIVATE_KEY'):
    print("   ✅ RECAPTCHA_PRIVATE_KEY configurado")
else:
    print("   ❌ RECAPTCHA_PRIVATE_KEY NO configurado")

# Verificar apps instaladas
apps_requeridas = ['django_recaptcha', 'allauth', 'usuarios']
for app in apps_requeridas:
    if app in settings.INSTALLED_APPS:
        print(f"   ✅ '{app}' en INSTALLED_APPS")
    else:
        print(f"   ❌ '{app}' NO está en INSTALLED_APPS")

# ============================================================================
# 5. VERIFICAR BASE DE DATOS
# ============================================================================
print("\n[5] Verificando base de datos...")

try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    print("   ✅ Conexión a base de datos exitosa")

    # Verificar tablas importantes
    from django.contrib.auth.models import User
    user_count = User.objects.count()
    print(f"   ✅ Usuarios en la base de datos: {user_count}")

except Exception as e:
    print(f"   ⚠️  Error en base de datos: {e}")
    print("   Ejecuta: python manage.py migrate")

# ============================================================================
# 6. VERIFICAR GOOGLE OAUTH
# ============================================================================
print("\n[6] Verificando Google OAuth...")

try:
    from allauth.socialaccount.models import SocialApp
    google_apps = SocialApp.objects.filter(provider='google')
    count = google_apps.count()

    if count == 0:
        print("   ⚠️  No hay configuración de Google OAuth")
        print("   Ejecuta: python LIMPIAR_GOOGLE_OAUTH.py")
    elif count == 1:
        app = google_apps.first()
        print("   ✅ Exactamente 1 configuración de Google OAuth")
        print(f"      Client ID: {app.client_id[:20]}...")
    else:
        print(f"   ❌ ERROR: {count} configuraciones (debe ser 1)")
        print("   Ejecuta: python LIMPIAR_GOOGLE_OAUTH.py")

except Exception as e:
    print(f"   ⚠️  Error: {e}")

# ============================================================================
# 7. VERIFICAR ARCHIVOS IMPORTANTES
# ============================================================================
print("\n[7] Verificando archivos importantes...")

archivos = {
    'manage.py': 'Script principal de Django',
    'config/settings.py': 'Configuración',
    'usuarios/views.py': 'Vistas de usuarios',
    'usuarios/forms.py': 'Formularios con reCAPTCHA',
    'usuarios/views_recuperacion.py': 'Sistema de recuperación',
    'templates/usuarios/login.html': 'Template de login',
    'templates/usuarios/recuperar_paso1.html': 'Template recuperación paso 1',
    'templates/usuarios/recuperar_paso2.html': 'Template recuperación paso 2',
    'templates/usuarios/recuperar_paso3.html': 'Template recuperación paso 3',
}

archivos_ok = True
for archivo, descripcion in archivos.items():
    if os.path.exists(archivo):
        print(f"   ✅ {archivo}")
    else:
        print(f"   ❌ {archivo} NO encontrado")
        archivos_ok = False

# ============================================================================
# 8. VERIFICAR SCRIPTS DE CONFIGURACIÓN
# ============================================================================
print("\n[8] Verificando scripts de configuración...")

scripts = [
    'CONFIGURAR_SISTEMA_COMPLETO.bat',
    'LIMPIAR_GOOGLE_OAUTH.py',
    'verificacion_final.py',
    'RESUMEN_FINAL.bat'
]

for script in scripts:
    if os.path.exists(script):
        print(f"   ✅ {script}")
    else:
        print(f"   ⚠️  {script} NO encontrado (opcional)")

# ============================================================================
# RESUMEN FINAL
# ============================================================================
print("\n" + "="*80)
print("📊 RESUMEN")
print("="*80)

all_ok = True

if python_version.major == 3 and python_version.minor >= 8:
    print("✅ Python")
else:
    print("⚠️  Python (versión antigua)")
    all_ok = False

if paquetes_ok:
    print("✅ Paquetes")
else:
    print("❌ Paquetes (faltantes)")
    all_ok = False

if archivos_ok:
    print("✅ Archivos")
else:
    print("⚠️  Archivos (algunos faltantes)")
    all_ok = False

print("\n" + "="*80)

if all_ok:
    print("🎉 ¡TODO ESTÁ PERFECTO!")
    print("="*80)
    print("\n✅ El sistema está listo para usar")
    print("\n🚀 PRÓXIMOS PASOS:")
    print("   1. Ejecuta: python manage.py runserver")
    print("   2. Visita: http://127.0.0.1:8000/usuarios/login/")
    print("   3. Prueba las funcionalidades")
else:
    print("⚠️  HAY PROBLEMAS QUE RESOLVER")
    print("="*80)
    print("\n📝 ACCIONES RECOMENDADAS:")
    if not paquetes_ok:
        print("   • Instalar paquetes faltantes")
    if not archivos_ok:
        print("   • Verificar que todos los archivos existan")
    print("   • Ejecutar: CONFIGURAR_SISTEMA_COMPLETO.bat")

print("\n" + "="*80)
print("📚 DOCUMENTACIÓN:")
print("   • README_RAPIDO.md - Inicio rápido")
print("   • INSTRUCCIONES_SISTEMA_COMPLETO.md - Guía completa")
print("   • IMPLEMENTACION_COMPLETA.md - Resumen técnico")
print("="*80 + "\n")

