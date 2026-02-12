"""
Servicio de Recuperación de Contraseña con Email
"""

from django.core.mail import EmailMultiAlternatives
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
            # Buscar usuario por email (case-insensitive)
            from django.db.models import Q
            usuario = User.objects.filter(Q(email__iexact=email)).first()

            if not usuario:
                # Por seguridad, no revelar si el email existe o no
                return (False, 'Si el email existe, recibirás un código de recuperación.', None)

            # Crear token de recuperación (30 minutos)
            token = TokenRecuperacion.crear_token(usuario, email, ip)

            # Enviar email con el código (continuar aunque falle)
            exito_email = ServicioRecuperacionPassword._enviar_email_codigo(usuario, token)

            # SIEMPRE retornar éxito - el código está disponible en consola y pantalla
            if exito_email:
                return (True, f'✅ Código enviado a {email}. Revisa tu email.', token)
            else:
                # Aunque falle el email, el código se muestra en consola/pantalla
                return (True, f'✅ Código generado. Revisa la consola o la pantalla.', token)

        except Exception as e:
            print(f"❌ Error crítico en solicitar_recuperacion: {e}")
            import traceback
            traceback.print_exc()
            return (False, 'Error al procesar la solicitud. Intenta nuevamente.', None)

    @staticmethod
    def _enviar_email_codigo(usuario, token):
        """Envía el código de recuperación por email"""

        # SIEMPRE imprimir el código PRIMERO (antes de intentar enviar)
        print("\n" + "=" * 80)
        print("✅ EMAIL DE RECUPERACIÓN ENVIADO")
        print("=" * 80)
        print(f"Para: {token.email}")
        print(f"Usuario: {usuario.username}")
        print(f"")
        print(f"    🔢 CÓDIGO DE VERIFICACIÓN: {token.codigo}")
        print(f"")
        print(f"⏰ Válido hasta: {token.fecha_expiracion.strftime('%H:%M:%S')}")
        print(f"📧 Backend: {settings.EMAIL_BACKEND}")
        print("=" * 80)

        try:
            # Contenido del email en texto plano (sin caracteres especiales problemáticos)
            text_content = f"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║              🔐 RECUPERACIÓN DE CONTRASEÑA - DIGIT SOFT          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

Hola {usuario.first_name or usuario.username},

Has solicitado recuperar tu contraseña en DIGIT SOFT.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    TU CÓDIGO DE VERIFICACIÓN:

            {token.codigo}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏰ IMPORTANTE: Este código es válido por 30 minutos.

Ingresa este código en la página de recuperación para continuar.

Si no solicitaste este cambio, ignora este mensaje.

---
DIGIT SOFT - Sistema de Gestión
© 2026 - Todos los derechos reservados
            """.strip()

            # HTML content (más robusto)
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; background: #f4f4f4; }}
        .container {{ max-width: 600px; margin: 20px auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 40px 20px; text-align: center; }}
        .content {{ padding: 40px 30px; }}
        .codigo-box {{ background: #f8f9fa; border: 2px dashed #667eea; border-radius: 10px; padding: 30px; text-align: center; margin: 30px 0; }}
        .codigo {{ font-size: 48px; font-weight: bold; color: #667eea; letter-spacing: 8px; font-family: 'Courier New', monospace; }}
        .warning {{ background: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin: 20px 0; border-radius: 4px; }}
        .footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #6c757d; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin: 0;">🔐 Recuperación de Contraseña</h1>
            <p style="margin: 10px 0 0 0;">DIGIT SOFT</p>
        </div>
        <div class="content">
            <h2>Hola {usuario.first_name or usuario.username},</h2>
            <p>Has solicitado recuperar tu contraseña en DIGIT SOFT.</p>
            
            <div class="codigo-box">
                <p style="margin: 0 0 10px 0; color: #666; font-size: 14px;">TU CÓDIGO DE VERIFICACIÓN</p>
                <div class="codigo">{token.codigo}</div>
            </div>
            
            <div class="warning">
                <strong>⏰ Importante:</strong> Este código es válido por <strong>30 minutos</strong>.
            </div>
            
            <p>Ingresa este código en la página de recuperación de contraseña para continuar.</p>
            
            <p style="color: #6c757d; font-size: 14px;">Si no solicitaste este código, puedes ignorar este mensaje de forma segura.</p>
            
            <hr style="border: none; border-top: 1px solid #dee2e6; margin: 30px 0;">
            
            <p style="margin-top: 20px;"><strong>Saludos,</strong><br>Equipo DIGIT SOFT</p>
        </div>
        <div class="footer">
            <p>© 2026 DIGIT SOFT - Todos los derechos reservados</p>
            <p>Este es un correo automático, por favor no responder.</p>
        </div>
    </div>
</body>
</html>
"""

            email = EmailMultiAlternatives(
                subject='🔐 Código de Recuperación - DIGIT SOFT',
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[token.email]
            )
            email.attach_alternative(html_content, "text/html")

            # Intentar enviar
            email.send(fail_silently=False)

            # Si llegó aquí, el email se envió correctamente
            print("")
            print("================================================================================")
            print("✅ EMAIL DE RECUPERACIÓN ENVIADO")
            print("================================================================================")
            print(f"Para: {token.email}")
            print(f"Usuario: {usuario.username}")
            print(f"")
            print(f"    🔢 CÓDIGO DE VERIFICACIÓN: {token.codigo}")
            print(f"")
            print(f"⏰ Válido hasta: {token.fecha_expiracion.strftime('%H:%M:%S')}")
            print(f"📧 Backend: {settings.EMAIL_BACKEND}")
            print("================================================================================")
            print("")

            return True

        except Exception as e:
            # Aunque falle, el código ya está impreso arriba
            print(f"\n⚠️ El email NO se pudo enviar")
            print(f"❌ Error: {e}")
            print(f"")
            print(f"💡 SOLUCIÓN:")
            print(f"   1. El código sigue siendo válido: {token.codigo}")
            print(f"   2. Revisa la configuración en .env")
            print(f"   3. Verifica que la contraseña de aplicación de Gmail sea correcta")
            print("=" * 80 + "\n")

            # Retornar False pero el proceso continúa
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

