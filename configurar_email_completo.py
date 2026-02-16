"""
CONFIGURADOR AUTOMÁTICO DE EMAIL - DIGIT SOFT
==============================================
Este script configura el envío de emails automáticamente.
"""

import os
import sys
import smtplib
import webbrowser
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Colores para la consola
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("=" * 80)
    print(f"{BOLD}{BLUE}🚀 CONFIGURACIÓN AUTOMÁTICA DE EMAIL - DIGIT SOFT{RESET}")
    print("=" * 80)
    print()

def check_current_config():
    """Verifica la configuración actual del archivo .env"""
    env_path = Path('.env')

    if not env_path.exists():
        return None, None

    email = None
    password = None

    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('EMAIL_HOST_USER='):
                    email = line.split('=', 1)[1].strip()
                elif line.startswith('EMAIL_HOST_PASSWORD='):
                    password = line.split('=', 1)[1].strip()
    except Exception as e:
        print(f"{RED}❌ Error leyendo .env: {e}{RESET}")
        return None, None

    return email, password

def test_smtp_connection(email, password):
    """Prueba la conexión SMTP con Gmail"""
    try:
        print(f"{YELLOW}⏳ Probando conexión con Gmail...{RESET}")

        # Conectar a Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        server.starttls()
        server.login(email, password)
        server.quit()

        print(f"{GREEN}✅ ¡Conexión exitosa con Gmail!{RESET}")
        return True

    except smtplib.SMTPAuthenticationError:
        print(f"{RED}❌ Error de autenticación - Contraseña incorrecta{RESET}")
        return False
    except Exception as e:
        print(f"{RED}❌ Error de conexión: {e}{RESET}")
        return False

