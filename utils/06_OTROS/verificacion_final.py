"""
Verificación final antes de iniciar el servidor
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.conf import settings

print("\n" + "="*80)
print("✅ VERIFICACIÓN FINAL - TODO LISTO PARA FUNCIONAR")
print("="*80)

# Verificar configuración en settings
print("\n[1] Verificando settings.py...")
providers = settings.SOCIALACCOUNT_PROVIDERS
if 'google' in providers:
    google_config = providers['google']
    if 'APP' in google_config:
        print("   ❌ ERROR: 'APP' está en settings.py (causa MultipleObjectsReturned)")
        print("   Elimina la sección 'APP' de SOCIALACCOUNT_PROVIDERS")
    else:
        print("   ✅ Configuración correcta en settings.py")
        print(f"   - SCOPE: {google_config.get('SCOPE')}")
else:
    print("   ⚠️  No hay configuración de Google en settings.py")

# Verificar base de datos
print("\n[2] Verificando base de datos...")
google_apps = SocialApp.objects.filter(provider='google')
if google_apps.count() == 1:
    app = google_apps.first()
    print(f"   ✅ Una sola configuración de Google OAuth")
    print(f"   - ID: {app.id}")
    print(f"   - Client ID: {app.client_id}")
    print(f"   - Sites: {[s.domain for s in app.sites.all()]}")
elif google_apps.count() > 1:
    print(f"   ❌ ERROR: {google_apps.count()} configuraciones (debe ser 1)")
    print("   Ejecuta: python ARREGLAR_GOOGLE_DEFINITIVO.py")
else:
    print("   ❌ ERROR: No hay configuración de Google OAuth")
    print("   Ejecuta: python ARREGLAR_GOOGLE_DEFINITIVO.py")

# Verificar Site
print("\n[3] Verificando Site...")
try:
    site = Site.objects.get(id=1)
    print(f"   ✅ Site configurado: {site.domain}")
except:
    print("   ❌ ERROR: Site no encontrado")

print("\n" + "="*80)
print("📋 RESUMEN")
print("="*80)

all_ok = True
if 'google' in providers and 'APP' not in providers['google'] and google_apps.count() == 1:
    print("\n✅ TODO ESTÁ PERFECTO - LISTO PARA FUNCIONAR")
    print("\n🚀 Pasos siguientes:")
    print("   1. Asegúrate que el servidor esté corriendo")
    print("   2. Ve a: http://127.0.0.1:8000/usuarios/login/")
    print("   3. Haz clic en 'Continuar con Google'")
    print("   4. Usa: davidcristancho160@gmail.com")
else:
    print("\n⚠️  HAY PROBLEMAS - REVISA LOS MENSAJES ARRIBA")
    all_ok = False

print("\n" + "="*80)
print("⚠️  IMPORTANTE: URIs en Google Cloud Console")
print("="*80)
print("\nAsegúrate de tener estas URIs autorizadas:")
print("   • http://127.0.0.1:8000/accounts/google/login/callback/")
print("   • http://localhost:8000/accounts/google/login/callback/")
print("\nEn: https://console.cloud.google.com/apis/credentials")
print("="*80 + "\n")

