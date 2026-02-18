"""
Script para inicializar la base de datos con datos esenciales
Crea superusuario y datos básicos automáticamente
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError


def crear_superusuario():
    """Crea un superusuario predeterminado si no existe"""

    print("=" * 80)
    print("DIGT SOFT - Inicialización de Base de Datos")
    print("=" * 80)
    print()

    # Credenciales por defecto
    USERNAME = 'admin'
    EMAIL = 'admin@digitsoft.com'
    PASSWORD = 'admin123'

    # Verificar si ya existe un superusuario
    if User.objects.filter(is_superuser=True).exists():
        print("⚠️  Ya existe al menos un superusuario en la base de datos.")
        print()
        print("📋 Superusuarios existentes:")
        for su in User.objects.filter(is_superuser=True):
            print(f"   - {su.username} ({su.email})")
        print()
        return False

    # Crear superusuario
    try:
        user = User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )

        print("✅ Superusuario creado exitosamente!")
        print()
        print(f"   👤 Usuario: {USERNAME}")
        print(f"   📧 Email: {EMAIL}")
        print(f"   🔑 Contraseña: {PASSWORD}")
        print()
        print("⚠️  IMPORTANTE: Cambia la contraseña después del primer login!")
        print()
        print("Para acceder al panel de administración:")
        print("   1. Inicia el servidor: python manage.py runserver")
        print("   2. Visita: http://localhost:8000/admin/")
        print(f"   3. Usuario: {USERNAME}")
        print(f"   4. Contraseña: {PASSWORD}")
        print()

        return True

    except IntegrityError:
        print(f"❌ Error: El usuario '{USERNAME}' ya existe.")
        return False
    except Exception as e:
        print(f"❌ Error al crear superusuario: {str(e)}")
        return False


if __name__ == '__main__':
    try:
        crear_superusuario()
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

