"""
Vistas para Recuperación de Contraseña
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .services_password import ServicioRecuperacionPassword
from .forms import RecuperarPasswordForm, VerificarCodigoForm, NuevaPasswordForm


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
    """Paso 1: Solicitar código de recuperación (SIN reCAPTCHA)"""

    if request.method == 'POST':
        # Obtener email directamente del POST (sin formulario)
        email = request.POST.get('email', '').strip().lower()

        if not email:
            messages.error(request, '❌ Por favor ingresa tu correo electrónico.')
            return render(request, 'usuarios/recuperar_paso1.html')

        # Validar formato de email básico
        if '@' not in email or '.' not in email:
            messages.error(request, '❌ Por favor ingresa un correo electrónico válido.')
            return render(request, 'usuarios/recuperar_paso1.html')

        # Verificar que el email existe en el sistema (case-insensitive)
        from django.contrib.auth.models import User
        from django.db.models import Q

        # Buscar usuario sin importar mayúsculas/minúsculas
        usuario = User.objects.filter(Q(email__iexact=email)).first()

        if not usuario:
            messages.error(
                request,
                f'❌ No existe una cuenta con este correo electrónico.<br>'
                f'<small style="color: #666;">Email ingresado: <strong>{email}</strong></small><br>'
                f'<small style="color: #666;">Verifica que sea el correo con el que te registraste.</small>'
            )
            return render(request, 'usuarios/recuperar_paso1.html')

        # Obtener IP del cliente
        ip = get_client_ip(request)

        # Solicitar recuperación (usar el email exacto del usuario en la BD)
        exito, mensaje, token = ServicioRecuperacionPassword.solicitar_recuperacion(
            usuario.email,  # Email exacto de la base de datos
            ip
        )

        if exito:
            # Guardar email Y código en sesión para el siguiente paso
            request.session['recovery_email'] = usuario.email

            # En modo desarrollo, guardar el código en sesión para mostrarlo
            from django.conf import settings
            if settings.DEBUG and token:
                request.session['recovery_code_debug'] = token.codigo
                request.session['recovery_username'] = usuario.username
                messages.success(request, f'✅ Código generado para {usuario.username}. Revisa la siguiente pantalla.')
            else:
                messages.success(request, f'✅ {mensaje}')

            return redirect('usuarios:verificar_codigo')
        else:
            messages.warning(request, mensaje)
            return render(request, 'usuarios/recuperar_paso1.html')

    # GET request - mostrar formulario vacío
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
        form = VerificarCodigoForm(request.POST)

        if form.is_valid():
            codigo = form.cleaned_data['codigo']

            # Verificar código
            valido, mensaje, token = ServicioRecuperacionPassword.verificar_codigo(email, codigo)

            if valido:
                # Guardar token ID en sesión
                request.session['recovery_token_id'] = token.id
                messages.success(request, f'✅ {mensaje}')
                return redirect('usuarios:nueva_password')
            else:
                messages.error(request, f'❌ {mensaje}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = VerificarCodigoForm()

    # Obtener código de debug de la sesión (si existe)
    codigo_debug = request.session.get('recovery_code_debug', None)
    username_debug = request.session.get('recovery_username', None)

    # Limpiar de la sesión después de leerlo
    if 'recovery_code_debug' in request.session:
        del request.session['recovery_code_debug']
    if 'recovery_username' in request.session:
        del request.session['recovery_username']

    return render(request, 'usuarios/recuperar_paso2.html', {
        'form': form,
        'email': email,
        'codigo_debug': codigo_debug,
        'username_debug': username_debug,
    })


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
        form = NuevaPasswordForm(request.POST)

        if form.is_valid():
            password1 = form.cleaned_data['password1']

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
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = NuevaPasswordForm()

    return render(request, 'usuarios/recuperar_paso3.html', {'form': form})


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

