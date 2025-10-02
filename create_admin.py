#!/usr/bin/env python
"""
Script para crear un usuario administrador único
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitsoft_project.settings')
sys.path.append(r'c:\Users\jorge\OneDrive - SENA\Carpetas Sin Comprimir\DIGIT SOFT\DIGIT SOFT')

django.setup()

from django.contrib.auth.models import User

def create_admin():
    """Crear usuario administrador único"""
    admin_username = 'admin'
    admin_email = 'admin@digitsoft.com'
    admin_password = 'admin123'  # Contraseña por defecto, cambiar después
    
    # Verificar si ya existe
    if User.objects.filter(username=admin_username).exists():
        print(f"El usuario '{admin_username}' ya existe.")
        admin = User.objects.get(username=admin_username)
    else:
        # Crear superusuario
        admin = User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password,
            first_name='Administrador',
            last_name='Sistema'
        )
        print(f"Superusuario '{admin_username}' creado exitosamente.")
    
    print(f"Usuario: {admin.username}")
    print(f"Email: {admin.email}")
    print(f"Es superusuario: {admin.is_superuser}")
    print(f"Es staff: {admin.is_staff}")
    print("Contraseña por defecto: admin123")
    
    return admin

if __name__ == "__main__":
    create_admin()