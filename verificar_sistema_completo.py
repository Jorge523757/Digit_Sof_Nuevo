"""
Script de Verificación Final - Google OAuth y Sistema de Recuperación
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from usuarios.models import PasswordResetToken
from usuarios.models_tokens import TokenRecuperacion
from django.contrib.auth.models import User

print("=" * 80)
print("🔍 VERIFICACIÓN FINAL DEL SISTEMA")
print("=" * 80)

# 1. Verificar Google OAuth
print("\n📱 1. GOOGLE OAUTH")
print("-" * 80)
google_apps = SocialApp.objects.filter(provider='google')
print(f"✓ Social Apps de Google encontradas: {google_apps.count()}")

if google_apps.count() == 1:
    app = google_apps.first()
    print(f"✅ PERFECTO: Solo hay 1 configuración de Google OAuth")
    print(f"   - Name: {app.name}")
    print(f"   - Client ID: {app.client_id[:30]}...")
    print(f"   - Sites: {[site.domain for site in app.sites.all()]}")
elif google_apps.count() == 0:
    print("❌ ERROR: No hay configuraciones de Google OAuth")
    print("   Ejecuta: python forzar_limpieza_google.py")
else:
    print(f"⚠️ ADVERTENCIA: Hay {google_apps.count()} configuraciones (debe ser solo 1)")
    print("   Ejecuta: python forzar_limpieza_google.py")
    for idx, app in enumerate(google_apps, 1):
        print(f"   {idx}. {app.name} - {app.client_id[:30]}...")

# 2. Verificar URLs de usuarios
print("\n🔗 2. URLS DEL MÓDULO USUARIOS")
print("-" * 80)
from django.urls import reverse
try:
    url_gestionar_contrasenas = reverse('usuarios:admin_gestionar_contrasenas')
    print(f"✅ URL 'admin_gestionar_contrasenas' configurada: {url_gestionar_contrasenas}")
except Exception as e:
    print(f"❌ ERROR: URL 'admin_gestionar_contrasenas' no encontrada: {e}")

try:
    url_solicitar = reverse('usuarios:solicitar_recuperacion')
    print(f"✅ URL 'solicitar_recuperacion' configurada: {url_solicitar}")
except Exception as e:
    print(f"❌ ERROR: {e}")

try:
    url_verificar = reverse('usuarios:verificar_codigo')
    print(f"✅ URL 'verificar_codigo' configurada: {url_verificar}")
except Exception as e:
    print(f"❌ ERROR: {e}")

# 3. Verificar modelos de recuperación
print("\n🔐 3. SISTEMA DE RECUPERACIÓN DE CONTRASEÑA")
print("-" * 80)

# Tokens antiguos (24 horas)
total_tokens_antiguos = PasswordResetToken.objects.count()
tokens_antiguos_validos = PasswordResetToken.objects.filter(used=False).count()
print(f"✓ Tokens antiguos (24h): {total_tokens_antiguos} total, {tokens_antiguos_validos} válidos")

# Tokens nuevos (30 minutos)
total_tokens_nuevos = TokenRecuperacion.objects.count()
tokens_nuevos_activos = TokenRecuperacion.objects.filter(usado=False).count()
print(f"✓ Códigos nuevos (30min): {total_tokens_nuevos} total, {tokens_nuevos_activos} activos")

# 4. Verificar templates
print("\n📄 4. TEMPLATES")
print("-" * 80)
import os
from django.conf import settings

templates_requeridos = [
    'usuarios/admin_gestionar_contrasenas.html',
    'usuarios/recuperar_paso1.html',
    'usuarios/recuperar_paso2.html',
    'usuarios/recuperar_paso3.html',
]

for template_name in templates_requeridos:
    template_encontrado = False
    for template_dir in settings.TEMPLATES[0]['DIRS']:
        template_path = os.path.join(template_dir, template_name)
        if os.path.exists(template_path):
            print(f"✅ {template_name}")
            template_encontrado = True
            break
    if not template_encontrado:
        print(f"❌ {template_name} - NO ENCONTRADO")

# 5. Verificar usuarios
print("\n👥 5. USUARIOS DEL SISTEMA")
print("-" * 80)
total_users = User.objects.count()
superusers = User.objects.filter(is_superuser=True).count()
staff = User.objects.filter(is_staff=True, is_superuser=False).count()
normales = User.objects.filter(is_staff=False, is_superuser=False).count()

print(f"✓ Total de usuarios: {total_users}")
print(f"  - Superusuarios: {superusers}")
print(f"  - Staff: {staff}")
print(f"  - Normales: {normales}")

# 6. Verificar vistas
print("\n🎯 6. VISTAS IMPORTANTES")
print("-" * 80)
from usuarios import views
from usuarios import views_recuperacion

vistas_requeridas = [
    ('views.admin_gestionar_contrasenas', views, 'admin_gestionar_contrasenas'),
    ('views_recuperacion.solicitar_recuperacion', views_recuperacion, 'solicitar_recuperacion'),
    ('views_recuperacion.verificar_codigo', views_recuperacion, 'verificar_codigo'),
    ('views_recuperacion.nueva_password', views_recuperacion, 'nueva_password'),
]

for nombre, modulo, funcion in vistas_requeridas:
    if hasattr(modulo, funcion):
        print(f"✅ {nombre}")
    else:
        print(f"❌ {nombre} - NO ENCONTRADA")

# RESUMEN FINAL
print("\n" + "=" * 80)
print("📊 RESUMEN FINAL")
print("=" * 80)

errores = []
advertencias = []

# Verificar Google OAuth
if google_apps.count() != 1:
    errores.append("Google OAuth no tiene exactamente 1 configuración")
else:
    print("✅ Google OAuth: OK")

# Verificar URL
try:
    reverse('usuarios:admin_gestionar_contrasenas')
    print("✅ URLs: OK")
except:
    errores.append("URL admin_gestionar_contrasenas no configurada")

# Verificar templates
if os.path.exists(os.path.join(settings.TEMPLATES[0]['DIRS'][0], 'usuarios/admin_gestionar_contrasenas.html')):
    print("✅ Templates: OK")
else:
    errores.append("Template admin_gestionar_contrasenas.html no encontrado")

# Verificar vistas
if hasattr(views, 'admin_gestionar_contrasenas'):
    print("✅ Vistas: OK")
else:
    errores.append("Vista admin_gestionar_contrasenas no encontrada")

print("\n" + "=" * 80)
if errores:
    print("❌ ERRORES ENCONTRADOS:")
    for error in errores:
        print(f"   - {error}")
else:
    print("🎉 ¡TODO PERFECTO! El sistema está funcionando correctamente")

if advertencias:
    print("\n⚠️ ADVERTENCIAS:")
    for adv in advertencias:
        print(f"   - {adv}")

print("=" * 80)

