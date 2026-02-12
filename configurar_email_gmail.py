#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para configurar el envío de emails de Gmail en DIGITSOFT
Ayuda a generar el archivo .env con las credenciales correctas
"""

import os
import sys

def print_banner():
    print("=" * 80)
    print("🚀 CONFIGURADOR DE EMAIL GMAIL - DIGITSOFT")
    print("=" * 80)
    print()

def print_instructions():
    print("📧 INSTRUCCIONES PARA OBTENER CONTRASEÑA DE APLICACIÓN DE GMAIL:")
    print()
    print("1. Ve a tu cuenta de Google: https://myaccount.google.com/")
    print("2. Busca 'Seguridad' en el menú lateral izquierdo")
    print("3. Activa la 'Verificación en dos pasos' (si no la tienes activada)")
    print("4. Ve a: https://myaccount.google.com/apppasswords")
    print("5. Selecciona 'Correo' y 'Windows Computer'")
    print("6. Haz clic en 'Generar'")
    print("7. Copia la contraseña de 16 caracteres que aparece")
    print()
    print("IMPORTANTE: NO uses tu contraseña normal de Gmail, usa la de aplicación")
    print()

def test_email_connection(email, password):
    """Prueba la conexión con Gmail"""
    import smtplib
    from email.mime.text import MIMEText

    try:
        print("\n⏳ Probando conexión con Gmail...")

        # Conectar al servidor SMTP de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        server.starttls()
        server.login(email, password)

        print("✅ ¡Conexión exitosa con Gmail!")
        print(f"✅ Email configurado: {email}")

        # Preguntar si quiere enviar un email de prueba
        enviar_prueba = input("\n¿Deseas enviar un email de prueba? (s/n): ").strip().lower()

        if enviar_prueba == 's':
            email_destino = input(f"Email de destino (Enter para enviar a {email}): ").strip() or email

            # Crear mensaje de prueba
            msg = MIMEText(
                "Este es un email de prueba desde DIGITSOFT.\n\n"
                "Si recibes este mensaje, la configuración de email está funcionando correctamente.\n\n"
                "Saludos,\nEquipo DIGITSOFT"
            )
            msg['Subject'] = '✅ Prueba de Email - DIGITSOFT'
            msg['From'] = f'DIGITSOFT <{email}>'
            msg['To'] = email_destino

            server.send_message(msg)
            print(f"✅ ¡Email de prueba enviado a {email_destino}!")
            print("   Revisa tu bandeja de entrada (puede tardar unos segundos)")

        server.quit()
        return True

    except smtplib.SMTPAuthenticationError:
        print("❌ Error de autenticación.")
        print("   - Verifica que la contraseña de aplicación sea correcta")
        print("   - Asegúrate de tener activada la verificación en dos pasos")
        return False
    except smtplib.SMTPException as e:
        print(f"❌ Error SMTP: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_env_file(email, password):
    """Crea el archivo .env con la configuración"""
    env_content = f"""# Configuración de Email - DIGITSOFT
# Generado automáticamente

# Backend de email (cambiar a console.EmailBackend para desarrollo)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

# Configuración SMTP de Gmail
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Credenciales de Gmail
EMAIL_HOST_USER={email}
EMAIL_HOST_PASSWORD={password}

# Email remitente
DEFAULT_FROM_EMAIL=DIGITSOFT <{email}>

# Email del administrador
ADMIN_EMAIL={email}

# URL del sitio
SITE_URL=http://localhost:8000

# Otras configuraciones
DEBUG=True
SECRET_KEY=django-insecure-digt-soft-2024-cambiar-en-produccion
"""

    env_path = os.path.join(os.path.dirname(__file__), '.env')

    # Si ya existe .env, preguntar si sobrescribir
    if os.path.exists(env_path):
        sobrescribir = input("\n⚠️  El archivo .env ya existe. ¿Sobrescribir? (s/n): ").strip().lower()
        if sobrescribir != 's':
            print("❌ Cancelado. No se modificó el archivo .env")
            return False

    try:
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write(env_content)
        print(f"\n✅ Archivo .env creado exitosamente en: {env_path}")
        return True
    except Exception as e:
        print(f"❌ Error al crear archivo .env: {e}")
        return False

def main():
    print_banner()
    print_instructions()

    # Solicitar credenciales
    print("=" * 80)
    print("📝 INGRESA TUS CREDENCIALES DE GMAIL")
    print("=" * 80)
    print()

    email = input("Email de Gmail: ").strip()

    if not email or '@' not in email:
        print("❌ Email inválido")
        return

    password = input("Contraseña de aplicación (16 caracteres): ").strip()

    if not password:
        print("❌ Debes ingresar la contraseña de aplicación")
        return

    # Limpiar espacios de la contraseña (Gmail los muestra con espacios)
    password = password.replace(' ', '')

    print()
    print("=" * 80)

    # Probar conexión
    if test_email_connection(email, password):
        print()
        print("=" * 80)

        # Crear archivo .env
        if create_env_file(email, password):
            print()
            print("=" * 80)
            print("🎉 ¡CONFIGURACIÓN COMPLETADA!")
            print("=" * 80)
            print()
            print("Próximos pasos:")
            print("1. Reinicia el servidor Django para que tome la nueva configuración")
            print("2. Prueba la recuperación de contraseña desde la aplicación")
            print("3. Los emails deberían llegar en menos de 1 minuto")
            print()
            print("Nota: Si usas variables de entorno, necesitas instalar python-dotenv:")
            print("      pip install python-dotenv")
            print()
    else:
        print()
        print("=" * 80)
        print("❌ No se pudo completar la configuración")
        print("=" * 80)
        print()
        print("Verifica:")
        print("- Que la contraseña de aplicación sea correcta (16 caracteres sin espacios)")
        print("- Que tengas activada la verificación en dos pasos en Gmail")
        print("- Que tu conexión a internet esté funcionando")
        print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Configuración cancelada por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

