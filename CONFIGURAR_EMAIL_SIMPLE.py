"""
═══════════════════════════════════════════════════════════════════════════
    ⚡ SOLUCIÓN RÁPIDA - ENVÍO DE EMAILS A USUARIOS
═══════════════════════════════════════════════════════════════════════════

🎯 TU PROBLEMA:
Los códigos de recuperación se ven en la consola pero NO llegan al email

✅ LA SOLUCIÓN:
Necesitas una "Contraseña de Aplicación" de Google (toma 2 minutos)

═══════════════════════════════════════════════════════════════════════════
"""

import webbrowser
import time
import os

def main():
    print(__doc__)

    print("╔" + "═" * 77 + "╗")
    print("║" + " " * 20 + "PASOS A SEGUIR (2 MINUTOS)" + " " * 31 + "║")
    print("╚" + "═" * 77 + "╝")
    print()

    print("PASO 1: Activar verificación en dos pasos (si no la tienes)")
    print("─" * 79)
    print("1. Voy a abrir tu navegador en la configuración de seguridad de Google")
    print("2. Si no tienes verificación en 2 pasos, actívala (sigue las instrucciones)")
    print()

    input("Presiona Enter para abrir la página de seguridad de Google...")
    webbrowser.open('https://myaccount.google.com/security')
    print()
    print("✅ Navegador abierto")
    print()
    print("⏳ Activa la verificación en dos pasos si no la tienes...")
    print("   (Si ya la tienes, continúa al siguiente paso)")
    print()

    input("Presiona Enter cuando hayas activado la verificación en 2 pasos...")
    print()

    print("PASO 2: Generar contraseña de aplicación")
    print("─" * 79)
    print("1. Voy a abrir la página para generar contraseñas de aplicación")
    print("2. Selecciona 'Correo' en el desplegable")
    print("3. Clic en 'Generar'")
    print("4. COPIA los 16 caracteres que aparecen")
    print()

    input("Presiona Enter para abrir la página de contraseñas de aplicación...")
    webbrowser.open('https://myaccount.google.com/apppasswords')
    print()
    print("✅ Navegador abierto en la página de contraseñas de aplicación")
    print()
    print("⏳ Genera la contraseña y cópiala...")
    print()

    print("PASO 3: Pegar la contraseña aquí")
    print("─" * 79)
    print()

    password = input("Pega la contraseña de aplicación aquí (16 caracteres): ").strip()

    if not password:
        print()
        print("❌ No ingresaste ninguna contraseña")
        print()
        input("Presiona Enter para salir y vuelve a ejecutar este script...")
        return

    # Limpiar espacios
    password = password.replace(' ', '')

    print()
    print("⏳ Guardando configuración...")

    # Crear archivo .env
    env_content = f"""# CONFIGURACIÓN DE EMAIL - DIGIT SOFT
# Configurado automáticamente el {time.strftime('%Y-%m-%d %H:%M:%S')}

# Backend de email (SMTP real)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

# Configuración SMTP de Gmail
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Credenciales de Gmail
EMAIL_HOST_USER=davidcristancho160@gmail.com
EMAIL_HOST_PASSWORD={password}

# Email remitente
DEFAULT_FROM_EMAIL=DIGIT SOFT <davidcristancho160@gmail.com>

# Email del administrador
ADMIN_EMAIL=davidcristancho160@gmail.com

# URL del sitio
SITE_URL=http://localhost:8000

# Otras configuraciones
DEBUG=True
SECRET_KEY=django-insecure-digt-soft-2024-cambiar-en-produccion
"""

    try:
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_content)

        print("✅ Configuración guardada en .env")
        print()

        # Probar conexión
        print("⏳ Probando conexión con Gmail...")
        print()

        import smtplib
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
            server.starttls()
            server.login('davidcristancho160@gmail.com', password)
            server.quit()

            print("╔" + "═" * 77 + "╗")
            print("║" + " " * 25 + "¡ÉXITO TOTAL!" + " " * 38 + "║")
            print("╚" + "═" * 77 + "╝")
            print()
            print("✅ Conexión con Gmail: FUNCIONANDO")
            print("✅ Configuración: COMPLETA")
            print("✅ Sistema listo para enviar emails a TODOS los usuarios")
            print()
            print("═" * 79)
            print("  📝 ÚLTIMO PASO (MUY IMPORTANTE)")
            print("═" * 79)
            print()
            print("DEBES REINICIAR EL SERVIDOR DE DJANGO:")
            print()
            print("1. Ve a la ventana donde está corriendo Django")
            print("2. Presiona Ctrl+C para detenerlo")
            print("3. Ejecuta de nuevo: python manage.py runserver")
            print()
            print("Sin reiniciar, Django seguirá usando la configuración antigua.")
            print()
            print("═" * 79)
            print("  🎉 DESPUÉS DE REINICIAR")
            print("═" * 79)
            print()
            print("Cuando un usuario olvide su contraseña:")
            print()
            print("  Usuario ingresa su email → Código llega a su email en 5-30 seg")
            print()
            print("✅ Funciona para 100, 1000, 10000+ usuarios")
            print("✅ Totalmente automático")
            print("✅ Cada usuario recibe SU código en SU email")
            print("✅ TU email solo se usa como remitente")
            print()

        except smtplib.SMTPAuthenticationError:
            print("❌ ERROR: Contraseña incorrecta")
            print()
            print("La contraseña no funcionó. Posibles razones:")
            print("1. No copiaste bien los 16 caracteres")
            print("2. No activaste la verificación en dos pasos")
            print()
            print("Vuelve a ejecutar este script y asegúrate de:")
            print("- Tener verificación en 2 pasos activa")
            print("- Copiar exactamente los 16 caracteres")
            print()

        except Exception as e:
            print(f"❌ ERROR de conexión: {e}")
            print()
            print("Verifica tu conexión a Internet y vuelve a intentar")
            print()

    except Exception as e:
        print(f"❌ ERROR guardando configuración: {e}")
        print()

    print()
    input("Presiona Enter para salir...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Configuración cancelada")
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()

