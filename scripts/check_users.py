import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

users = User.objects.all()
print(f"\n{'='*50}")
print(f"USUARIOS EN LA BASE DE DATOS")
print(f"{'='*50}")
print(f"Total de usuarios: {users.count()}\n")

if users.exists():
    for user in users:
        print(f"Usuario: {user.username}")
        print(f"  Email: {user.email}")
        print(f"  Es superusuario: {'SÍ' if user.is_superuser else 'NO'}")
        print(f"  Es staff: {'SÍ' if user.is_staff else 'NO'}")
        print(f"  Activo: {'SÍ' if user.is_active else 'NO'}")
        print(f"  Fecha creación: {user.date_joined}")
        print()
else:
    print("❌ No hay usuarios creados en el sistema.")
    print("\n💡 Para crear un superusuario ejecuta:")
    print("   python manage.py createsuperuser")

print(f"{'='*50}\n")

