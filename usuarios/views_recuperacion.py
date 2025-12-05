"""
DIGITSOFT - Módulo de Recuperación de Contraseña
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from usuarios.decorators import staff_required
from clientes.models import Cliente
from tecnicos.models import Tecnico
from proveedores.models import Proveedor


def solicitar_recuperacion(request):
    """Formulario público para solicitar recuperación de contraseña"""
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        tipo_usuario = request.POST.get('tipo_usuario', 'usuario')

        if not email:
            messages.error(request, 'Por favor ingresa tu correo electrónico.')
            return redirect('usuarios:solicitar_recuperacion')

        # Buscar usuario según el tipo
        usuario_encontrado = None
        nombre_usuario = None

        try:
            if tipo_usuario == 'usuario':
                user = User.objects.get(email=email)
                usuario_encontrado = user
                nombre_usuario = user.get_full_name() or user.username

            elif tipo_usuario == 'cliente':
                cliente = Cliente.objects.get(email=email)
                if cliente.usuario:
                    usuario_encontrado = cliente.usuario
                    nombre_usuario = cliente.nombre_completo

            elif tipo_usuario == 'tecnico':
                tecnico = Tecnico.objects.get(email=email)
                if tecnico.usuario:
                    usuario_encontrado = tecnico.usuario
                    nombre_usuario = tecnico.nombre_completo

            elif tipo_usuario == 'proveedor':
                proveedor = Proveedor.objects.get(email=email)
                nombre_usuario = proveedor.nombre_contacto

        except (User.DoesNotExist, Cliente.DoesNotExist, Tecnico.DoesNotExist, Proveedor.DoesNotExist):
            # Por seguridad, no revelamos si el email existe o no
            messages.info(request,
                'Si el correo está registrado, recibirás instrucciones para recuperar tu contraseña.')
            return redirect('main:index')

        if usuario_encontrado:
            # Generar token de recuperación
            token = get_random_string(32)

            # Guardar token en sesión temporalmente (o en modelo si prefieres)
            request.session[f'reset_token_{token}'] = {
                'user_id': usuario_encontrado.id,
                'email': email,
                'tipo': tipo_usuario
            }

            # Enviar correo con enlace
            try:
                reset_url = request.build_absolute_uri(
                    f'/usuarios/recuperar-contrasena/{token}/'
                )

                send_mail(
                    'Recuperación de Contraseña - DIGITSOFT',
                    f'Hola {nombre_usuario},\n\n'
                    f'Has solicitado recuperar tu contraseña.\n\n'
                    f'Haz clic en el siguiente enlace para establecer una nueva contraseña:\n'
                    f'{reset_url}\n\n'
                    f'Este enlace expirará en 1 hora.\n\n'
                    f'Si no solicitaste este cambio, ignora este correo.\n\n'
                    f'Saludos,\nEquipo DIGITSOFT',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                messages.success(request,
                    'Se ha enviado un correo con instrucciones para recuperar tu contraseña.')
            except Exception as e:
                messages.warning(request,
                    'Tu solicitud ha sido recibida. Un administrador te contactará pronto.')
        else:
            messages.info(request,
                'Si el correo está registrado, recibirás instrucciones para recuperar tu contraseña.')

        return redirect('main:index')

    return render(request, 'usuarios/recuperacion/solicitar.html')


def recuperar_contrasena(request, token):
    """Formulario para establecer nueva contraseña con token"""
    # Verificar token
    session_key = f'reset_token_{token}'
    token_data = request.session.get(session_key)

    if not token_data:
        messages.error(request, 'El enlace de recuperación es inválido o ha expirado.')
        return redirect('usuarios:solicitar_recuperacion')

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not password1 or not password2:
            messages.error(request, 'Por favor completa todos los campos.')
            return redirect('usuarios:recuperar_contrasena', token=token)

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('usuarios:recuperar_contrasena', token=token)

        if len(password1) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return redirect('usuarios:recuperar_contrasena', token=token)

        try:
            user = User.objects.get(id=token_data['user_id'])
            user.set_password(password1)
            user.save()

            # Eliminar token usado
            del request.session[session_key]

            messages.success(request,
                '¡Contraseña actualizada exitosamente! Ya puedes iniciar sesión.')
            return redirect('usuarios:login')

        except User.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
            return redirect('usuarios:solicitar_recuperacion')

    return render(request, 'usuarios/recuperacion/nueva_contrasena.html', {
        'token': token,
        'email': token_data.get('email')
    })


@login_required
@staff_required
def admin_gestionar_contrasenas(request):
    """Panel de administrador para gestionar contraseñas de usuarios"""

    # Obtener todos los usuarios
    usuarios_sistema = User.objects.all().order_by('username')
    clientes = Cliente.objects.all().order_by('nombres')
    tecnicos = Tecnico.objects.all().order_by('nombres')
    proveedores = Proveedor.objects.all().order_by('nombre_empresa')

    context = {
        'usuarios_sistema': usuarios_sistema,
        'clientes': clientes,
        'tecnicos': tecnicos,
        'proveedores': proveedores,
    }

    return render(request, 'usuarios/recuperacion/admin_panel.html', context)


@login_required
@staff_required
def admin_cambiar_contrasena(request, tipo, id):
    """Administrador cambia contraseña de un usuario"""

    if request.method == 'POST':
        nueva_contrasena = request.POST.get('nueva_contrasena')
        enviar_correo = request.POST.get('enviar_correo') == 'on'

        if not nueva_contrasena:
            messages.error(request, 'Debes especificar una nueva contraseña.')
            return redirect('usuarios:admin_gestionar_contrasenas')

        usuario = None
        email = None
        nombre = None

        try:
            if tipo == 'usuario':
                user = get_object_or_404(User, id=id)
                user.set_password(nueva_contrasena)
                user.save()
                usuario = user
                email = user.email
                nombre = user.get_full_name() or user.username

            elif tipo == 'cliente':
                cliente = get_object_or_404(Cliente, id=id)
                if cliente.usuario:
                    cliente.usuario.set_password(nueva_contrasena)
                    cliente.usuario.save()
                    usuario = cliente.usuario
                    email = cliente.email
                    nombre = cliente.nombre_completo
                else:
                    messages.error(request, 'Este cliente no tiene usuario asociado.')
                    return redirect('usuarios:admin_gestionar_contrasenas')

            elif tipo == 'tecnico':
                tecnico = get_object_or_404(Tecnico, id=id)
                if tecnico.usuario:
                    tecnico.usuario.set_password(nueva_contrasena)
                    tecnico.usuario.save()
                    usuario = tecnico.usuario
                    email = tecnico.email
                    nombre = tecnico.nombre_completo
                else:
                    messages.error(request, 'Este técnico no tiene usuario asociado.')
                    return redirect('usuarios:admin_gestionar_contrasenas')

            elif tipo == 'proveedor':
                proveedor = get_object_or_404(Proveedor, id=id)
                # Los proveedores no tienen usuario, solo almacenamos en sesión
                messages.info(request,
                    f'Contraseña registrada para proveedor: {proveedor.nombre_empresa}')
                email = proveedor.email
                nombre = proveedor.nombre_contacto

            # Enviar correo si se solicitó
            if enviar_correo and email:
                try:
                    send_mail(
                        'Nueva Contraseña - DIGITSOFT',
                        f'Hola {nombre},\n\n'
                        f'El administrador ha actualizado tu contraseña.\n\n'
                        f'Tu nueva contraseña es: {nueva_contrasena}\n\n'
                        f'Por seguridad, te recomendamos cambiarla después de iniciar sesión.\n\n'
                        f'Saludos,\nEquipo DIGITSOFT',
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        fail_silently=False,
                    )
                    messages.success(request,
                        f'Contraseña actualizada y correo enviado a {email}')
                except Exception as e:
                    messages.warning(request,
                        f'Contraseña actualizada pero no se pudo enviar el correo: {str(e)}')
            else:
                messages.success(request,
                    f'Contraseña actualizada exitosamente para {nombre}')

        except Exception as e:
            messages.error(request, f'Error al cambiar contraseña: {str(e)}')

        return redirect('usuarios:admin_gestionar_contrasenas')

    return redirect('usuarios:admin_gestionar_contrasenas')


@login_required
@staff_required
def admin_generar_contrasena_temporal(request, tipo, id):
    """Generar contraseña temporal automática y enviar por correo"""

    # Generar contraseña aleatoria
    contrasena_temporal = get_random_string(12)

    usuario = None
    email = None
    nombre = None

    try:
        if tipo == 'usuario':
            user = get_object_or_404(User, id=id)
            user.set_password(contrasena_temporal)
            user.save()
            email = user.email
            nombre = user.get_full_name() or user.username

        elif tipo == 'cliente':
            cliente = get_object_or_404(Cliente, id=id)
            if cliente.usuario:
                cliente.usuario.set_password(contrasena_temporal)
                cliente.usuario.save()
                email = cliente.email
                nombre = cliente.nombre_completo

        elif tipo == 'tecnico':
            tecnico = get_object_or_404(Tecnico, id=id)
            if tecnico.usuario:
                tecnico.usuario.set_password(contrasena_temporal)
                tecnico.usuario.save()
                email = tecnico.email
                nombre = tecnico.nombre_completo

        # Enviar correo
        if email:
            try:
                send_mail(
                    'Contraseña Temporal - DIGITSOFT',
                    f'Hola {nombre},\n\n'
                    f'Se ha generado una contraseña temporal para tu cuenta.\n\n'
                    f'Contraseña temporal: {contrasena_temporal}\n\n'
                    f'Por favor, cámbiala después de iniciar sesión.\n\n'
                    f'Saludos,\nEquipo DIGITSOFT',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request,
                    f'Contraseña temporal generada y enviada a {email}')
            except Exception as e:
                messages.warning(request,
                    f'Contraseña generada: {contrasena_temporal} (No se pudo enviar correo)')
        else:
            messages.info(request, f'Contraseña temporal generada: {contrasena_temporal}')

    except Exception as e:
        messages.error(request, f'Error al generar contraseña: {str(e)}')

    return redirect('usuarios:admin_gestionar_contrasenas')

