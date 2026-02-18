"""
Script para probar recuperación de contraseña con diferentes variaciones de email
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.services_password import ServicioRecuperacionPassword

print("=" * 80)
print("🧪 PRUEBA DE RECUPERACIÓN CON DIFERENTES EMAILS")
print("=" * 80)
print()

# Mostrar usuarios existentes
print("👥 USUARIOS REGISTRADOS:")
print("-" * 80)
usuarios = User.objects.all()
for u in usuarios:
    print(f"   Usuario: {u.username:20} | Email: {u.email}")
print("-" * 80)
print()

# Probar con diferentes variaciones de email
emails_prueba = [
    'jorgedavidcristanchoguarin@gmail.com',  # Minúsculas
    'Jorgedavidcristanchoguarin@gmail.com',  # Primera mayúscula
    'JORGEDAVIDCRISTANCHOGUARIN@GMAIL.COM',  # Todo mayúsculas
    'JorgedavidCristanchoguarin@Gmail.com',  # Mezcla
    'davidcristancho160@gmail.com',          # Otro usuario
]

print("🔍 PROBANDO RECUPERACIÓN CON DIFERENTES VARIACIONES:")
print("=" * 80)

for email in emails_prueba:
    print(f"\n📧 Probando con: {email}")
    print("-" * 40)

    # Simular la búsqueda case-insensitive
    from django.db.models import Q
    usuario = User.objects.filter(Q(email__iexact=email)).first()

    if usuario:
        print(f"✅ Usuario encontrado: {usuario.username}")
        print(f"   Email en BD: {usuario.email}")

        # Probar generación de código
        exito, mensaje, token = ServicioRecuperacionPassword.solicitar_recuperacion(
            usuario.email,
            '127.0.0.1'
        )

        if exito and token:
            print(f"✅ Código generado: {token.codigo}")
        else:
            print(f"❌ Error: {mensaje}")
    else:
        print(f"❌ No se encontró usuario con ese email")

print("\n" + "=" * 80)
print("✅ PRUEBA COMPLETADA")
print("=" * 80)
print()
print("📝 RESUMEN:")
print("   - La búsqueda debe ser case-insensitive (sin importar mayúsculas)")
print("   - Si el email existe (en cualquier variación), debe funcionar")
print("   - El código debe generarse correctamente")
print()

