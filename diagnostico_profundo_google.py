"""
Diagnóstico profundo de la base de datos para encontrar duplicados
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from allauth.socialaccount.models import SocialApp
from django.db import connection

print("\n" + "="*80)
print("🔍 DIAGNÓSTICO PROFUNDO DE BASE DE DATOS")
print("="*80)

# Consulta SQL directa para ver todos los registros
print("\n[1] Consultando tabla socialaccount_socialapp directamente...")
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT id, provider, name, client_id
        FROM socialaccount_socialapp
        WHERE provider = 'google'
    """)
    rows = cursor.fetchall()

    print(f"\n   Registros encontrados: {len(rows)}")
    for row in rows:
        print(f"\n   ID: {row[0]}")
        print(f"   Provider: {row[1]}")
        print(f"   Name: {row[2]}")
        print(f"   Client ID: {row[3]}")

# Consulta ORM
print("\n[2] Consultando con Django ORM...")
apps = SocialApp.objects.filter(provider='google')
print(f"\n   Apps encontradas: {apps.count()}")
for app in apps:
    print(f"\n   ID: {app.id}")
    print(f"   Provider: {app.provider}")
    print(f"   Name: {app.name}")
    print(f"   Client ID: {app.client_id}")
    sites = app.sites.all()
    print(f"   Sites: {[s.domain for s in sites]}")

# Verificar tabla intermedia
print("\n[3] Verificando tabla intermedia socialaccount_socialapp_sites...")
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT id, socialapp_id, site_id
        FROM socialaccount_socialapp_sites
    """)
    rows = cursor.fetchall()

    print(f"\n   Registros encontrados: {len(rows)}")
    for row in rows:
        print(f"   ID: {row[0]} | App ID: {row[1]} | Site ID: {row[2]}")

print("\n" + "="*80)
print("🔧 ANÁLISIS")
print("="*80)

if apps.count() > 1:
    print("\n❌ PROBLEMA: Hay múltiples configuraciones de Google OAuth")
    print("   Ejecuta: python ARREGLAR_GOOGLE_DEFINITIVO.py")
elif apps.count() == 1:
    print("\n✅ CORRECTO: Solo hay una configuración")
    app = apps.first()
    if app.sites.count() == 0:
        print("   ⚠️  PROBLEMA: La app no está asociada a ningún site")
    elif app.sites.count() > 1:
        print("   ⚠️  PROBLEMA: La app está asociada a múltiples sites")
    else:
        print("   ✅ CORRECTO: La app está asociada a un site")
else:
    print("\n⚠️  No hay configuraciones de Google OAuth")
    print("   Ejecuta: python ARREGLAR_GOOGLE_DEFINITIVO.py")

print("\n" + "="*80 + "\n")

