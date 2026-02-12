"""
DIGIT SOFT - Vistas de Gestión de Contraseñas (SOLO ADMIN)
Permite al administrador cambiar contraseñas de clientes y técnicos
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import messages
from django.db.models import Q


def es_admin(user):
    """Verificar que el usuario sea administrador"""
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(es_admin)
def admin_gestionar_contrasenas(request):
    """
    Vista principal para gestión de contraseñas
    SOLO ADMIN: Lista de TODOS los clientes y técnicos (con o sin usuario)
    """
    
    # Obtener parámetros de búsqueda
    busqueda = request.GET.get('busqueda', '')
    tipo_filtro = request.GET.get('tipo', '')  # CLIENTE o TECNICO
    
    # Importar modelos
    from clientes.models import Cliente
    from tecnicos.models import Tecnico

    # Lista combinada de usuarios
    usuarios_lista = []

    # Obtener TODOS los clientes
    if not tipo_filtro or tipo_filtro == 'CLIENTE':
        clientes = Cliente.objects.filter(activo=True).order_by('nombres')

        if busqueda:
            clientes = clientes.filter(
                Q(nombres__icontains=busqueda) |
                Q(apellidos__icontains=busqueda) |
                Q(correo__icontains=busqueda) |
                Q(telefono__icontains=busqueda)
            )

        for cliente in clientes:
            # Buscar si tiene usuario
            try:
                usuario = User.objects.filter(email=cliente.correo).first()
            except:
                usuario = None

            usuarios_lista.append({
                'tipo': 'CLIENTE',
                'tipo_display': 'Cliente',
                'id': cliente.id,
                'nombre': f"{cliente.nombres} {cliente.apellidos}",
                'email': cliente.correo,
                'telefono': cliente.telefono,
                'usuario': usuario,
                'tiene_usuario': usuario is not None,
                'activo': cliente.activo if usuario else True,
            })

    # Obtener TODOS los técnicos
    if not tipo_filtro or tipo_filtro == 'TECNICO':
        tecnicos = Tecnico.objects.filter(activo=True, eliminado=False).order_by('nombres')

        if busqueda:
            tecnicos = tecnicos.filter(
                Q(nombres__icontains=busqueda) |
                Q(apellidos__icontains=busqueda) |
                Q(correo__icontains=busqueda) |
                Q(telefono__icontains=busqueda)
            )

        for tecnico in tecnicos:
            # Buscar si tiene usuario
            try:
                usuario = User.objects.filter(email=tecnico.correo).first()
            except:
                usuario = None

            usuarios_lista.append({
                'tipo': 'TECNICO',
                'tipo_display': 'Técnico',
                'id': tecnico.id,
                'nombre': f"{tecnico.nombres} {tecnico.apellidos}",
                'email': tecnico.correo,
                'telefono': tecnico.telefono,
                'usuario': usuario,
                'tiene_usuario': usuario is not None,
                'activo': tecnico.activo if usuario else True,
            })

    # Ordenar por nombre
    usuarios_lista.sort(key=lambda x: x['nombre'])

    # Contar por tipo
    total_usuarios = len(usuarios_lista)
    clientes_count = Cliente.objects.filter(activo=True).count()
    tecnicos_count = Tecnico.objects.filter(activo=True, eliminado=False).count()

    context = {
        'usuarios': usuarios_lista,
        'busqueda': busqueda,
        'tipo_filtro': tipo_filtro,
        'total_usuarios': total_usuarios,
        'clientes_count': clientes_count,
        'tecnicos_count': tecnicos_count,
    }
    
    return render(request, 'usuarios/admin_gestionar_contrasenas.html', context)


@login_required
@user_passes_test(es_admin)
def admin_cambiar_contrasena(request, user_id):
    """
    Vista para que el ADMIN cambie la contraseña de un usuario
    """
    
    usuario = get_object_or_404(User, pk=user_id)
    
    # Verificar que no sea un admin
    if usuario.is_staff or usuario.is_superuser:
        messages.error(request, '❌ No puedes cambiar la contraseña de un administrador desde aquí.')
        return redirect('usuarios:admin_gestionar_contrasenas')
    
    if request.method == 'POST':
        form = SetPasswordForm(usuario, request.POST)
        if form.is_valid():
            form.save()
            
            # Obtener tipo de usuario
            try:
                tipo_usuario = usuario.perfil.get_tipo_usuario_display()
            except:
                tipo_usuario = 'Usuario'
            
            messages.success(
                request,
                f'✅ Contraseña cambiada exitosamente para {tipo_usuario}: {usuario.username}'
            )
            return redirect('usuarios:admin_gestionar_contrasenas')
        else:
            messages.error(request, '❌ Por favor corrige los errores en el formulario.')
    else:
        form = SetPasswordForm(usuario)
    
    # Obtener información adicional del usuario
    try:
        perfil = usuario.perfil
        tipo_usuario = perfil.get_tipo_usuario_display()
    except:
        perfil = None
        tipo_usuario = 'Usuario'
    
    datos_adicionales = None
    
    if perfil and perfil.tipo_usuario == 'CLIENTE':
        try:
            from clientes.models import Cliente
            datos_adicionales = Cliente.objects.filter(correo=usuario.email).first()
        except:
            pass
    
    elif perfil and perfil.tipo_usuario == 'TECNICO':
        try:
            from tecnicos.models import Tecnico
            datos_adicionales = Tecnico.objects.filter(correo=usuario.email).first()
        except:
            pass
    
    context = {
        'form': form,
        'usuario': usuario,
        'tipo_usuario': tipo_usuario,
        'perfil': perfil,
        'datos_adicionales': datos_adicionales,
    }
    
    return render(request, 'usuarios/admin_cambiar_contrasena.html', context)

