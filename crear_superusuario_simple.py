"""
Script simple para crear superusuario rápidamente
Uso: python crear_superusuario_simple.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Configuración del superusuario
USERNAME = 'admin'
EMAIL = 'admin@digtsoft.com'
PASSWORD = 'admin123'

try:
    if User.objects.filter(username=USERNAME).exists():
        print(f"⚠ El usuario '{USERNAME}' ya existe.")
        user = User.objects.get(username=USERNAME)
        print(f"Usuario: {user.username}")
        print(f"Email: {user.email}")
        print(f"Es superusuario: {user.is_superuser}")
    else:
        user = User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )
        print("✓ Superusuario creado exitosamente!")
        print(f"Usuario: {USERNAME}")
        print(f"Email: {EMAIL}")
        print(f"Contraseña: {PASSWORD}")
except Exception as e:
    print(f"❌ Error: {e}")

