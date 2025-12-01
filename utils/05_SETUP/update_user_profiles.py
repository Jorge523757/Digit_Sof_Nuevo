"""
Script para crear perfiles de usuario para usuarios existentes
"""
import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digitsoft_project.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import UserProfile

def create_profiles_for_existing_users():
    """Crear perfiles para usuarios existentes que no tengan"""
    users_without_profile = []
    
    for user in User.objects.all():
        try:
            # Intentar acceder al perfil
            profile = user.profile
            print(f"✓ Usuario {user.username} ya tiene perfil: {profile.role}")
        except UserProfile.DoesNotExist:
            # El usuario no tiene perfil, crear uno
            users_without_profile.append(user)
    
    if users_without_profile:
        print(f"\nEncontrados {len(users_without_profile)} usuarios sin perfil:")
        
        for user in users_without_profile:
            # Determinar el rol basado en las características del usuario
            if user.is_superuser:
                role = 'administrador'
                print(f"  - {user.username} (superusuario) -> Administrador")
            elif user.is_staff:
                role = 'administrador'
                print(f"  - {user.username} (staff) -> Administrador")
            else:
                role = 'cliente'
                print(f"  - {user.username} -> Cliente")
            
            # Crear el perfil
            profile = UserProfile.objects.create(
                user=user,
                role=role,
                documento=f"DOC_{user.id}",  # Documento temporal
                telefono="0000000000",        # Teléfono temporal
                direccion="Dirección no especificada",  # Dirección temporal
                activo=True
            )
            print(f"    ✓ Perfil creado para {user.username}")
    else:
        print("Todos los usuarios ya tienen perfiles asignados.")

def show_user_profiles():
    """Mostrar todos los perfiles de usuario"""
    print("\n" + "="*50)
    print("PERFILES DE USUARIO ACTUALES")
    print("="*50)
    
    for profile in UserProfile.objects.all():
        user = profile.user
        print(f"""
Usuario: {user.username}
Nombre: {user.get_full_name() or 'No especificado'}
Email: {user.email or 'No especificado'}
Rol: {profile.get_role_display()}
Documento: {profile.documento}
Teléfono: {profile.telefono}
Dirección: {profile.direccion}
Es superusuario: {'Sí' if user.is_superuser else 'No'}
Es staff: {'Sí' if user.is_staff else 'No'}
Activo: {'Sí' if profile.activo else 'No'}
Fecha creación: {profile.fecha_creacion}
{'-'*30}""")

if __name__ == '__main__':
    print("🔧 ACTUALIZANDO PERFILES DE USUARIO")
    print("="*40)
    
    create_profiles_for_existing_users()
    show_user_profiles()
    
    print("\n✅ ¡Actualización completada!")
    print("\nAhora todos los usuarios tienen perfiles con roles asignados.")
    print("Los usuarios pueden completar su información desde su perfil.")