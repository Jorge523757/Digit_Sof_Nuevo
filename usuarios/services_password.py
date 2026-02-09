"""
Servicio de Recuperación de Contraseña con Email
"""

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth.models import User
from .models_tokens import TokenRecuperacion


class ServicioRecuperacionPassword:
    """Gestiona el proceso completo de recuperación de contraseña"""

    @staticmethod
    def solicitar_recuperacion(email, ip=None):
        """
        Inicia el proceso de recuperación enviando código por email
        Retorna: (exito, mensaje, token)
        """
        try:
            # Buscar usuario por email
            usuario = User.objects.filter(email=email).first()

            if not usuario:
                # Por seguridad, no revelar si el email existe o no
                return (False, 'Si el email existe, recibirás un código de recuperación.', None)

            # Crear token de recuperación (30 minutos)
            token = TokenRecuperacion.crear_token(usuario, email, ip)

            # Enviar email con el código
            exito_email = ServicioRecuperacionPassword._enviar_email_codigo(usuario, token)

            if exito_email:
                return (True, f'Código de recuperación enviado a {email}. Válido por 30 minutos.', token)
            else:
                return (False, 'Error al enviar el email. Intenta nuevamente.', None)

        except Exception as e:
            print(f"Error en solicitar_recuperacion: {e}")
            return (False, 'Error al procesar la solicitud. Intenta nuevamente.', None)

    @staticmethod
    def _enviar_email_codigo(usuario, token):
        """Envía el código de recuperación por email"""
        try:
            contexto = {
                'usuario': usuario,
                'codigo': token.codigo,
                'vigencia_minutos': 30,
                'fecha_expiracion': token.fecha_expiracion,
            }

            html_content = render_to_string('emails/codigo_recuperacion.html', contexto)
            text_content = f"""
Hola {usuario.username},

Has solicitado recuperar tu contraseña en DIGIT SOFT.

Tu código de verificación es: {token.codigo}

Este código es válido por 30 minutos.

Si no solicitaste este cambio, ignora este mensaje.

---
DIGIT SOFT - Sistema de Gestión
            """.strip()

            email = EmailMultiAlternatives(
                subject='Código de Recuperación de Contraseña - DIGIT SOFT',
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[token.email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            print(f"✅ Email enviado a {token.email} con código: {token.codigo}")
            return True

        except Exception as e:
            print(f"❌ Error enviando email: {e}")
            return False

    @staticmethod
    def verificar_codigo(email, codigo):
        """
        Verifica que el código sea válido
        Retorna: (valido, mensaje, token)
        """
        try:
            # Buscar token válido
            token = TokenRecuperacion.objects.filter(
                email=email,
                codigo=codigo,
                usado=False
            ).first()

            if not token:
                return (False, 'Código incorrecto o ya usado.', None)

            if token.esta_expirado:
                return (False, 'El código ha expirado. Solicita uno nuevo.', None)

            return (True, 'Código verificado correctamente.', token)

        except Exception as e:
            print(f"Error en verificar_codigo: {e}")
            return (False, 'Error al verificar el código.', None)

    @staticmethod
    def cambiar_password(token, nueva_password):
        """
        Cambia la contraseña del usuario usando un token válido
        Retorna: (exito, mensaje)
        """
        try:
            if not token.es_valido:
                return (False, 'El código ya no es válido.')

            # Cambiar contraseña
            usuario = token.usuario
            usuario.set_password(nueva_password)
            usuario.save()

            # Marcar token como usado
            token.marcar_usado()

            # Invalidar todos los demás tokens del usuario
            TokenRecuperacion.objects.filter(
                usuario=usuario,
                usado=False
            ).update(usado=True)

            print(f"✅ Contraseña cambiada para {usuario.username}")
            return (True, 'Contraseña cambiada exitosamente. Ya puedes iniciar sesión.')

        except Exception as e:
            print(f"Error en cambiar_password: {e}")
            return (False, 'Error al cambiar la contraseña.')

    @staticmethod
    def validar_password(password):
        """
        Valida que la contraseña cumpla con los requisitos
        Retorna: (valida, mensaje)
        """
        if len(password) < 8:
            return (False, 'La contraseña debe tener al menos 8 caracteres.')

        if password.isdigit():
            return (False, 'La contraseña no puede ser solo números.')

        if password.isalpha():
            return (False, 'La contraseña debe incluir números.')

        if password.lower() == password:
            return (False, 'La contraseña debe incluir al menos una mayúscula.')

        # Contraseñas comunes bloqueadas
        comunes = ['12345678', 'password', 'Password1', 'Admin123', 'Qwerty123']
        if password in comunes:
            return (False, 'Contraseña muy común. Elige una más segura.')

        return (True, 'Contraseña válida.')

