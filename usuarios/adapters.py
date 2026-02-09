"""
Adaptadores personalizados para django-allauth
Gestiona la creación automática de perfiles al registrarse con Google
"""

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from usuarios.models import PerfilUsuario


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Adaptador personalizado para manejar el registro de usuarios
    """

    def get_login_redirect_url(self, request):
        """
        Redirige al dashboard después del login
        """
        path = "/dashboard/"
        return path


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Adaptador personalizado para manejar el registro con redes sociales (Google)
    """

    def pre_social_login(self, request, sociallogin):
        """
        Se ejecuta antes de que el usuario inicie sesión con una cuenta social.
        Si el email ya existe, vincula automáticamente la cuenta de Google.
        """
        # Si el usuario ya está autenticado, no hacer nada
        if sociallogin.is_existing:
            return

        # Obtener el email de la cuenta social
        try:
            email = sociallogin.account.extra_data.get('email', '').lower()
        except:
            return

        if not email:
            return

        # Buscar si existe un usuario con ese email
        from django.contrib.auth.models import User
        try:
            user = User.objects.get(email__iexact=email)

            # Vincular la cuenta de Google al usuario existente
            sociallogin.connect(request, user)

            # Asegurar que el usuario tenga perfil
            if not hasattr(user, 'perfil'):
                PerfilUsuario.objects.create(
                    user=user,
                    tipo_usuario='CLIENTE',
                    activo=True,
                    bloqueado=False
                )
                print(f"✅ Perfil creado para usuario existente: {user.username}")

            print(f"✅ Cuenta de Google vinculada a usuario existente: {user.username}")

        except User.DoesNotExist:
            # El usuario no existe, se creará en save_user
            pass
        except User.MultipleObjectsReturned:
            # Hay múltiples usuarios con ese email (no debería pasar)
            pass

    def populate_user(self, request, sociallogin, data):
        """
        Llena la información del usuario desde los datos de Google
        """
        user = super().populate_user(request, sociallogin, data)

        # Obtener datos adicionales de Google
        if sociallogin.account.provider == 'google':
            extra_data = sociallogin.account.extra_data

            # Asignar nombre y apellido si están disponibles
            if 'given_name' in extra_data:
                user.first_name = extra_data['given_name']

            if 'family_name' in extra_data:
                user.last_name = extra_data['family_name']

            # Si no hay username, crear uno a partir del email
            if not user.username:
                email_parts = user.email.split('@')
                base_username = email_parts[0]
                username = base_username

                # Asegurar que el username sea único
                from django.contrib.auth.models import User
                counter = 1
                while User.objects.filter(username=username).exists():
                    username = f"{base_username}{counter}"
                    counter += 1

                user.username = username

        return user

    def save_user(self, request, sociallogin, form=None):
        """
        Guarda el usuario y crea automáticamente su perfil
        """
        user = super().save_user(request, sociallogin, form)

        # Crear el perfil de usuario automáticamente si no existe
        if not hasattr(user, 'perfil'):
            PerfilUsuario.objects.create(
                user=user,
                tipo_usuario='CLIENTE',  # Por defecto, los usuarios de Google son clientes
                activo=True,
                bloqueado=False
            )
            print(f"✅ Perfil creado automáticamente para: {user.username}")

        return user

    def get_connect_redirect_url(self, request, socialaccount):
        """
        URL de redirección después de conectar una cuenta social
        """
        return "/dashboard/"

    def get_signup_redirect_url(self, request):
        """
        URL de redirección después de completar el registro con cuenta social
        """
        return "/dashboard/"

