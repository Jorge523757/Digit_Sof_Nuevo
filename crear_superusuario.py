"""
Script para crear un superusuario para el sistema Django
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Datos del superusuario
username = 'admin'
email = 'admin@digitsoft.com'
password = 'admin123'

# Verificar si el usuario ya existe
if User.objects.filter(username=username).exists():
    print(f"El usuario '{username}' ya existe.")
    user = User.objects.get(username=username)
    # Actualizar contraseña por si acaso
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(f"Usuario '{username}' actualizado correctamente.")
else:
    # Crear el superusuario
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"Superusuario '{username}' creado exitosamente!")

print("\n" + "="*50)
print("CREDENCIALES DE ACCESO")
print("="*50)
print(f"Username: {username}")
print(f"Email: {email}")
print(f"Password: {password}")
print("="*50)
print("\nPuedes acceder al admin en: http://127.0.0.1:8000/admin/")

