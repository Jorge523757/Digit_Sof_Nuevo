#!/usr/bin/env python
"""
Script para cambiar la contraseña del administrador
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitsoft_project.settings')
sys.path.append(r'c:\Users\jorge\OneDrive - SENA\Carpetas Sin Comprimir\DIGIT SOFT\DIGIT SOFT')

django.setup()

from django.contrib.auth.models import User

def change_admin_password():
    """Cambiar contraseña del administrador"""
    try:
        admin = User.objects.get(username='admin')
        
        # Nueva contraseña más segura
        new_password = 'DigitSoft2025@Admin!'
        admin.set_password(new_password)
        admin.save()
        
        print("✅ Contraseña del administrador cambiada exitosamente")
        print(f"👤 Usuario: {admin.username}")
        print(f"🔐 Nueva contraseña: {new_password}")
        print("🚨 IMPORTANTE: Guarda esta contraseña en un lugar seguro")
        
        return True
    except User.DoesNotExist:
        print("❌ No se encontró el usuario administrador")
        return False

if __name__ == "__main__":
    change_admin_password()