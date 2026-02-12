import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from usuarios.models_tokens import TokenRecuperacion

# Buscar el código más reciente
token = TokenRecuperacion.objects.filter(
    email__iexact='davidcristancho160@gmail.com',
    usado=False
).order_by('-fecha_creacion').first()

if token:
    print("\n" + "="*50)
    print("🔐 TU CÓDIGO DE RECUPERACIÓN")
    print("="*50)
    print(f"\n   CÓDIGO: {token.codigo}\n")
    print(f"   Expira: {token.fecha_expiracion}")
    print(f"   Email: {token.email}")
    print("\n" + "="*50)
    print(f"\n✅ COPIA ESTE CÓDIGO: {token.codigo}\n")
else:
    print("\n❌ No se encontró código activo")

