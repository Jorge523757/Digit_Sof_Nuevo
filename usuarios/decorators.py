"""
DIGT SOFT - Decoradores de Permisos
Controla el acceso a vistas según el tipo de usuario
"""

from functools import wraps
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def superuser_required(view_func):
    """
    Decorador que requiere que el usuario sea superusuario
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
            return redirect('usuarios:login')

        if not request.user.is_superuser:
            messages.error(
                request,
                'No tienes permisos para acceder a esta sección. Solo administradores.'
            )
            return redirect('dashboard:index')

        return view_func(request, *args, **kwargs)
    return wrapper


def staff_required(view_func):
    """
    Decorador que requiere que el usuario sea staff (personal autorizado)
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
            return redirect('usuarios:login')

        if not (request.user.is_staff or request.user.is_superuser):
            messages.error(
                request,
                'No tienes permisos para acceder a esta sección. Solo personal autorizado.'
            )
            return redirect('dashboard:index')

        return view_func(request, *args, **kwargs)
    return wrapper


def admin_or_staff_required(view_func):
    """
    Decorador que requiere que el usuario sea admin o staff
    Alias de staff_required para mayor claridad
    """
    return staff_required(view_func)


def permission_required_custom(permission_name):
    """
    Decorador personalizado que verifica permisos específicos
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
                return redirect('usuarios:login')

            if not (request.user.is_superuser or request.user.has_perm(permission_name)):
                messages.error(
                    request,
                    'No tienes los permisos necesarios para realizar esta acción.'
                )
                return redirect('dashboard:index')

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def verificar_perfil_activo(view_func):
    """
    Decorador que verifica que el perfil del usuario esté activo
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
            return redirect('usuarios:login')

        # Verificar si tiene perfil y si está bloqueado
        if hasattr(request.user, 'perfil'):
            if request.user.perfil.bloqueado:
                messages.error(
                    request,
                    f'Tu cuenta está bloqueada. Motivo: {request.user.perfil.motivo_bloqueo or "No especificado"}'
                )
                return redirect('usuarios:login')

        return view_func(request, *args, **kwargs)
    return wrapper

