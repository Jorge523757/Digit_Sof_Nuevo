"""
DIGIT SOFT - Script para crear usuario cliente de prueba
Ejecutar: python crear_usuario_cliente.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from clientes.models import Cliente

User = get_user_model()

print("=" * 70)
print("   👤 CREANDO USUARIO CLIENTE DE PRUEBA")
print("=" * 70)

# Datos del cliente
username = "cliente_demo"
email = "cliente@demo.com"
password = "cliente123"
first_name = "Roberto"
last_name = "García"
documento = "9999888877"
telefono = "3001112233"
direccion = "Calle Demo #123, Ciudad Demo"

# Verificar si ya existe
if User.objects.filter(username=username).exists():
    print(f"\n⚠️  El usuario '{username}' ya existe.")
    user = User.objects.get(username=username)
    print(f"\n📧 Email: {user.email}")
    print(f"🔑 Contraseña: {password}")
    print(f"👤 Tipo: Cliente (sin permisos staff)")
else:
    # Crear usuario
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    # Asegurarse de que NO sea staff ni superuser
    user.is_staff = False
    user.is_superuser = False
    user.save()

    # Actualizar perfil
    perfil = user.perfil
    perfil.tipo_usuario = 'CLIENTE'
    perfil.telefono = telefono
    perfil.direccion = direccion
    perfil.documento = documento
    perfil.save()

    # Crear registro en tabla clientes
    try:
        cliente, created = Cliente.objects.get_or_create(
            numero_documento=documento,
            defaults={
                'nombres': first_name,
                'apellidos': last_name,
                'telefono': telefono,
                'correo': email,
                'direccion': direccion,
                'activo': True
            }
        )

        # Vincular cliente con perfil
        perfil.cliente = cliente
        perfil.save()

        print(f"\n✅ Usuario cliente '{username}' creado exitosamente")
        print(f"\n📋 Información del Cliente:")
        print(f"   Nombre: {first_name} {last_name}")
        print(f"   Usuario: {username}")
        print(f"   Email: {email}")
        print(f"   Contraseña: {password}")
        print(f"   Documento: {documento}")
        print(f"   Teléfono: {telefono}")

    except Exception as e:
        print(f"\n⚠️  Error al crear cliente: {e}")

print("\n" + "=" * 70)
print("   🔐 CREDENCIALES DE ACCESO")
print("=" * 70)
print(f"\n   Usuario: {username}")
print(f"   Contraseña: {password}")
print(f"   Tipo: Cliente (acceso limitado)")

print("\n" + "=" * 70)
print("   🎯 CÓMO PROBAR LAS RESTRICCIONES")
print("=" * 70)
print("\n   1. Iniciar servidor: python manage.py runserver")
print("   2. Ir a: http://127.0.0.1:8000/usuarios/login/")
print(f"   3. Ingresar con: {username} / {password}")
print("   4. Intentar acceder a: http://127.0.0.1:8000/clientes/")
print("   5. Verás el mensaje: 'No tienes permisos...'")
print("   6. Serás redirigido al dashboard de cliente")

print("\n" + "=" * 70)
print("   📊 COMPARACIÓN DE ACCESOS")
print("=" * 70)
print("\n   ADMIN (admin/admin123):")
print("      ✅ Acceso COMPLETO a todos los módulos")
print("      ✅ Dashboard con estadísticas")
print("      ✅ Panel de administración Django")

print(f"\n   CLIENTE ({username}/{password}):")
print("      ❌ NO puede acceder a módulos administrativos")
print("      ✅ Dashboard limitado con info de contacto")
print("      ❌ NO tiene acceso al panel admin")

print("\n" + "=" * 70)
print("   ✅ ¡LISTO PARA PROBAR!")
print("=" * 70)

