"""
Script para verificar el estado de los usuarios y depurar problemas de registro
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario
from allauth.socialaccount.models import SocialAccount

print("\n" + "="*80)
print("🔍 DIAGNÓSTICO COMPLETO - USUARIOS Y REGISTRO GOOGLE")
print("="*80)

# 1. Usuarios totales
print("\n[1] USUARIOS EN EL SISTEMA:")
usuarios = User.objects.all()
print(f"   Total: {usuarios.count()}")
for user in usuarios:
    tiene_perfil = "✅" if hasattr(user, 'perfil') else "❌"
    es_google = "🔵" if SocialAccount.objects.filter(user=user, provider='google').exists() else "⚪"
    print(f"   {tiene_perfil} {es_google} {user.username} ({user.email})")

# 2. Cuentas sociales
print("\n[2] CUENTAS SOCIALES (GOOGLE):")
social_accounts = SocialAccount.objects.filter(provider='google')
print(f"   Total: {social_accounts.count()}")
for sa in social_accounts:
    print(f"   - {sa.user.username} ({sa.user.email})")
    print(f"     Provider: {sa.provider}")
    print(f"     UID: {sa.uid}")

# 3. Perfiles
print("\n[3] PERFILES DE USUARIO:")
perfiles = PerfilUsuario.objects.all()
print(f"   Total: {perfiles.count()}")
for perfil in perfiles:
    print(f"   - {perfil.user.username}: {perfil.get_tipo_usuario_display()}")
    print(f"     Activo: {perfil.activo}, Bloqueado: {perfil.bloqueado}")

# 4. Verificar el usuario específico
print("\n[4] VERIFICANDO davidcristancho160@gmail.com:")
try:
    user = User.objects.get(email='davidcristancho160@gmail.com')
    print(f"   ✅ Usuario existe: {user.username}")
    print(f"   - Email: {user.email}")
    print(f"   - Nombre: {user.first_name} {user.last_name}")
    print(f"   - Activo: {user.is_active}")
    print(f"   - Staff: {user.is_staff}")

    # Verificar perfil
    try:
        perfil = user.perfil
        print(f"   ✅ Tiene perfil: {perfil.get_tipo_usuario_display()}")
    except PerfilUsuario.DoesNotExist:
        print("   ❌ NO tiene perfil")

    # Verificar cuenta social
    try:
        social = SocialAccount.objects.get(user=user, provider='google')
        print(f"   ✅ Tiene cuenta de Google vinculada")
    except SocialAccount.DoesNotExist:
        print("   ❌ NO tiene cuenta de Google vinculada")

except User.DoesNotExist:
    print("   ❌ El usuario NO existe todavía")

print("\n" + "="*80)
print("📋 RECOMENDACIONES:")
print("="*80)

usuarios_sin_perfil = []
for user in usuarios:
    if not hasattr(user, 'perfil'):
        usuarios_sin_perfil.append(user)

if usuarios_sin_perfil:
    print(f"\n⚠️  Hay {len(usuarios_sin_perfil)} usuario(s) sin perfil:")
    for user in usuarios_sin_perfil:
        print(f"   - {user.username} ({user.email})")
    print("\n   Ejecuta: python arreglar_usuarios_google.py")
else:
    print("\n✅ Todos los usuarios tienen perfil")

print("\n" + "="*80 + "\n")

