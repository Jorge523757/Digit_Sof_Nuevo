"""
Script para diagnosticar el problema de Google OAuth
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

print("🔍 DIAGNÓSTICO DE GOOGLE OAUTH\n")

# Verificar Sites
print("📍 SITES:")
sites = Site.objects.all()
print(f"   Total: {sites.count()}")
for site in sites:
    print(f"   - ID: {site.id}, Domain: {site.domain}, Name: {site.name}")

# Verificar Social Apps
print("\n📱 SOCIAL APPS (Google):")
google_apps = SocialApp.objects.filter(provider='google')
print(f"   Total: {google_apps.count()}")
for app in google_apps:
    print(f"   - ID: {app.id}")
    print(f"     Name: {app.name}")
    print(f"     Client ID: {app.client_id}")
    print(f"     Sites asociados: {[f'ID:{s.id} ({s.domain})' for s in app.sites.all()]}")

# Verificar SITE_ID en settings
from django.conf import settings
print(f"\n⚙️ SITE_ID en settings.py: {settings.SITE_ID}")

# Intentar obtener la app como lo hace allauth
print("\n🧪 PRUEBA DE get_app():")
try:
    from allauth.socialaccount.models import SocialApp
    app = SocialApp.objects.get(provider='google')
    print(f"   ✅ Se obtuvo correctamente: {app.name}")
except SocialApp.MultipleObjectsReturned as e:
    print(f"   ❌ Error MultipleObjectsReturned: {e}")
    print("   📋 Apps encontradas:")
    apps = SocialApp.objects.filter(provider='google')
    for app in apps:
        print(f"      - {app.id}: {app.name} (Client ID: {app.client_id[:20]}...)")
except SocialApp.DoesNotExist:
    print(f"   ❌ No existe Social App de Google")

print("\n✅ Diagnóstico completado")

