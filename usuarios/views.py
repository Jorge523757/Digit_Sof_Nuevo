"""
DIGT SOFT - Módulo de Usuarios
Views - Vistas de Autenticación, Registro, Perfil y Notificaciones
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import RegistroClienteForm, RegistroTecnicoForm, PerfilUsuarioForm
from .models import PerfilUsuario, Notificacion
from .decorators import admin_required, staff_required


# ==================== AUTENTICACIÓN ====================


def registro_cliente(request):
    """Vista para registro de nuevos clientes"""
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                '¡Registro exitoso! Tu cuenta ha sido creada. Ahora puedes iniciar sesión.'
            )
            return redirect('usuarios:login')
        else:
            messages.error(
                request,
                'Por favor, corrige los errores en el formulario.'
            )
    else:
        form = RegistroClienteForm()

    return render(request, 'usuarios/registro.html', {'form': form})


def registro_tecnico(request):
    """Vista para registro de nuevos técnicos"""
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = RegistroTecnicoForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                '¡Registro exitoso! Tu cuenta de técnico ha sido creada. Ahora puedes iniciar sesión.'
            )
            return redirect('usuarios:login')
        else:
            messages.error(
                request,
                'Por favor, corrige los errores en el formulario.'
            )
    else:
        form = RegistroTecnicoForm()

    return render(request, 'usuarios/registro_tecnico.html', {'form': form})


def login_view(request):
    """Vista personalizada de login"""
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Verificar si el usuario está bloqueado
            if hasattr(user, 'perfil') and user.perfil.bloqueado:
                messages.error(
                    request,
                    f'Tu cuenta ha sido bloqueada. Motivo: {user.perfil.motivo_bloqueo or "No especificado"}'
                )
                return render(request, 'usuarios/login.html')

            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.first_name or user.username}!')

            # Redirigir según el tipo de usuario
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)

            return redirect('dashboard:index')
        else:
            messages.error(
                request,
                'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.'
            )

    return render(request, 'usuarios/login.html')


@login_required
def logout_view(request):
    """Vista de cierre de sesión"""
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('core:home')


@login_required
def perfil_view(request):
    """Vista del perfil de usuario"""
    perfil = request.user.perfil

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()

            # Actualizar también el nombre del usuario
            request.user.first_name = request.POST.get('first_name', request.user.first_name)
            request.user.last_name = request.POST.get('last_name', request.user.last_name)
            request.user.save()

            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('usuarios:perfil')
    else:
        form = PerfilUsuarioForm(instance=perfil)

    context = {
        'perfil': perfil,
        'form': form
    }
    return render(request, 'usuarios/perfil.html', context)


@login_required
def cambiar_contrasena(request):
    """Vista para cambiar contraseña"""
    from django.contrib.auth.forms import PasswordChangeForm
    from django.contrib.auth import update_session_auth_hash

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            return redirect('usuarios:perfil')
        else:
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'usuarios/cambiar_contrasena.html', {'form': form})


# ==================== RECUPERACIÓN DE CONTRASEÑA ====================

def recuperar_password(request):
    """Vista para solicitar recuperación de contraseña"""
    from .forms import RecuperarPasswordForm
    from .models import PasswordResetToken
    from django.core.mail import send_mail
    from django.conf import settings

    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = RecuperarPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)

            # Crear token de recuperación
            token = PasswordResetToken.create_token(user)

            # Construir URL de reset
            reset_url = request.build_absolute_uri(
                f'/usuarios/reset-password/{token.token}/'
            )

            # Enviar email (en desarrollo, solo mostrar mensaje)
            try:
                # Mensaje de email
                subject = 'Recuperación de Contraseña - DIGITSOFT'
                message = f"""
Hola {user.first_name or user.username},

Has solicitado recuperar tu contraseña en DIGITSOFT.

Para crear una nueva contraseña, haz clic en el siguiente enlace:
{reset_url}

Este enlace es válido por 24 horas.

Si no solicitaste este cambio, puedes ignorar este mensaje.

