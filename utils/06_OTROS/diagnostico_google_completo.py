"""
Script de Diagnóstico Completo de Google OAuth
Verifica TODAS las configuraciones posibles que pueden causar MultipleObjectsReturned
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from django.contrib.sites.models import Site
from django.db import connection

print("=" * 80)
print("🔍 DIAGNÓSTICO COMPLETO DE GOOGLE OAUTH")
print("=" * 80)

# 1. Ver todas las Social Apps
print("\n📱 1. SOCIAL APPS EN LA BASE DE DATOS")
print("-" * 80)

all_apps = SocialApp.objects.all()
print(f"Total de Social Apps: {all_apps.count()}")

for app in all_apps:
    print(f"\n   App ID: {app.id}")
    print(f"   - Name: {app.name}")
    print(f"   - Provider: {app.provider}")
    print(f"   - Client ID: {app.client_id[:40]}...")
    print(f"   - Sites: {[s.domain for s in app.sites.all()]}")

# 2. Ver específicamente las de Google
print("\n📱 2. SOCIAL APPS DE GOOGLE")
print("-" * 80)

google_apps = SocialApp.objects.filter(provider='google')
print(f"Total de Apps de Google: {google_apps.count()}")

if google_apps.count() > 1:
    print("❌ ERROR: Hay múltiples configuraciones de Google!")
    print("   Esto causa el error MultipleObjectsReturned")
    print("\n   Detalles:")
    for idx, app in enumerate(google_apps, 1):
        print(f"\n   {idx}. ID: {app.id}")
        print(f"      Name: {app.name}")
        print(f"      Client ID: {app.client_id[:40]}...")
elif google_apps.count() == 1:
    print("✅ CORRECTO: Solo hay 1 configuración de Google")
    app = google_apps.first()
    print(f"   - ID: {app.id}")
    print(f"   - Name: {app.name}")
    print(f"   - Client ID: {app.client_id}")
else:
    print("❌ ERROR: No hay configuraciones de Google")

# 3. Ver las Social Apps sin filtro usando SQL directo
print("\n🔍 3. CONSULTA SQL DIRECTA")
print("-" * 80)

with connection.cursor() as cursor:
    cursor.execute("SELECT id, provider, name, client_id FROM socialaccount_socialapp")
    rows = cursor.fetchall()

    print(f"Registros en socialaccount_socialapp: {len(rows)}")
    for row in rows:
        print(f"   ID: {row[0]} | Provider: {row[1]} | Name: {row[2]} | Client ID: {row[3][:40]}...")

# 4. Ver relación con Sites
print("\n🌐 4. RELACIÓN CON SITES")
print("-" * 80)

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT sa.id, sa.provider, sa.name, s.domain 
        FROM socialaccount_socialapp sa
        LEFT JOIN socialaccount_socialapp_sites sas ON sa.id = sas.socialapp_id
        LEFT JOIN django_site s ON sas.site_id = s.id
    """)
    rows = cursor.fetchall()

    print(f"Relaciones App-Site: {len(rows)}")
    for row in rows:
        print(f"   App ID: {row[0]} | Provider: {row[1]} | Name: {row[2]} | Site: {row[3]}")

# 5. Ver Social Accounts (cuentas de usuarios conectadas)
print("\n👥 5. SOCIAL ACCOUNTS (Usuarios con Google)")
print("-" * 80)

google_accounts = SocialAccount.objects.filter(provider='google')
print(f"Usuarios con cuenta de Google conectada: {google_accounts.count()}")

for account in google_accounts[:5]:  # Mostrar solo los primeros 5
    print(f"   - User: {account.user.username} | UID: {account.uid}")

# 6. Verificar tokens
print("\n🔑 6. SOCIAL TOKENS")
print("-" * 80)

tokens = SocialToken.objects.filter(app__provider='google')
print(f"Tokens de Google activos: {tokens.count()}")

# RESUMEN Y SOLUCIÓN
print("\n" + "=" * 80)
print("📊 RESUMEN Y DIAGNÓSTICO")
print("=" * 80)

total_google = SocialApp.objects.filter(provider='google').count()

if total_google == 0:
    print("❌ PROBLEMA: No hay configuración de Google OAuth")
    print("   SOLUCIÓN: Ejecuta python limpieza_total_google.py")
elif total_google == 1:
    print("✅ CORRECTO: Hay exactamente 1 configuración de Google OAuth")
    print("   El error MultipleObjectsReturned NO debería ocurrir")
    print("\n   Si aún ves el error:")
    print("   1. Reinicia el servidor Django (Ctrl+C y python manage.py runserver)")
    print("   2. Limpia el caché del navegador")
    print("   3. Intenta en modo incógnito")
else:
    print(f"❌ PROBLEMA: Hay {total_google} configuraciones de Google OAuth")
    print("   SOLUCIÓN:")
    print("   1. Ejecuta: python limpieza_total_google.py")
    print("   2. Reinicia el servidor Django")
    print("   3. Verifica con: python diagnostico_google_completo.py")

print("\n" + "=" * 80)

