import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Datos del superusuario
username = "admin"
email = "admin@digitsoft.com"
password = "admin123"  # Cambiar esta contraseña después

# Verificar si ya existe
if User.objects.filter(username=username).exists():
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(f"✅ Superusuario '{username}' actualizado correctamente")
else:
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"✅ Superusuario '{username}' creado correctamente")

print(f"\n📧 Email: {email}")
print(f"🔑 Contraseña: {password}")
print(f"\n⚠️  IMPORTANTE: Cambia la contraseña después del primer inicio de sesión")
print(f"\n🌐 Accede al panel admin en: http://127.0.0.1:8000/admin/")