Saludos,
Equipo DIGITSOFT
"""

                # En desarrollo, solo mostrar en consola
                print("=" * 80)
                print("EMAIL DE RECUPERACIÓN")
                print("=" * 80)
                print(f"Para: {email}")
                print(f"Asunto: {subject}")
                print(message)
                print("=" * 80)
                print(f"URL de reset: {reset_url}")
                print("=" * 80)

                # Intentar enviar email (si está configurado)
                # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

                messages.success(
                    request,
                    f'✅ Se ha enviado un correo a {email} con las instrucciones para recuperar tu contraseña. '
                    f'Por favor revisa tu bandeja de entrada y spam.'
                )

                # En desarrollo, también mostrar el link directamente
                messages.info(
                    request,
                    f'🔗 Link de recuperación (solo en desarrollo): '
                    f'<a href="{reset_url}" class="alert-link">Click aquí para resetear</a>'
                )

                return redirect('usuarios:login')

            except Exception as e:
                messages.error(request, f'Error al enviar el correo: {str(e)}')
    else:
        form = RecuperarPasswordForm()

    return render(request, 'usuarios/recuperar_password.html', {'form': form})


def reset_password(request, token):
    """Vista para resetear la contraseña con token"""
    from .forms import ResetPasswordForm
    from .models import PasswordResetToken

    try:
        reset_token = PasswordResetToken.objects.get(token=token)

        # Verificar si el token es válido
        if not reset_token.is_valid():
            messages.error(
                request,
                '❌ Este enlace de recuperación ha expirado o ya fue usado. '
                'Por favor solicita uno nuevo.'
            )
            return redirect('usuarios:recuperar_password')

        if request.method == 'POST':
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                # Cambiar la contraseña
                new_password = form.cleaned_data['new_password1']
                user = reset_token.user
                user.set_password(new_password)
                user.save()

                # Marcar token como usado
                reset_token.mark_as_used()

                messages.success(
                    request,
                    '✅ Tu contraseña ha sido cambiada exitosamente. '
                    'Ahora puedes iniciar sesión con tu nueva contraseña.'
                )
                return redirect('usuarios:login')
        else:
            form = ResetPasswordForm()

        context = {
            'form': form,
            'token': token,
            'user': reset_token.user
        }
        return render(request, 'usuarios/reset_password.html', context)

    except PasswordResetToken.DoesNotExist:
        messages.error(
            request,
            '❌ El enlace de recuperación no es válido. '
            'Por favor solicita uno nuevo.'
        )
        return redirect('usuarios:recuperar_password')


# ==================== GESTIÓN DE USUARIOS (ADMIN) ====================

@login_required
@staff_required
def listar_usuarios(request):
    """Vista para listar todos los usuarios del sistema"""
    # Búsqueda
    query = request.GET.get('q', '')
    rol_filtro = request.GET.get('rol', '')
    estado_filtro = request.GET.get('estado', '')

    usuarios = User.objects.all().order_by('-date_joined')

    # Aplicar filtros
    if query:
        usuarios = usuarios.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

    if rol_filtro == 'superuser':
        usuarios = usuarios.filter(is_superuser=True)
    elif rol_filtro == 'staff':
        usuarios = usuarios.filter(is_staff=True, is_superuser=False)
    elif rol_filtro == 'normal':
        usuarios = usuarios.filter(is_staff=False, is_superuser=False)

    if estado_filtro == 'activo':
        usuarios = usuarios.filter(is_active=True)
    elif estado_filtro == 'inactivo':
        usuarios = usuarios.filter(is_active=False)

    # Estadísticas
    total_usuarios = User.objects.count()
    usuarios_activos = User.objects.filter(is_active=True).count()
    usuarios_inactivos = User.objects.filter(is_active=False).count()
    usuarios_staff = User.objects.filter(is_staff=True).count()

    context = {
        'usuarios': usuarios,
        'total_usuarios': total_usuarios,
        'usuarios_activos': usuarios_activos,
        'usuarios_inactivos': usuarios_inactivos,
        'usuarios_staff': usuarios_staff,
    }

    return render(request, 'usuarios/gestionar/listar.html', context)


@login_required
@staff_required
def crear_usuario(request):
    """Vista para crear un nuevo usuario"""
    if request.method == 'POST':
        from django.contrib.auth.forms import UserCreationForm
        from .forms import UsuarioCrearForm

        form = UsuarioCrearForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Actualizar perfil
            perfil = user.perfil
            perfil.tipo_usuario = request.POST.get('tipo_usuario', 'CLIENTE')
            perfil.telefono = request.POST.get('telefono', '')
            perfil.direccion = request.POST.get('direccion', '')
            perfil.documento = request.POST.get('documento', '')
            perfil.save()

            messages.success(request, f'Usuario {user.username} creado exitosamente.')
            return redirect('usuarios:detalle_usuario', user_id=user.id)
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        from .forms import UsuarioCrearForm
        form = UsuarioCrearForm()

    context = {
        'form': form,
        'tipos_usuario': PerfilUsuario.TIPO_USUARIO_CHOICES,
    }

    return render(request, 'usuarios/gestionar/crear.html', context)


@login_required
@staff_required
def detalle_usuario(request, user_id):
    """Vista para ver el detalle de un usuario"""
    usuario = get_object_or_404(User.objects.select_related('perfil'), id=user_id)

    context = {
        'usuario': usuario,
        'perfil': usuario.perfil,
    }

    return render(request, 'usuarios/gestionar/detalle.html', context)


@login_required
@staff_required
def editar_usuario(request, user_id):
    """Vista para editar un usuario"""
    usuario = get_object_or_404(User, id=user_id)
    perfil = usuario.perfil

    if request.method == 'POST':
        # Actualizar datos de usuario
        usuario.username = request.POST.get('username', usuario.username)
        usuario.email = request.POST.get('email', usuario.email)
        usuario.first_name = request.POST.get('first_name', '')
        usuario.last_name = request.POST.get('last_name', '')
        usuario.is_active = request.POST.get('is_active') == 'on'

        # Solo admin puede cambiar is_staff
        if request.user.is_superuser:
            usuario.is_staff = request.POST.get('is_staff') == 'on'

        usuario.save()

        # Actualizar perfil
        perfil.tipo_usuario = request.POST.get('tipo_usuario', perfil.tipo_usuario)
        perfil.telefono = request.POST.get('telefono', '')
        perfil.direccion = request.POST.get('direccion', '')
        perfil.documento = request.POST.get('documento', '')
        perfil.save()

        messages.success(request, f'Usuario {usuario.username} actualizado exitosamente.')
        return redirect('usuarios:detalle_usuario', user_id=usuario.id)

    context = {
        'usuario': usuario,
        'perfil': perfil,
        'tipos_usuario': PerfilUsuario.TIPO_USUARIO_CHOICES,
    }

    return render(request, 'usuarios/gestionar/editar.html', context)


@login_required
@staff_required
@require_http_methods(["POST"])
def eliminar_usuario(request, user_id):
    """Vista para eliminar un usuario"""
    usuario = get_object_or_404(User, id=user_id)

    # No permitir eliminar superusuarios o al mismo usuario
    if usuario.is_superuser:
        messages.error(request, 'No se puede eliminar un superusuario.')
        return redirect('usuarios:listar_usuarios')

    if usuario == request.user:
        messages.error(request, 'No puedes eliminar tu propia cuenta.')
        return redirect('usuarios:listar_usuarios')

    username = usuario.username
    usuario.delete()

    messages.success(request, f'Usuario {username} eliminado exitosamente.')
    return redirect('usuarios:listar_usuarios')


@login_required
@staff_required
@require_http_methods(["POST"])
def bloquear_usuario(request, user_id):
    """Vista para bloquear un usuario"""
    usuario = get_object_or_404(User, id=user_id)

    if usuario.is_superuser:
        messages.error(request, 'No se puede bloquear un superusuario.')
        return redirect('usuarios:detalle_usuario', user_id=user_id)

    if usuario == request.user:
        messages.error(request, 'No puedes bloquearte a ti mismo.')
        return redirect('usuarios:detalle_usuario', user_id=user_id)

    motivo = request.POST.get('motivo', 'Sin motivo especificado')
    usuario.perfil.bloquear(motivo)

    messages.success(request, f'Usuario {usuario.username} bloqueado exitosamente.')
    return redirect('usuarios:detalle_usuario', user_id=user_id)


@login_required
@staff_required
@require_http_methods(["POST"])
def desbloquear_usuario(request, user_id):
    """Vista para desbloquear un usuario"""
    usuario = get_object_or_404(User, id=user_id)
    usuario.perfil.desbloquear()

    messages.success(request, f'Usuario {usuario.username} desbloqueado exitosamente.')
    return redirect('usuarios:detalle_usuario', user_id=user_id)


@login_required
@admin_required
@require_http_methods(["POST"])
def toggle_staff(request, user_id):
    """Vista para cambiar el estado de staff de un usuario"""
    usuario = get_object_or_404(User, id=user_id)

    if usuario.is_superuser:
        messages.error(request, 'No se puede modificar un superusuario.')
        return redirect('usuarios:detalle_usuario', user_id=user_id)

    usuario.is_staff = not usuario.is_staff
    usuario.save()

    estado = "staff" if usuario.is_staff else "usuario normal"
    messages.success(request, f'Usuario {usuario.username} ahora es {estado}.')
    return redirect('usuarios:detalle_usuario', user_id=user_id)


