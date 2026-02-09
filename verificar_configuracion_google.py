"""
Script para verificar y mostrar la configuración actual de Google OAuth
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

print("=" * 80)
print("🔍 CONFIGURACIÓN ACTUAL DE GOOGLE OAUTH")
print("=" * 80)

# Verificar Site
site = Site.objects.get_current()
print(f"\n📍 Site configurado:")
print(f"   - ID: {site.id}")
print(f"   - Domain: {site.domain}")
print(f"   - Name: {site.name}")

# Verificar Social App
google_apps = SocialApp.objects.filter(provider='google')
print(f"\n📱 Social Apps de Google: {google_apps.count()}")

for app in google_apps:
    print(f"\n   App ID: {app.id}")
    print(f"   - Name: {app.name}")
    print(f"   - Provider: {app.provider}")
    print(f"   - Client ID: {app.client_id}")
    print(f"   - Secret: {app.secret[:20]}...")
    print(f"   - Sites: {[s.domain for s in app.sites.all()]}")

# Mostrar las URIs que debes configurar en Google Cloud Console
print("\n" + "=" * 80)
print("🔧 URIs DE REDIRECCIÓN QUE DEBES CONFIGURAR EN GOOGLE CLOUD")
print("=" * 80)
print("\nVe a: https://console.cloud.google.com/")
print("Luego: APIs y servicios > Credenciales > Tu OAuth 2.0 Client ID")
print("\nAgrega estas URIs de redirección autorizadas:")
print("\n   ✓ http://127.0.0.1:8000/accounts/google/login/callback/")
print("   ✓ http://localhost:8000/accounts/google/login/callback/")
print("   ✓ http://127.0.0.1:8000/accounts/google/login/callback")
print("   ✓ http://localhost:8000/accounts/google/login/callback")

print("\n" + "=" * 80)
print("⚠️ IMPORTANTE: Después de agregar las URIs en Google Cloud:")
print("=" * 80)
print("\n1. Guarda los cambios en Google Cloud Console")
print("2. Espera 1-2 minutos (puede tardar en propagarse)")
print("3. Reinicia el servidor Django")
print("4. Intenta nuevamente en modo incógnito")

print("\n" + "=" * 80)

