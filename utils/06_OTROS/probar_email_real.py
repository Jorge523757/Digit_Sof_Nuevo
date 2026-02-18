"""
Script para probar el envío real de emails con la configuración actual
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import datetime

def probar_email():
    """Prueba el envío de un email real"""

    print("\n" + "=" * 80)
    print("📧 PRUEBA DE ENVÍO DE EMAIL REAL")
    print("=" * 80)
    print(f"Backend: {settings.EMAIL_BACKEND}")
    print(f"Host: {settings.EMAIL_HOST}")
    print(f"Puerto: {settings.EMAIL_PORT}")
    print(f"TLS: {settings.EMAIL_USE_TLS}")
    print(f"Usuario: {settings.EMAIL_HOST_USER}")
    print(f"Contraseña configurada: {'✅ Sí' if settings.EMAIL_HOST_PASSWORD else '❌ No'}")
    print("=" * 80)

    try:
        # Crear email de prueba
        subject = "✅ Prueba de Configuración de Email - DIGIT SOFT"

        text_content = f"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║              ✅ PRUEBA DE EMAIL - DIGIT SOFT                     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

¡Hola!

Este es un email de prueba enviado el {datetime.now().strftime('%d/%m/%Y a las %H:%M:%S')}

Si recibes este mensaje, significa que la configuración de email está funcionando correctamente.

✅ Backend: {settings.EMAIL_BACKEND}
✅ Servidor: {settings.EMAIL_HOST}:{settings.EMAIL_PORT}
✅ Seguridad: TLS activado

---
DIGIT SOFT - Sistema de Gestión
© 2026 - Todos los derechos reservados
"""

        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; }}
        .container {{ max-width: 600px; margin: 20px auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #28a745 0%, #20c997 100%); color: white; padding: 40px 20px; text-align: center; }}
        .content {{ padding: 40px 30px; }}
        .info-box {{ background: #e7f5ee; border-left: 4px solid #28a745; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        .footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #6c757d; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin: 0;">✅ Email de Prueba</h1>
            <p style="margin: 10px 0 0 0;">DIGIT SOFT</p>
        </div>
        <div class="content">
            <h2>¡Configuración Exitosa!</h2>
            <p>Este es un email de prueba enviado el <strong>{datetime.now().strftime('%d/%m/%Y a las %H:%M:%S')}</strong></p>
            
            <div class="info-box">
                <strong>✅ Si recibes este mensaje:</strong>
                <ul>
                    <li>La configuración de email está funcionando</li>
                    <li>El servidor SMTP responde correctamente</li>
                    <li>Las credenciales son válidas</li>
                    <li>Los emails de recuperación de contraseña llegarán sin problemas</li>
                </ul>
            </div>
            
            <p><strong>Detalles técnicos:</strong></p>
            <ul>
                <li>Backend: {settings.EMAIL_BACKEND}</li>
                <li>Servidor: {settings.EMAIL_HOST}:{settings.EMAIL_PORT}</li>
                <li>Seguridad: TLS activado</li>
            </ul>
            
            <hr style="border: none; border-top: 1px solid #dee2e6; margin: 30px 0;">
            
            <p style="margin-top: 20px;"><strong>Saludos,</strong><br>Equipo DIGIT SOFT</p>
        </div>
        <div class="footer">
            <p>© 2026 DIGIT SOFT - Todos los derechos reservados</p>
            <p>Este es un correo de prueba automático.</p>
        </div>
    </div>
</body>
</html>
"""

        # Crear y enviar email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.EMAIL_HOST_USER]  # Enviar al mismo email configurado
        )
        email.attach_alternative(html_content, "text/html")

        print("\n📤 Enviando email...")
        email.send(fail_silently=False)

        print("\n" + "=" * 80)
        print("✅ EMAIL ENVIADO EXITOSAMENTE")
        print("=" * 80)
        print(f"📧 Para: {settings.EMAIL_HOST_USER}")
        print(f"📬 Revisa tu bandeja de entrada y SPAM")
        print(f"⏰ Enviado a las: {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 80)
        print("\n✅ La configuración de email está funcionando correctamente.")
        print("   Los códigos de recuperación ahora llegarán al email del usuario.\n")

        return True

    except Exception as e:
        print("\n" + "=" * 80)
        print("❌ ERROR AL ENVIAR EMAIL")
        print("=" * 80)
        print(f"Error: {e}")
        print("\n💡 POSIBLES SOLUCIONES:")
        print("   1. Verifica la contraseña de aplicación de Gmail")
        print("   2. Revisa que el archivo .env tenga las credenciales correctas")
        print("   3. Asegúrate de tener conexión a internet")
        print("   4. Verifica que la verificación en 2 pasos esté activa en Gmail")
        print("\n📖 Guía: https://myaccount.google.com/apppasswords")
        print("=" * 80)

        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    probar_email()

