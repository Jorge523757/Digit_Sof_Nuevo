"""
DIGITSOFT - Script para crear base de datos MySQL
Este script crea la base de datos digitsoft_db y el usuario digitsoft_user
"""

import subprocess
import getpass

def main():
    print("\n" + "="*70)
    print("    DIGITSOFT - CREAR BASE DE DATOS MYSQL")
    print("="*70 + "\n")

    # Ruta de MySQL
    mysql_path = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"

    print("📋 Este script creará:")
    print("   - Base de datos: digitsoft_db")
    print("   - Usuario: digitsoft_user")
    print("   - Password: digitsoft2024")
    print()

    # Pedir password de root
    root_password = getpass.getpass("🔑 Ingresa la password de root de MySQL: ")

    print("\n⏳ Creando base de datos...")

    # Comandos SQL
    sql_commands = """
DROP DATABASE IF EXISTS digitsoft_db;
CREATE DATABASE digitsoft_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'digitsoft_user'@'localhost' IDENTIFIED BY 'digitsoft2024';
GRANT ALL PRIVILEGES ON digitsoft_db.* TO 'digitsoft_user'@'localhost';
FLUSH PRIVILEGES;
USE digitsoft_db;
SELECT 'Base de datos digitsoft_db creada exitosamente!' AS STATUS;
"""

    try:
        # Ejecutar comando MySQL
        process = subprocess.Popen(
            [mysql_path, '-u', 'root', f'-p{root_password}'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate(input=sql_commands)

        if process.returncode == 0:
            print("\n" + "="*70)
            print("✅ BASE DE DATOS CREADA EXITOSAMENTE")
            print("="*70 + "\n")

            print("📊 Datos de conexión:")
            print("   Base de datos: digitsoft_db")
            print("   Usuario:       digitsoft_user")
            print("   Password:      digitsoft2024")
            print("   Host:          localhost")
            print("   Puerto:        3306")
            print()

            print("="*70)
            print("📝 PRÓXIMOS PASOS:")
            print("="*70)
            print("1. Ejecutar migraciones:")
            print("   python manage.py migrate")
            print()
            print("2. Crear superusuario:")
            print("   python manage.py createsuperuser")
            print()
            print("3. Iniciar servidor:")
            print("   python manage.py runserver")
            print()

        else:
            print("\n" + "="*70)
            print("❌ ERROR AL CREAR LA BASE DE DATOS")
            print("="*70 + "\n")
            print(f"Error: {stderr}")
            print()
            print("Verifica que:")
            print("- MySQL esté corriendo (services.msc)")
            print("- La password de root sea correcta")
            print("- El usuario root tenga permisos")

    except FileNotFoundError:
        print("\n❌ No se encontró MySQL en la ruta predeterminada")
        print(f"   Buscado en: {mysql_path}")
        print()
        print("Soluciones:")
        print("1. Verifica que MySQL esté instalado")
        print("2. Busca mysql.exe en tu computadora")
        print("3. Edita la variable mysql_path en este script")

    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()

