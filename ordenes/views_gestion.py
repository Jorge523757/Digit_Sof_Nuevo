"""
DIGIT SOFT - Vistas adicionales de Órdenes de Servicio
Vistas para asignación y diagnóstico
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from .models import OrdenServicio
from .forms import AsignarTecnicoForm, DiagnosticoForm
from reportes_dano.models import RegistroDano
from tecnicos.models import Tecnico
from notificaciones.services import ServicioNotificaciones


def es_staff(user):
    """Verifica si el usuario es staff"""
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def asignar_tecnico(request, reporte_id):
    """
    Vista para que el admin asigne un técnico a un reporte
    y cree la orden de servicio
    """

    reporte = get_object_or_404(RegistroDano, id=reporte_id)

    # Verificar que no tenga orden ya
    if reporte.orden:
        messages.warning(request, 'Este reporte ya tiene una orden de servicio asignada.')
        return redirect('ordenes:detalle', orden_id=reporte.orden.id)

    if request.method == 'POST':
        # Crear orden de servicio basada en el reporte
        orden = OrdenServicio.objects.create(
            cliente=reporte.cliente,
            tipo_equipo=reporte.equipo.tipo_equipo if reporte.equipo else 'No especificado',
            marca=reporte.equipo.marca if reporte.equipo else 'No especificado',
            modelo=reporte.equipo.modelo if reporte.equipo else 'No especificado',
            serie=reporte.equipo.numero_serie if reporte.equipo else '',
            falla_reportada=reporte.descripcion_dano,
            tiempo_requerido_cliente=reporte.tiempo_requerido_cliente,
            reporte_relacionado=reporte,
            estado='RECIBIDA'
        )

        # Asignar técnico si se seleccionó
        tecnico_id = request.POST.get('tecnico_asignado')
        if tecnico_id:
            try:
                tecnico = Tecnico.objects.get(id=tecnico_id, activo=True, eliminado=False)
                orden.tecnico_asignado = tecnico

                # Asignar prioridad
                prioridad = request.POST.get('prioridad', 'MEDIA')
                orden.prioridad = prioridad

                # Fecha de compromiso si se especificó
                fecha_compromiso = request.POST.get('fecha_compromiso')
                if fecha_compromiso:
                    orden.fecha_compromiso = fecha_compromiso

                orden.save()

                # Actualizar estado del reporte
                reporte.orden = orden
                reporte.estado = 'ASIGNADO'
                reporte.save()

                # Notificar al técnico
                try:
                    ServicioNotificaciones.notificar_tecnico_asignacion(orden)
                    messages.success(
                        request,
                        f'✅ Orden #{orden.numero_orden} creada y técnico {tecnico.nombre_completo} notificado.'
                    )
                except Exception as e:
                    messages.warning(
                        request,
                        f'Orden creada pero error al notificar técnico: {str(e)}'
                    )

                return redirect('ordenes:detalle', orden_id=orden.id)

            except Tecnico.DoesNotExist:
                orden.delete()
                messages.error(request, 'El técnico seleccionado no es válido.')
        else:
            orden.save()
            reporte.orden = orden
            reporte.estado = 'REVISADO'
            reporte.save()
            messages.success(request, f'✅ Orden #{orden.numero_orden} creada. Asigne un técnico.')
            return redirect('ordenes:detalle', orden_id=orden.id)

    # Obtener técnicos disponibles
    tecnicos_disponibles = Tecnico.objects.filter(
        activo=True,
        eliminado=False
    ).order_by('nombres')

    context = {
        'reporte': reporte,
        'tecnicos': tecnicos_disponibles,
    }
    return render(request, 'ordenes/asignar_tecnico.html', context)


@login_required
def ingresar_diagnostico(request, orden_id):
    """
    Vista para que el técnico ingrese el diagnóstico
    y tiempo estimado de reparación
    """

    orden = get_object_or_404(OrdenServicio, id=orden_id)

    # Verificar permisos
    perfil = request.user.perfil

    # El técnico solo puede diagnosticar órdenes asignadas a él
    if perfil.tipo_usuario == 'TECNICO':
        # TODO: Obtener técnico del usuario
        # Por ahora permitimos acceso
        pass
    elif not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'No tienes permiso para acceder a esta orden.')
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = DiagnosticoForm(request.POST, instance=orden)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.fecha_diagnostico = timezone.now()
            orden.estado = 'DIAGNOSTICADA'
            orden.save()

            # Notificar al cliente
            try:
                ServicioNotificaciones.notificar_cliente_orden_servicio(orden)
                messages.success(
                    request,
                    f'✅ Diagnóstico guardado y cliente notificado sobre la orden #{orden.numero_orden}.'
                )
            except Exception as e:
                messages.warning(
                    request,
                    f'Diagnóstico guardado pero error al notificar cliente: {str(e)}'
                )

            return redirect('ordenes:detalle', orden_id=orden.id)
    else:
        form = DiagnosticoForm(instance=orden)

    context = {
        'form': form,
        'orden': orden,
    }
    return render(request, 'ordenes/diagnostico.html', context)


@login_required
def mis_ordenes_cliente(request):
    """Vista para que el cliente vea solo sus órdenes"""

    try:
        perfil = request.user.perfil
        if perfil.tipo_usuario != 'CLIENTE':
            messages.error(request, 'Solo los clientes pueden ver sus órdenes.')
            return redirect('dashboard:index')

        cliente = perfil.cliente
        if not cliente:
            messages.error(request, 'No se encontró un cliente asociado a tu usuario.')
            return redirect('dashboard:index')
    except Exception as e:
        messages.error(request, 'Error al obtener información del cliente.')
        return redirect('dashboard:index')

    # Filtros
    estado = request.GET.get('estado', '')

    # Obtener órdenes del cliente
    ordenes = OrdenServicio.objects.filter(cliente=cliente).order_by('-fecha_recepcion')

    if estado:
        ordenes = ordenes.filter(estado=estado)

    # Estadísticas
    total_ordenes = ordenes.count()
    en_proceso = ordenes.filter(
        estado__in=['RECIBIDA', 'EN_DIAGNOSTICO', 'DIAGNOSTICADA', 'EN_REPARACION']
    ).count()
    completadas = ordenes.filter(estado__in=['REPARADA', 'ENTREGADA']).count()

    context = {
        'ordenes': ordenes,
        'cliente': cliente,
        'total_ordenes': total_ordenes,
        'en_proceso': en_proceso,
        'completadas': completadas,
        'estado_filter': estado,
    }
    return render(request, 'ordenes/mis_ordenes_cliente.html', context)


@login_required
def mis_ordenes_tecnico(request):
    """Vista para que el técnico vea solo sus órdenes asignadas"""

    try:
        perfil = request.user.perfil
        if perfil.tipo_usuario != 'TECNICO':
            messages.error(request, 'Solo los técnicos pueden ver sus órdenes asignadas.')
            return redirect('dashboard:index')

        # Obtener técnico asociado al usuario
        # Buscar técnico por email del usuario
        tecnico = Tecnico.objects.filter(correo=request.user.email).first()

        if not tecnico:
            messages.error(request, 'No se encontró un técnico asociado a tu usuario.')
            return redirect('dashboard:index')

    except Exception as e:
        messages.error(request, f'Error al obtener información del técnico: {str(e)}')
        return redirect('dashboard:index')

    # Filtros
    estado = request.GET.get('estado', '')

    # Obtener órdenes asignadas al técnico
    ordenes = OrdenServicio.objects.filter(
        tecnico_asignado=tecnico
    ).order_by('-fecha_recepcion')

    if estado:
        ordenes = ordenes.filter(estado=estado)

    # Estadísticas
    total_ordenes = ordenes.count()
    pendientes = ordenes.filter(estado__in=['RECIBIDA', 'EN_DIAGNOSTICO']).count()
    en_reparacion = ordenes.filter(estado='EN_REPARACION').count()
    completadas = ordenes.filter(estado__in=['REPARADA', 'ENTREGADA']).count()

    context = {
        'ordenes': ordenes,
        'tecnico': tecnico,
        'total_ordenes': total_ordenes,
        'pendientes': pendientes,
        'en_reparacion': en_reparacion,
        'completadas': completadas,
        'estado_filter': estado,
    }
    return render(request, 'ordenes/mis_ordenes_tecnico.html', context)


@login_required
def detalle_orden(request, orden_id):
    """Vista de detalle de orden con control de permisos"""

    orden = get_object_or_404(OrdenServicio, id=orden_id)

    # Verificar permisos
    perfil = request.user.perfil

    # Cliente solo puede ver sus órdenes
    if perfil.tipo_usuario == 'CLIENTE':
        if orden.cliente != perfil.cliente:
            messages.error(request, 'No tienes permiso para ver esta orden.')
            return redirect('ordenes:mis_ordenes_cliente')

    # Técnico solo puede ver órdenes asignadas a él
    elif perfil.tipo_usuario == 'TECNICO':
        tecnico = Tecnico.objects.filter(correo=request.user.email).first()
        if not tecnico or orden.tecnico_asignado != tecnico:
            messages.error(request, 'No tienes permiso para ver esta orden.')
            return redirect('ordenes:mis_ordenes_tecnico')

    # Admin puede ver todo
    elif not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'No tienes permiso para ver esta orden.')
        return redirect('dashboard:index')

    # Obtener seguimientos
    seguimientos = orden.seguimientos.all().order_by('-fecha')

    # Obtener repuestos
    repuestos = orden.repuestos.all()

    context = {
        'orden': orden,
        'seguimientos': seguimientos,
        'repuestos': repuestos,
        'puede_diagnosticar': (
            perfil.tipo_usuario == 'TECNICO' or
            request.user.is_staff or
            request.user.is_superuser
        ),
    }
    return render(request, 'ordenes/detalle.html', context)

