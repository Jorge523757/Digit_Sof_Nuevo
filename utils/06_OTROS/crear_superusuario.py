"""
Script para crear o actualizar superusuario con contraseña
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Datos del superusuario
USERNAME = 'admin'
EMAIL = 'admin@digitsoft.com'
PASSWORD = 'admin123'  # Contraseña por defecto

try:
    # Intentar obtener el usuario
    user = User.objects.get(username=USERNAME)
    print(f"✅ Usuario '{USERNAME}' ya existe")

    # Actualizar contraseña
    user.set_password(PASSWORD)
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.email = EMAIL
    user.save()

    print(f"✅ Contraseña actualizada para '{USERNAME}'")

except User.DoesNotExist:
    # Crear nuevo superusuario
    user = User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD
    )
    print(f"✅ Superusuario '{USERNAME}' creado exitosamente")

print()
print("=" * 60)
print("CREDENCIALES DEL SUPERUSUARIO")
print("=" * 60)
print(f"Usuario:    {USERNAME}")
print(f"Email:      {EMAIL}")
print(f"Contraseña: {PASSWORD}")
print("=" * 60)
print()
print("Puedes acceder en:")
print("http://127.0.0.1:8000/admin/")
print("http://127.0.0.1:8000/usuarios/login/")
print()
print("⚠️ IMPORTANTE: Cambia la contraseña después del primer login")

