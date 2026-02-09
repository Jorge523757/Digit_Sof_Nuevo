"""
Script para configurar Google OAuth en la base de datos
NOTA: Las credenciales deben configurarse en el panel de admin de Django
o mediante variables de entorno.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

print("\n" + "=" * 80)
print("🔧 CONFIGURACIÓN DE GOOGLE OAUTH")
print("=" * 80)

# Obtener credenciales de variables de entorno o usar placeholders
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', 'TU_CLIENT_ID_AQUI')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', 'TU_CLIENT_SECRET_AQUI')

if GOOGLE_CLIENT_ID == 'TU_CLIENT_ID_AQUI' or GOOGLE_CLIENT_SECRET == 'TU_CLIENT_SECRET_AQUI':
    print("\n⚠️  ADVERTENCIA: Credenciales no configuradas")
    print("\nOpciones para configurar:")
    print("\n1. Variables de entorno:")
    print("   set GOOGLE_CLIENT_ID=tu_client_id")
    print("   set GOOGLE_CLIENT_SECRET=tu_client_secret")
    print("   python configurar_google_oauth.py")
    print("\n2. Panel de administración de Django:")
    print("   - Ve a: http://127.0.0.1:8000/admin/")
    print("   - Social applications → Add")
    print("   - Configura las credenciales allí")
    print("\n3. Edita este archivo y reemplaza los placeholders")
    print("\n" + "=" * 80 + "\n")
    exit(1)

# Eliminar configuraciones duplicadas
print("\n[1/3] Limpiando configuraciones duplicadas...")
google_apps = SocialApp.objects.filter(provider='google')
if google_apps.count() > 1:
    google_apps.delete()
    print(f"   ✓ {google_apps.count()} configuración(es) eliminada(s)")
elif google_apps.count() == 1:
    print("   ✓ Una configuración existente encontrada")
else:
    print("   ℹ️  No hay configuraciones previas")

# Verificar site
print("\n[2/3] Verificando configuración de Site...")
site, created = Site.objects.get_or_create(
    id=1,
    defaults={
        'domain': 'localhost:8000',
        'name': 'DIGIT SOFT'
    }
)
if not created:
    site.domain = 'localhost:8000'
    site.name = 'DIGIT SOFT'
    site.save()
print(f"   ✓ Site configurado: {site.domain}")

# Crear o actualizar configuración
print("\n[3/3] Configurando Google OAuth...")
google_apps = SocialApp.objects.filter(provider='google')

if google_apps.count() == 0:
    # Crear nueva configuración
    app = SocialApp.objects.create(
        provider='google',
        name='Google OAuth DIGIT SOFT',
        client_id=GOOGLE_CLIENT_ID,
        secret=GOOGLE_CLIENT_SECRET
    )
    app.sites.add(site)
    print(f"   ✓ Nueva configuración creada (ID: {app.id})")
else:
    # Actualizar configuración existente
    app = google_apps.first()
    app.client_id = GOOGLE_CLIENT_ID
    app.secret = GOOGLE_CLIENT_SECRET
    app.name = 'Google OAuth DIGIT SOFT'
    app.save()
    app.sites.clear()
    app.sites.add(site)
    print(f"   ✓ Configuración actualizada (ID: {app.id})")

print("\n" + "=" * 80)
print("✅ CONFIGURACIÓN COMPLETADA")
print("=" * 80)
print(f"\n📋 Resumen:")
print(f"   - Provider: google")
print(f"   - Name: {app.name}")
print(f"   - Client ID: {app.client_id[:20]}...")
print(f"   - Sites: {[s.domain for s in app.sites.all()]}")
print("\n" + "=" * 80 + "\n")

