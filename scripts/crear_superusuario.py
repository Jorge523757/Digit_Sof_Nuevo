import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Crear superusuario
username = 'admin'
email = 'admin@digtsoft.com'
password = 'admin123'

if User.objects.filter(username=username).exists():
    print(f"❌ El usuario '{username}' ya existe.")
else:
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"\n{'='*60}")
    print(f"✅ SUPERUSUARIO CREADO EXITOSAMENTE")
    print(f"{'='*60}")
    print(f"  Usuario:    {username}")
    print(f"  Contraseña: {password}")
    print(f"  Email:      {email}")
    print(f"{'='*60}")
    print(f"\n💡 Accede al sistema en:")
    print(f"   http://127.0.0.1:8000/admin/")
    print(f"\n🔐 Credenciales de acceso:")
    print(f"   Usuario: {username}")
    print(f"   Contraseña: {password}")
    print(f"\n{'='*60}\n")

