"""
Script para verificar y corregir el perfil del usuario Teodoro12
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

# Buscar usuario Teodoro12
try:
    user = User.objects.get(username='Teodoro12')
    print(f"✅ Usuario encontrado: {user.username}")
    print(f"   Email: {user.email}")
    print(f"   Is Staff: {user.is_staff}")
    print(f"   Is Superuser: {user.is_superuser}")

    # Verificar perfil
    try:
        perfil = user.perfil
        print(f"\n✅ Perfil encontrado:")
        print(f"   Tipo Usuario: {perfil.tipo_usuario}")

        if perfil.tipo_usuario != 'CLIENTE':
            print(f"\n⚠️ El perfil NO es CLIENTE, corrigiendo...")
            perfil.tipo_usuario = 'CLIENTE'
            perfil.save()
            print(f"✅ Perfil actualizado a CLIENTE")
        else:
            print(f"\n✅ El perfil YA es CLIENTE")

    except PerfilUsuario.DoesNotExist:
        print(f"\n❌ El usuario NO tiene perfil, creando...")
        perfil = PerfilUsuario.objects.create(
            user=user,
            tipo_usuario='CLIENTE'
        )
        print(f"✅ Perfil CLIENTE creado")

except User.DoesNotExist:
    print("❌ Usuario Teodoro12 NO encontrado")
except Exception as e:
    print(f"❌ Error: {e}")

