"""
Vistas para Recuperación de Contraseña
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .services_password import ServicioRecuperacionPassword


def get_client_ip(request):
    """Obtiene la IP del cliente"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@require_http_methods(["GET", "POST"])
def solicitar_recuperacion(request):
    """Paso 1: Solicitar código de recuperación"""

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()

        if not email:
            messages.error(request, '❌ Por favor ingresa tu email.')
            return render(request, 'usuarios/recuperar_paso1.html')

        # Obtener IP del cliente
        ip = get_client_ip(request)

        # Solicitar recuperación
        exito, mensaje, token = ServicioRecuperacionPassword.solicitar_recuperacion(email, ip)

        if exito:
            # Guardar email en sesión para el siguiente paso
            request.session['recovery_email'] = email
            messages.success(request, f'✅ {mensaje}')
            return redirect('usuarios:verificar_codigo')
        else:
            messages.warning(request, mensaje)
            return render(request, 'usuarios/recuperar_paso1.html')

    return render(request, 'usuarios/recuperar_paso1.html')


@require_http_methods(["GET", "POST"])
def verificar_codigo(request):
    """Paso 2: Verificar código recibido por email"""

    # Verificar que hay email en sesión
    email = request.session.get('recovery_email')
    if not email:
        messages.error(request, '❌ Sesión expirada. Inicia el proceso nuevamente.')
        return redirect('usuarios:solicitar_recuperacion')

    if request.method == 'POST':
        codigo = request.POST.get('codigo', '').strip()

        if not codigo:
            messages.error(request, '❌ Por favor ingresa el código.')
            return render(request, 'usuarios/recuperar_paso2.html', {'email': email})

        # Verificar código
        valido, mensaje, token = ServicioRecuperacionPassword.verificar_codigo(email, codigo)

        if valido:
            # Guardar token ID en sesión
            request.session['recovery_token_id'] = token.id
            messages.success(request, f'✅ {mensaje}')
            return redirect('usuarios:nueva_password')
        else:
            messages.error(request, f'❌ {mensaje}')
            return render(request, 'usuarios/recuperar_paso2.html', {'email': email})

    return render(request, 'usuarios/recuperar_paso2.html', {'email': email})


@require_http_methods(["GET", "POST"])
def nueva_password(request):
    """Paso 3: Establecer nueva contraseña"""

    # Verificar que hay token en sesión
    token_id = request.session.get('recovery_token_id')
    if not token_id:
        messages.error(request, '❌ Sesión expirada. Inicia el proceso nuevamente.')
        return redirect('usuarios:solicitar_recuperacion')

    # Obtener token
    from .models_tokens import TokenRecuperacion
    token = TokenRecuperacion.objects.filter(id=token_id).first()

    if not token or not token.es_valido:
        messages.error(request, '❌ El código ha expirado. Solicita uno nuevo.')
        # Limpiar sesión
        request.session.pop('recovery_email', None)
        request.session.pop('recovery_token_id', None)
        return redirect('usuarios:solicitar_recuperacion')

    if request.method == 'POST':
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # Validar que no estén vacías
        if not password1 or not password2:
            messages.error(request, '❌ Por favor completa ambos campos.')
            return render(request, 'usuarios/recuperar_paso3.html')

        # Validar que coincidan
        if password1 != password2:
            messages.error(request, '❌ Las contraseñas no coinciden.')
            return render(request, 'usuarios/recuperar_paso3.html')

        # Validar fortaleza de la contraseña
        valida, mensaje = ServicioRecuperacionPassword.validar_password(password1)
        if not valida:
            messages.error(request, f'❌ {mensaje}')
            return render(request, 'usuarios/recuperar_paso3.html')

        # Cambiar contraseña
        exito, mensaje = ServicioRecuperacionPassword.cambiar_password(token, password1)

        if exito:
            # Limpiar sesión
            request.session.pop('recovery_email', None)
            request.session.pop('recovery_token_id', None)

            messages.success(request, f'✅ {mensaje}')
            return redirect('usuarios:login')
        else:
            messages.error(request, f'❌ {mensaje}')
            return render(request, 'usuarios/recuperar_paso3.html')

    return render(request, 'usuarios/recuperar_paso3.html')


@require_http_methods(["POST"])
def reenviar_codigo(request):
    """Reenvía el código de recuperación"""

    email = request.session.get('recovery_email')
    if not email:
        messages.error(request, '❌ Sesión expirada.')
        return redirect('usuarios:solicitar_recuperacion')

    ip = get_client_ip(request)
    exito, mensaje, token = ServicioRecuperacionPassword.solicitar_recuperacion(email, ip)

    if exito:
        messages.success(request, '✅ Código reenviado a tu email.')
    else:
        messages.error(request, '❌ Error al reenviar el código.')

    return redirect('usuarios:verificar_codigo')

