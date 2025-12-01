"""
DIGT SOFT - Inicializador Completo del Sistema
Crea superusuario y pobla la base de datos con datos de prueba
Este script se ejecuta automáticamente al clonar el proyecto
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.db import connection

User = get_user_model()


def print_banner():
    """Imprime un banner de bienvenida"""
    print("\n" + "=" * 70)
    print("🚀 DIGIT SOFT - INICIALIZADOR AUTOMÁTICO DEL SISTEMA 🚀")
    print("=" * 70 + "\n")


def check_database():
    """Verifica si la base de datos está inicializada"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM django_migrations")
            count = cursor.fetchone()[0]
            return count > 0
    except:
        return False


def create_superuser():
    """Crea un superusuario si no existe"""
    print("\n" + "-" * 70)
    print("👤 PASO 1: Creando Superusuario")
    print("-" * 70)
    
    username = "admin"
    email = "admin@digitsoft.com"
    password = "admin123"
    
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print(f"✅ Superusuario '{username}' actualizado correctamente")
    else:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"✅ Superusuario '{username}' creado correctamente")
    
    print(f"\n📧 Email: {email}")
    print(f"🔑 Contraseña: {password}")
    print(f"\n⚠️  IMPORTANTE: Cambia esta contraseña en producción")
    print(f"🌐 Panel Admin: http://127.0.0.1:8000/admin/")


def populate_database():
    """Pobla la base de datos con datos de prueba"""
    print("\n" + "-" * 70)
    print("📦 PASO 2: Poblando Base de Datos con Datos de Prueba")
    print("-" * 70 + "\n")
    
    # Poblar Clientes
    print("👥 Generando clientes...")
    call_command('populate_clientes', 30, '--clear')
    
    print("\n")
    
    # Poblar Proveedores
    print("🏢 Generando proveedores...")
    call_command('populate_proveedores', 15, '--clear')
    
    print("\n")
    
    # Poblar Productos
    print("📦 Generando productos...")
    call_command('populate_productos', 50, '--clear')


def main():
    """Función principal"""
    print_banner()
    
    try:
        # Verificar si hay migraciones pendientes
        if not check_database():
            print("⚠️  Base de datos no inicializada. Aplicando migraciones...")
            call_command('migrate')
            print("✅ Migraciones aplicadas correctamente\n")
        
        # Crear superusuario
        create_superuser()
        
        # Poblar base de datos
        populate_database()
        
        # Mensaje final
        print("\n" + "=" * 70)
        print("✅ SISTEMA INICIALIZADO CORRECTAMENTE")
        print("=" * 70)
        print("\n🎉 Tu sistema DIGIT SOFT está listo para usarse!")
        print("\n📋 Próximos pasos:")
        print("   1. Ejecuta: python manage.py runserver")
        print("   2. Accede al panel admin: http://127.0.0.1:8000/admin/")
        print("   3. Usuario: admin | Contraseña: admin123")
        print("\n💡 Tip: Explora los datos de prueba generados para familiarizarte con el sistema")
        print("=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error durante la inicialización: {str(e)}")
        print("Por favor, revisa los errores e intenta nuevamente.")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

