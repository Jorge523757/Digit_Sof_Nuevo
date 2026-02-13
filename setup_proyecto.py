#!/usr/bin/env python
"""
CONFIGURACIÓN AUTOMÁTICA DEL PROYECTO DIGIT SOFT
Ejecuta este script después de clonar el repositorio
"""

import os
import sys
import subprocess
import platform

def print_header(text):
    """Imprime un encabezado decorado"""
    print("\n" + "="*70)
    print(f"   {text}")
    print("="*70 + "\n")

def print_step(number, text):
    """Imprime un paso numerado"""
    print(f"\n{'='*70}")
    print(f"   PASO {number}: {text}")
    print(f"{'='*70}\n")

def run_command(command, description):
    """Ejecuta un comando y muestra el resultado"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Completado")
            return True
        else:
            print(f"❌ Error en {description}")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print_header("🚀 CONFIGURACIÓN AUTOMÁTICA - DIGIT SOFT")
    print("Este script configurará automáticamente el proyecto")
    print("Incluye: instalación de dependencias, migraciones y datos iniciales")

    input("\nPresiona Enter para continuar...")

    # Paso 1: Instalar dependencias
    print_step(1, "INSTALANDO DEPENDENCIAS")
    if not run_command("pip install -r requirements.txt", "Instalación de dependencias"):
        print("\n⚠️  Advertencia: Algunas dependencias pueden haber fallado")
        continuar = input("¿Deseas continuar? (s/n): ")
        if continuar.lower() != 's':
            sys.exit(1)

    # Paso 2: Aplicar migraciones
    print_step(2, "APLICANDO MIGRACIONES DE BASE DE DATOS")
    run_command("python manage.py migrate", "Migraciones de base de datos")

    # Paso 3: Crear superusuario automáticamente
    print_step(3, "CREANDO SUPERUSUARIO")
    print("📝 Creando usuario administrador con credenciales predeterminadas:")
    print("   Usuario: admin")
    print("   Contraseña: admin123")
    print("   Email: admin@digitsoft.com")

    # Crear superusuario usando script Python
    create_superuser_script = """
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Verificar si ya existe el superusuario
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@digitsoft.com',
        password='admin123',
        first_name='Administrador',
        last_name='Sistema'
    )
    print("✅ Superusuario 'admin' creado exitosamente")
else:
    print("ℹ️  El superusuario 'admin' ya existe")
"""

    with open('temp_create_superuser.py', 'w', encoding='utf-8') as f:
        f.write(create_superuser_script)

    run_command("python temp_create_superuser.py", "Creación de superusuario")

    # Eliminar archivo temporal
    if os.path.exists('temp_create_superuser.py'):
        os.remove('temp_create_superuser.py')

    # Paso 4: Crear vistas SQL (si existe el script)
    print_step(4, "CONFIGURANDO VISTAS SQL")
    if os.path.exists('gestionar_vistas_ordenes.py'):
        run_command("python gestionar_vistas_ordenes.py crear", "Creación de vistas SQL")
    else:
        print("ℹ️  Script de vistas SQL no encontrado (opcional)")

    # Paso 5: Recolectar archivos estáticos
    print_step(5, "RECOLECTANDO ARCHIVOS ESTÁTICOS")
    run_command("python manage.py collectstatic --noinput", "Archivos estáticos")

    # Finalización
    print_header("✅ CONFIGURACIÓN COMPLETADA")
    print("\n🎉 ¡El proyecto está listo para usar!\n")
    print("📋 CREDENCIALES DE ACCESO:")
    print("   URL: http://127.0.0.1:8000")
    print("   Usuario: admin")
    print("   Contraseña: admin123")
    print("\n🚀 PARA INICIAR EL SERVIDOR:")
    print("   python manage.py runserver")
    print("\n" + "="*70 + "\n")

if __name__ == '__main__':
    main()

