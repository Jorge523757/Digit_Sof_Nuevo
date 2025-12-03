"""
DIGT SOFT - Módulo de Usuarios
Views - Vistas de Autenticación y Registro
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from .forms import RegistroClienteForm, PerfilUsuarioForm
from .models import PerfilUsuario


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

