"""
Script para verificar y crear un superusuario si no existe
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

def verificar_y_crear_superusuario():
    # Verificar si existen superusuarios
    superusuarios = User.objects.filter(is_superuser=True)

    print("=" * 60)
    print("VERIFICACIÓN DE SUPERUSUARIOS")
    print("=" * 60)

    if superusuarios.exists():
        print(f"\n✓ Se encontraron {superusuarios.count()} superusuario(s):\n")
        for user in superusuarios:
            print(f"  - Usuario: {user.username}")
            print(f"    Email: {user.email or '(sin email)'}")
            print(f"    Activo: {'Sí' if user.is_active else 'No'}")
            print()

        respuesta = input("¿Deseas crear otro superusuario? (s/n): ").lower().strip()
        if respuesta != 's':
            print("\nNo se creó ningún superusuario nuevo.")
            return
    else:
        print("\n⚠ No se encontraron superusuarios en el sistema.\n")

    # Crear nuevo superusuario
    print("\n" + "=" * 60)
    print("CREAR NUEVO SUPERUSUARIO")
    print("=" * 60 + "\n")

    while True:
        username = input("Ingrese el nombre de usuario: ").strip()
        if not username:
            print("❌ El nombre de usuario no puede estar vacío.")
            continue

        if User.objects.filter(username=username).exists():
            print(f"❌ El usuario '{username}' ya existe. Intenta con otro nombre.")
            continue

        break

    while True:
        email = input("Ingrese el email (opcional, presiona Enter para omitir): ").strip()
        if email and User.objects.filter(email=email).exists():
            print(f"❌ El email '{email}' ya está registrado.")
            continue
        break

    while True:
        password = input("Ingrese la contraseña: ").strip()
        if len(password) < 4:
            print("❌ La contraseña debe tener al menos 4 caracteres.")
            continue

        password2 = input("Confirme la contraseña: ").strip()
        if password != password2:
            print("❌ Las contraseñas no coinciden. Intenta de nuevo.")
            continue

        break

    # Crear el superusuario
    try:
        user = User.objects.create_superuser(
            username=username,
            email=email if email else '',
            password=password
        )
        print("\n" + "=" * 60)
        print("✓ SUPERUSUARIO CREADO EXITOSAMENTE")
        print("=" * 60)
        print(f"\nUsuario: {user.username}")
        if user.email:
            print(f"Email: {user.email}")
        print("\nYa puedes iniciar sesión en el sistema con estas credenciales.")

    except Exception as e:
        print(f"\n❌ Error al crear el superusuario: {e}")

if __name__ == '__main__':
    try:
        verificar_y_crear_superusuario()
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

