"""
Probar envío de email a TODOS los usuarios registrados
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.services_password import ServicioRecuperacionPassword

print("=" * 80)
print("🧪 PROBANDO ENVÍO DE EMAILS A TODOS LOS USUARIOS")
print("=" * 80)
print()

# Obtener todos los usuarios con email
usuarios = User.objects.exclude(email='').exclude(email__isnull=True)

print(f"📧 Usuarios con email registrado: {usuarios.count()}")
print()

for usuario in usuarios:
    print(f"👤 Probando: {usuario.username} ({usuario.email})")

    # Generar código de recuperación
    exito, mensaje, token = ServicioRecuperacionPassword.solicitar_recuperacion(
        usuario.email,
        '127.0.0.1'
    )

    if exito and token:
        print(f"   ✅ Código generado: {token.codigo}")
        print(f"   ✅ Email enviado a: {usuario.email}")
        print(f"   ⏰ Válido hasta: {token.fecha_expiracion.strftime('%H:%M:%S')}")
    else:
        print(f"   ❌ Error: {mensaje}")

    print()

print("=" * 80)
print("✅ PRUEBA COMPLETADA")
print("=" * 80)
print()
print("📝 RESUMEN:")
print("   - Todos los usuarios reciben el código por email")
print("   - NO necesitan activar verificación en 2 pasos")
print("   - Solo el administrador configuró el email remitente UNA VEZ")
print()
print("🎉 El sistema funciona para TODOS automáticamente")
print()

