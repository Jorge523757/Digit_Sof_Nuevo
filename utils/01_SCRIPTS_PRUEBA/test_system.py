#!/usr/bin/env python
"""
Script para probar funcionalidades básicas del sistema
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitsoft_project.settings')
sys.path.append(r'c:\Users\jorge\OneDrive - SENA\Carpetas Sin Comprimir\DIGIT SOFT\DIGIT SOFT')

django.setup()

from django.contrib.auth.models import User
from main.models import Cliente, Producto, Marca

def test_system():
    """Probar funcionalidades básicas"""
    print("🔍 Probando sistema Digit Soft...")
    
    # 1. Verificar usuarios
    print(f"\n👥 Usuarios registrados: {User.objects.count()}")
    admin = User.objects.filter(is_superuser=True).first()
    if admin:
        print(f"✅ Administrador encontrado: {admin.username}")
    else:
        print("❌ No hay administrador")
    
    # 2. Verificar modelos
    print(f"\n📊 Estadísticas:")
    print(f"   - Clientes: {Cliente.objects.count()}")
    print(f"   - Marcas: {Marca.objects.count()}")
    print(f"   - Productos: {Producto.objects.count()}")
    
    # 3. Crear datos de prueba si no existen
    if Cliente.objects.count() == 0:
        print("\n🔧 Creando datos de prueba...")
        try:
            # Crear marca de prueba
            marca = Marca.objects.create(
                nombre="Dell",
                descripcion="Marca de computadores"
            )
            
            # Crear cliente de prueba
            cliente = Cliente.objects.create(
                nombre="Juan Pérez",
                email="juan@test.com",
                telefono="123456789",
                direccion="Calle 123"
            )
            
            # Crear producto de prueba
            producto = Producto.objects.create(
                nombreProducto="Laptop Dell",
                descripcion="Laptop Dell Inspiron",
                precio=1500000,
                cantidad=10,
                marca=marca
            )
            
            print("✅ Datos de prueba creados")
        except Exception as e:
            print(f"❌ Error creando datos: {e}")
    
    print("\n🎉 Pruebas completadas")
    print("\n📋 Credenciales de administrador:")
    print("   Usuario: admin")
    print("   Contraseña: DigitSoft2025@Admin!")
    print("\n🌐 URLs disponibles:")
    print("   - Página principal: http://127.0.0.1:8000/")
    print("   - Login: http://127.0.0.1:8000/auth/login/")
    print("   - Registro: http://127.0.0.1:8000/auth/register/")

if __name__ == "__main__":
    test_system()