def send_test_email(email, password):
    """Envía un email de prueba"""
    try:
        print(f"{YELLOW}⏳ Enviando email de prueba a {email}...{RESET}")

        # Crear el mensaje
        msg = MIMEMultipart('alternative')
        msg['Subject'] = '✅ DIGIT SOFT - Configuración Exitosa'
        msg['From'] = f'DIGIT SOFT <{email}>'
        msg['To'] = email

        # Contenido del email
        text = """
¡Felicidades!

Tu sistema de envío de emails está configurado correctamente.

Ahora todos los códigos de recuperación de contraseña llegarán automáticamente
al email de cada usuario.

- DIGIT SOFT
        """

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 20px auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .header {{  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #00b4d8 100%) !important; color: white; padding: 40px 20px; text-align: center; }}
        .content {{ padding: 40px 30px; }}
        .success-box {{ background: #d4edda; border: 2px solid #28a745; border-radius: 10px; padding: 20px; text-align: center; margin: 20px 0; }}
        .footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #6c757d; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin: 0;">✅ ¡Configuración Exitosa!</h1>
            <p style="margin: 10px 0 0 0;">DIGIT SOFT</p>
        </div>
        <div class="content">
            <div class="success-box">
                <h2 style="color: #28a745; margin: 0 0 10px 0;">🎉 ¡Todo funcionando!</h2>
                <p style="margin: 0;">Tu sistema de envío de emails está configurado correctamente</p>
            </div>
            
            <h3>✅ ¿Qué significa esto?</h3>
            <ul>
                <li>Los códigos de recuperación de contraseña llegarán automáticamente</li>
                <li>Cada usuario recibirá su código en su propio email</li>
                <li>Funciona para 100, 1000, 10000+ usuarios</li>
                <li>Totalmente automático - sin intervención manual</li>
            </ul>
            
            <p style="margin-top: 30px;"><strong>Próximo paso:</strong></p>
            <ol>
                <li>Reinicia el servidor Django (Ctrl+C y luego: python manage.py runserver)</li>
                <li>Prueba la función "Olvidé mi contraseña"</li>
                <li>El código llegará al email en 5-30 segundos</li>
            </ol>
            
            <hr style="border: none; border-top: 1px solid #dee2e6; margin: 30px 0;">
            
            <p><strong>Saludos,</strong><br>Equipo DIGIT SOFT</p>
        </div>
        <div class="footer">
            <p>© 2026 DIGIT SOFT - Todos los derechos reservados</p>
        </div>
    </div>
</body>
</html>
        """

        part1 = MIMEText(text, 'plain', 'utf-8')
        part2 = MIMEText(html, 'html', 'utf-8')

        msg.attach(part1)
        msg.attach(part2)

        # Enviar
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        server.quit()

        print(f"{GREEN}✅ Email de prueba enviado correctamente{RESET}")
        print(f"{BLUE}📧 Revisa tu bandeja de entrada: {email}{RESET}")
        return True

    except Exception as e:
        print(f"{RED}❌ Error enviando email: {e}{RESET}")
        return False

def save_env_file(email, password):
    """Guarda la configuración en el archivo .env"""
    try:
        env_content = f"""# CONFIGURACIÓN DE EMAIL - DIGIT SOFT
# Configurado automáticamente

# Backend de email (SMTP real)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

# Configuración SMTP de Gmail
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Credenciales de Gmail
EMAIL_HOST_USER={email}
EMAIL_HOST_PASSWORD={password}

# Email remitente
DEFAULT_FROM_EMAIL=DIGIT SOFT <{email}>

# Email del administrador
ADMIN_EMAIL={email}

# URL del sitio
SITE_URL=http://localhost:8000

# Otras configuraciones
DEBUG=True
SECRET_KEY=django-insecure-digt-soft-2024-cambiar-en-produccion
"""

        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_content)

        print(f"{GREEN}✅ Archivo .env actualizado{RESET}")
        return True

    except Exception as e:
        print(f"{RED}❌ Error guardando .env: {e}{RESET}")
        return False

def main():
    print_header()

    # Verificar configuración actual
    current_email, current_password = check_current_config()

    if current_email and current_password and current_password != 'AQUI_TU_CONTRASEÑA_DE_APLICACION':
        print(f"{BLUE}📧 Email configurado: {current_email}{RESET}")
        print(f"{YELLOW}🔑 Ya existe una contraseña configurada{RESET}")
        print()

        # Probar la configuración actual
        if test_smtp_connection(current_email, current_password):
            print()
            print(f"{GREEN}{'=' * 80}{RESET}")
            print(f"{BOLD}{GREEN}✅ ¡TU CONFIGURACIÓN YA ESTÁ LISTA!{RESET}")
            print(f"{GREEN}{'=' * 80}{RESET}")
            print()
            print(f"{BLUE}El sistema está configurado correctamente para enviar emails.{RESET}")
            print()

            # Preguntar si quiere enviar email de prueba
            respuesta = input(f"{YELLOW}¿Quieres enviar un email de prueba? (S/n): {RESET}").strip().lower()

            if respuesta != 'n':
                print()
                send_test_email(current_email, current_password)

            print()
            print(f"{BOLD}📝 PRÓXIMO PASO:{RESET}")
            print(f"{BLUE}{'─' * 80}{RESET}")
            print(f"{YELLOW}1. Reinicia el servidor Django:{RESET}")
            print(f"   - Presiona Ctrl+C en la ventana donde corre el servidor")
            print(f"   - Ejecuta: python manage.py runserver")
            print()
            print(f"{YELLOW}2. Prueba la función 'Olvidé mi contraseña':{RESET}")
            print(f"   - Ve a: http://127.0.0.1:8000/usuarios/login/")
            print(f"   - Clic en 'Olvidé mi contraseña'")
            print(f"   - Ingresa un email registrado")
            print(f"   - El código llegará al email en 5-30 segundos")
            print()
            print(f"{GREEN}✅ Funciona automáticamente para TODOS los usuarios registrados{RESET}")
            print(f"{BLUE}{'─' * 80}{RESET}")
            print()

            return
        else:
            print()
            print(f"{YELLOW}La contraseña guardada no funciona. Necesitas configurar una nueva.{RESET}")
            print()

    # No hay configuración o no funciona - pedir nueva contraseña
    print(f"{BOLD}🔧 CONFIGURACIÓN NECESARIA{RESET}")
    print(f"{BLUE}{'─' * 80}{RESET}")
    print()
    print(f"{YELLOW}Para enviar emails necesitas una 'Contraseña de Aplicación' de Google.{RESET}")
    print()
    print(f"{BOLD}Pasos:{RESET}")
    print(f"1. Ve a: https://myaccount.google.com/apppasswords")
    print(f"2. Selecciona 'Correo' y genera la contraseña")
    print(f"3. Copia la contraseña de 16 caracteres")
    print(f"4. Pégala aquí")
    print()

    respuesta = input(f"{YELLOW}¿Abrir la página de Google ahora? (S/n): {RESET}").strip().lower()

    if respuesta != 'n':
        print(f"{BLUE}⏳ Abriendo navegador...{RESET}")
        webbrowser.open('https://myaccount.google.com/apppasswords')
        print()

    # Pedir email
    if current_email and current_email != 'davidcristancho160@gmail.com':
        email = input(f"Email de Gmail [{current_email}]: ").strip() or current_email
    else:
        email = input(f"{YELLOW}Email de Gmail (ej: davidcristancho160@gmail.com): {RESET}").strip()

    if not email:
        print(f"{RED}❌ Email no puede estar vacío{RESET}")
        return

    # Pedir contraseña
    password = input(f"{YELLOW}Contraseña de aplicación (16 caracteres): {RESET}").strip()

    if not password:
        print(f"{RED}❌ Contraseña no puede estar vacía{RESET}")
        return

    # Limpiar espacios de la contraseña
    password = password.replace(' ', '')

    print()

    # Probar conexión
    if test_smtp_connection(email, password):
        print()

        # Guardar configuración
        if save_env_file(email, password):
            print()

            # Enviar email de prueba
            send_test_email(email, password)

            print()
            print(f"{GREEN}{'=' * 80}{RESET}")
            print(f"{BOLD}{GREEN}🎉 ¡CONFIGURACIÓN COMPLETADA EXITOSAMENTE!{RESET}")
            print(f"{GREEN}{'=' * 80}{RESET}")
            print()
            print(f"{BOLD}📝 PRÓXIMO PASO (IMPORTANTE):{RESET}")
            print(f"{BLUE}{'─' * 80}{RESET}")
            print(f"{YELLOW}1. REINICIA EL SERVIDOR DJANGO:{RESET}")
            print(f"   - Ve a la ventana donde corre el servidor")
            print(f"   - Presiona Ctrl+C para detenerlo")
            print(f"   - Ejecuta: python manage.py runserver")
            print()
            print(f"{YELLOW}2. PRUEBA LA FUNCIÓN:{RESET}")
            print(f"   - Ve a: http://127.0.0.1:8000/usuarios/login/")
            print(f"   - Clic en 'Olvidé mi contraseña'")
            print(f"   - Ingresa un email registrado")
            print(f"   - El código llegará al email en 5-30 segundos")
            print()
            print(f"{GREEN}✅ Funciona para 100, 1000, 10000+ usuarios automáticamente{RESET}")
            print(f"{BLUE}{'─' * 80}{RESET}")
            print()
    else:
        print()
        print(f"{RED}❌ No se pudo completar la configuración{RESET}")
        print()
        print(f"{YELLOW}💡 Posibles soluciones:{RESET}")
        print(f"1. Verifica que la verificación en dos pasos esté activa")
        print(f"2. Genera una nueva contraseña de aplicación")
        print(f"3. Asegúrate de copiar los 16 caracteres correctamente")
        print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f"{YELLOW}Configuración cancelada{RESET}")
    except Exception as e:
        print(f"{RED}❌ Error inesperado: {e}{RESET}")
        import traceback
        traceback.print_exc()

    input("\nPresiona Enter para salir...")

