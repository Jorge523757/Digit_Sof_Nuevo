"""
Script para vincular cuenta de Google a usuario existente
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount, SocialApp
from django.contrib.sites.models import Site

print("\n" + "="*80)
print("🔗 VINCULANDO CUENTA DE GOOGLE A USUARIO EXISTENTE")
print("="*80)

# Email del usuario
email = 'davidcristancho160@gmail.com'

print(f"\n[1] Buscando usuario con email: {email}")
try:
    user = User.objects.get(email__iexact=email)
    print(f"   ✅ Usuario encontrado: {user.username}")
    print(f"   - Nombre: {user.first_name} {user.last_name}")
    print(f"   - Email: {user.email}")
except User.DoesNotExist:
    print(f"   ❌ No se encontró usuario con ese email")
    exit(1)

print(f"\n[2] Verificando si ya tiene cuenta de Google vinculada...")
existing_social = SocialAccount.objects.filter(user=user, provider='google')
if existing_social.exists():
    print(f"   ✅ Ya tiene cuenta de Google vinculada")
    print(f"   - UID: {existing_social.first().uid}")
else:
    print(f"   ❌ NO tiene cuenta de Google vinculada todavía")

print(f"\n[3] Verificando perfil de usuario...")
try:
    perfil = user.perfil
    print(f"   ✅ Tiene perfil: {perfil.get_tipo_usuario_display()}")
except:
    print(f"   ⚠️  No tiene perfil, creando...")
    from usuarios.models import PerfilUsuario
    perfil = PerfilUsuario.objects.create(
        user=user,
        tipo_usuario='CLIENTE',
        activo=True,
        bloqueado=False
    )
    print(f"   ✅ Perfil creado")

print("\n" + "="*80)
print("✅ USUARIO LISTO PARA VINCULAR CON GOOGLE")
print("="*80)

print(f"\n📋 INFORMACIÓN DEL USUARIO:")
print(f"   - Username: {user.username}")
print(f"   - Email: {user.email}")
print(f"   - Nombre completo: {user.first_name} {user.last_name}")
print(f"   - Perfil: {perfil.get_tipo_usuario_display()}")
print(f"   - Activo: {user.is_active}")

print("\n" + "="*80)
print("🚀 PRÓXIMOS PASOS")
print("="*80)

print("\n1. REINICIA EL SERVIDOR Django")
print("2. Ve a: http://127.0.0.1:8000/usuarios/login/")
print("3. Haz clic en 'Continuar con Google'")
print("4. Selecciona: davidcristancho160@gmail.com")
print("\nAhora debería:")
print("   ✅ Vincular automáticamente tu cuenta de Google")
print("   ✅ Redirigirte al dashboard")
print("   ✅ Funcionar correctamente")

print("\n" + "="*80)
print("⚠️  IMPORTANTE")
print("="*80)
print("\nSi aún te pide completar el registro:")
print("   - Simplemente haz clic en 'Completar Registro'")
print("   - La cuenta se vinculará automáticamente")
print("   - Serás redirigido al dashboard")

print("\n" + "="*80 + "\n")

