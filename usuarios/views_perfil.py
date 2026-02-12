"""
DIGIT SOFT - Vistas de Recuperación de Contraseña
Permite a clientes y técnicos cambiar su contraseña
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User


@login_required
def cambiar_contrasena(request):
    """
    Vista para que el usuario cambie su propia contraseña
    Accesible para: Cliente, Técnico
    """

    # Verificar que NO sea admin/staff (ellos usan el panel admin)
    if request.user.is_staff or request.user.is_superuser:
        messages.warning(request, 'Los administradores deben usar el panel de administración.')
        return redirect('admin:index')

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Importante: Mantener la sesión activa después del cambio
            update_session_auth_hash(request, user)

            messages.success(
                request,
                '✅ Tu contraseña ha sido cambiada exitosamente. '
                'Ahora puedes iniciar sesión con tu nueva contraseña.'
            )
            return redirect('usuarios:mi_perfil')
        else:
            messages.error(
                request,
                '❌ Por favor corrige los errores en el formulario.'
            )
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
        'titulo': 'Cambiar Contraseña',
    }
    return render(request, 'usuarios/cambiar_contrasena.html', context)


@login_required
def mi_perfil(request):
    """
    Vista del perfil del usuario
    Muestra información y permite acceder a cambio de contraseña
    """

    try:
        perfil = request.user.perfil
    except:
        perfil = None

    # Obtener información adicional según el tipo
    datos_adicionales = None

    if perfil and perfil.tipo_usuario == 'CLIENTE':
        try:
            from clientes.models import Cliente
            datos_adicionales = Cliente.objects.filter(correo=request.user.email).first()
        except:
            pass

    elif perfil and perfil.tipo_usuario == 'TECNICO':
        try:
            from tecnicos.models import Tecnico
            datos_adicionales = Tecnico.objects.filter(correo=request.user.email).first()
        except:
            pass

    context = {
        'perfil': perfil,
        'datos_adicionales': datos_adicionales,
    }
    return render(request, 'usuarios/mi_perfil.html', context)

