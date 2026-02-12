"""
DIGIT SOFT - Vistas de Reportes de Daño
Vistas para que clientes reporten equipos dañados
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from .models import RegistroDano
from .forms import ReporteDanoForm
from clientes.models import Cliente
from notificaciones.services import ServicioNotificaciones


@login_required
def crear_reporte(request):
    """Vista para que el cliente reporte un equipo dañado"""

    # Obtener el cliente asociado al usuario
    try:
        perfil = request.user.perfil
        if perfil.tipo_usuario != 'CLIENTE':
            messages.error(request, 'Solo los clientes pueden reportar equipos dañados.')
            return redirect('dashboard:index')

        cliente = perfil.cliente
        if not cliente:
            messages.error(request, 'No se encontró un cliente asociado a tu usuario.')
            return redirect('dashboard:index')
    except Exception as e:
        messages.error(request, 'Error al obtener información del cliente.')
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = ReporteDanoForm(request.POST, cliente=cliente)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.cliente = cliente
            reporte.usuario = request.user
            reporte.estado = 'PENDIENTE'
            reporte.save()

            # Notificar al administrador
            try:
                ServicioNotificaciones.notificar_admin_reporte_cliente(reporte)
                messages.success(
                    request,
                    f'✅ Reporte #{reporte.numero_reporte} creado exitosamente. '
                    f'El administrador ha sido notificado y se le asignará un técnico pronto.'
                )
            except Exception as e:
                messages.warning(
                    request,
                    f'Reporte creado, pero hubo un error al enviar la notificación: {str(e)}'
                )

            return redirect('reportes_dano:mis_reportes')
    else:
        form = ReporteDanoForm(cliente=cliente)

    context = {
        'form': form,
        'cliente': cliente,
    }
    return render(request, 'reportes_dano/crear_reporte.html', context)


@login_required
def mis_reportes(request):
    """Vista para que el cliente vea sus reportes"""

    try:
        perfil = request.user.perfil
        if perfil.tipo_usuario != 'CLIENTE':
            messages.error(request, 'Solo los clientes pueden ver sus reportes.')
            return redirect('dashboard:index')

        cliente = perfil.cliente
        if not cliente:
            messages.error(request, 'No se encontró un cliente asociado a tu usuario.')
            return redirect('dashboard:index')
    except Exception as e:
        messages.error(request, 'Error al obtener información del cliente.')
        return redirect('dashboard:index')

    # Obtener reportes del cliente
    reportes = RegistroDano.objects.filter(cliente=cliente).order_by('-fecha_reporte')

    context = {
        'reportes': reportes,
        'cliente': cliente,
    }
    return render(request, 'reportes_dano/mis_reportes.html', context)


@login_required
def detalle_reporte(request, reporte_id):
    """Vista para ver detalle de un reporte"""

    reporte = get_object_or_404(RegistroDano, id=reporte_id)

    # Verificar permisos
    perfil = request.user.perfil

    # Cliente solo puede ver sus reportes
    if perfil.tipo_usuario == 'CLIENTE':
        if reporte.cliente != perfil.cliente:
            messages.error(request, 'No tienes permiso para ver este reporte.')
            return redirect('reportes_dano:mis_reportes')

    # Técnico puede ver reportes de órdenes asignadas
    elif perfil.tipo_usuario == 'TECNICO':
        # TODO: Verificar si el técnico tiene una orden relacionada
        pass

    # Admin puede ver todo
    elif not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'No tienes permiso para ver este reporte.')
        return redirect('dashboard:index')

    context = {
        'reporte': reporte,
    }
    return render(request, 'reportes_dano/detalle_reporte.html', context)


@login_required
def lista_reportes_admin(request):
    """Vista para que el admin vea todos los reportes"""

    # Solo admin
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'No tienes permiso para acceder a esta página.')
        return redirect('dashboard:index')

    # Filtros
    estado = request.GET.get('estado', '')
    busqueda = request.GET.get('busqueda', '')

    reportes = RegistroDano.objects.all().order_by('-fecha_reporte')

    if estado:
        reportes = reportes.filter(estado=estado)

    if busqueda:
        reportes = reportes.filter(
            Q(numero_reporte__icontains=busqueda) |
            Q(cliente__nombre__icontains=busqueda) |
            Q(cliente__apellido__icontains=busqueda) |
            Q(descripcion_dano__icontains=busqueda)
        )

    # Estadísticas
    total_reportes = RegistroDano.objects.count()
    pendientes = RegistroDano.objects.filter(estado='PENDIENTE').count()
    en_proceso = RegistroDano.objects.filter(estado__in=['REVISADO', 'ASIGNADO', 'EN_PROCESO']).count()
    completados = RegistroDano.objects.filter(estado='COMPLETADO').count()

    context = {
        'reportes': reportes,
        'total_reportes': total_reportes,
        'pendientes': pendientes,
        'en_proceso': en_proceso,
        'completados': completados,
        'estado_filter': estado,
        'busqueda': busqueda,
    }
    return render(request, 'reportes_dano/lista_admin.html', context)

