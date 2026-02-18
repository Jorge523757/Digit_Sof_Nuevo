"""
Script para arreglar usuarios de Google sin perfil
Crea automáticamente el perfil para usuarios que se registraron con Google
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario
from allauth.socialaccount.models import SocialAccount

print("\n" + "="*80)
print("🔧 ARREGLANDO USUARIOS DE GOOGLE SIN PERFIL")
print("="*80)

# 1. Buscar usuarios con cuenta de Google
print("\n[1/3] Buscando usuarios con cuenta de Google...")
google_accounts = SocialAccount.objects.filter(provider='google')
print(f"   Encontrados: {google_accounts.count()} usuario(s) con cuenta de Google")

# 2. Verificar cuáles NO tienen perfil
print("\n[2/3] Verificando perfiles...")
usuarios_sin_perfil = []

for social_account in google_accounts:
    user = social_account.user
    try:
        perfil = user.perfil
        print(f"   ✅ {user.username} ({user.email}) - Ya tiene perfil")
    except PerfilUsuario.DoesNotExist:
        usuarios_sin_perfil.append(user)
        print(f"   ❌ {user.username} ({user.email}) - SIN PERFIL")

# 3. Crear perfiles faltantes
if usuarios_sin_perfil:
    print(f"\n[3/3] Creando {len(usuarios_sin_perfil)} perfil(es)...")
    for user in usuarios_sin_perfil:
        perfil = PerfilUsuario.objects.create(
            user=user,
            tipo_usuario='CLIENTE',
            activo=True,
            bloqueado=False
        )
        print(f"   ✅ Perfil creado para: {user.username} ({user.email})")
else:
    print("\n[3/3] ✅ Todos los usuarios ya tienen perfil")

print("\n" + "="*80)
print("✅ PROCESO COMPLETADO")
print("="*80)

# Resumen final
total_usuarios = User.objects.count()
total_perfiles = PerfilUsuario.objects.count()
total_google = google_accounts.count()

print(f"\n📊 RESUMEN:")
print(f"   - Total de usuarios: {total_usuarios}")
print(f"   - Total de perfiles: {total_perfiles}")
print(f"   - Usuarios con Google: {total_google}")

if total_usuarios == total_perfiles:
    print("\n   ✅ TODOS LOS USUARIOS TIENEN PERFIL")
else:
    print(f"\n   ⚠️  Hay {total_usuarios - total_perfiles} usuario(s) sin perfil")

print("\n" + "="*80)
print("🚀 AHORA PUEDES INICIAR SESIÓN CON GOOGLE")
print("="*80)
print("\n1. Ve a: http://127.0.0.1:8000/usuarios/login/")
print("2. Haz clic en 'Continuar con Google'")
print("3. Selecciona: davidcristancho160@gmail.com")
print("4. ¡Deberías entrar al dashboard directamente!")
print("\n" + "="*80 + "\n")

