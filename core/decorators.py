"""
DIGIT SOFT - Decoradores de Seguridad
Decoradores personalizados para control de acceso
"""

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def es_admin(user):
    """Verifica que el usuario sea administrador"""
    return user.is_authenticated and (user.is_staff or user.is_superuser)


def es_cliente(user):
    """Verifica que el usuario sea cliente"""
    if not user.is_authenticated:
        return False
    try:
        return user.perfil.tipo_usuario == 'CLIENTE'
    except:
        return False


def es_tecnico(user):
    """Verifica que el usuario sea técnico"""
    if not user.is_authenticated:
        return False
    try:
        return user.perfil.tipo_usuario == 'TECNICO'
    except:
        return False


def es_cliente_o_tecnico(user):
    """Verifica que el usuario sea cliente o técnico"""
    return es_cliente(user) or es_tecnico(user)


def es_admin_o_tecnico(user):
    """Verifica que el usuario sea admin o técnico"""
    return es_admin(user) or es_tecnico(user)


# Decoradores combinados para usar directamente
admin_required = user_passes_test(es_admin, login_url='/usuarios/login/')
cliente_required = user_passes_test(es_cliente, login_url='/usuarios/login/')
tecnico_required = user_passes_test(es_tecnico, login_url='/usuarios/login/')
cliente_o_tecnico_required = user_passes_test(es_cliente_o_tecnico, login_url='/usuarios/login/')
admin_o_tecnico_required = user_passes_test(es_admin_o_tecnico, login_url='/usuarios/login/')


def verificar_permiso_objeto(get_objeto_func, verificar_propietario_func):
    """
    Decorador genérico para verificar permisos sobre un objeto

    Args:
        get_objeto_func: Función que obtiene el objeto (recibe request, *args, **kwargs)
        verificar_propietario_func: Función que verifica si el usuario es propietario (recibe user, objeto)
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def wrapper(request, *args, **kwargs):
            # Si es admin, permitir siempre
            if es_admin(request.user):
                return view_func(request, *args, **kwargs)

            # Obtener objeto
            objeto = get_objeto_func(request, *args, **kwargs)

            if objeto is None:
                messages.error(request, 'El objeto solicitado no existe.')
                return redirect('dashboard:index')

            # Verificar si es propietario
            if not verificar_propietario_func(request.user, objeto):
                messages.error(request, 'No tienes permiso para acceder a este recurso.')
                return redirect('dashboard:index')

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator

