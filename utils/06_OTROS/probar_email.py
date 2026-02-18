"""
Script de Prueba de Email Profesional
Verifica que el envío de emails funcione correctamente
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

print("=" * 80)
print("🧪 PROBANDO CONFIGURACIÓN DE EMAIL")
print("=" * 80)
print()

# Verificar configuración
print("📧 Configuración actual:")
print(f"   Backend: {settings.EMAIL_BACKEND}")
print(f"   Host: {settings.EMAIL_HOST}")
print(f"   Puerto: {settings.EMAIL_PORT}")
print(f"   Usuario: {settings.EMAIL_HOST_USER}")
print(f"   Password configurado: {'✅ SÍ' if settings.EMAIL_HOST_PASSWORD and settings.EMAIL_HOST_PASSWORD != 'AQUI_TU_CONTRASEÑA_DE_APLICACION' else '❌ NO'}")
print()

print("=" * 80)
print("📨 ENVIANDO EMAIL DE PRUEBA...")
print("=" * 80)
print()

try:
    resultado = send_mail(
        subject='✅ Prueba - Sistema DIGIT SOFT Configurado',
        message='¡Felicidades! Tu sistema DIGIT SOFT está correctamente configurado para enviar emails.\n\nLos códigos de recuperación ahora llegarán automáticamente a los usuarios.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['davidcristancho160@gmail.com'],
        fail_silently=False,
    )

    if resultado:
        print("✅ ¡EMAIL ENVIADO EXITOSAMENTE!")
        print()
        print("🎉 El sistema está configurado correctamente")
        print()
        print("📬 Revisa tu bandeja de entrada:")
        print("   Email: davidcristancho160@gmail.com")
        print()
        print("⏱️  El email debería llegar en unos segundos")
        print("   Si no lo ves, revisa la carpeta de SPAM")
        print()
    else:
        print("❌ Error: No se pudo enviar el email")

except Exception as e:
    print("❌ ERROR AL ENVIAR EMAIL:")
    print(f"   {e}")
    print()
    print("📝 Posibles causas:")
    print("   - La contraseña de aplicación es incorrecta")
    print("   - La verificación en 2 pasos no está activada")
    print("   - Problema de conexión a internet")

print()
print("=" * 80)

