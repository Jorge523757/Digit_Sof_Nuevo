"""
DIGT SOFT - Vistas del Módulo de Órdenes de Servicio
Gestión completa de servicio técnico
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import OrdenServicio, RepuestoOrden, SeguimientoOrden


def ordenes_lista(request):
    """Lista de órdenes con búsqueda y filtros avanzados"""
    ordenes = OrdenServicio.objects.select_related('cliente', 'tecnico_asignado').all().order_by('-fecha_recepcion')

    # Búsqueda simple
    busqueda = request.GET.get('busqueda', '')
    if busqueda:
        ordenes = ordenes.filter(
            Q(numero_orden__icontains=busqueda) |
            Q(cliente__nombres__icontains=busqueda) |
            Q(cliente__apellidos__icontains=busqueda) |
            Q(marca__icontains=busqueda) |
            Q(modelo__icontains=busqueda) |
            Q(tipo_equipo__icontains=busqueda)
        )

    # Filtros avanzados
    estado = request.GET.get('estado', '')
    if estado:
        ordenes = ordenes.filter(estado=estado)

    prioridad = request.GET.get('prioridad', '')
    if prioridad:
        ordenes = ordenes.filter(prioridad=prioridad)

    cliente = request.GET.get('cliente', '')
    if cliente:
        ordenes = ordenes.filter(
            Q(cliente__nombres__icontains=cliente) |
            Q(cliente__apellidos__icontains=cliente)
        )

    tecnico = request.GET.get('tecnico', '')
    if tecnico:
        ordenes = ordenes.filter(
            Q(tecnico_asignado__nombres__icontains=tecnico) |
            Q(tecnico_asignado__apellidos__icontains=tecnico)
        )

    equipo = request.GET.get('equipo', '')
    if equipo:
        ordenes = ordenes.filter(tipo_equipo__icontains=equipo)

    # Filtro por rango de fechas
    fecha_desde = request.GET.get('fecha_desde', '')
    fecha_hasta = request.GET.get('fecha_hasta', '')

    if fecha_desde:
        try:
            from datetime import datetime
            fecha_desde_obj = datetime.strptime(fecha_desde, '%Y-%m-%d')
            ordenes = ordenes.filter(fecha_recepcion__date__gte=fecha_desde_obj.date())
        except ValueError:
            pass

    if fecha_hasta:
        try:
            from datetime import datetime
            fecha_hasta_obj = datetime.strptime(fecha_hasta, '%Y-%m-%d')
            ordenes = ordenes.filter(fecha_recepcion__date__lte=fecha_hasta_obj.date())
        except ValueError:
            pass

    # Paginación
    paginator = Paginator(ordenes, 20)
    page_obj = paginator.get_page(request.GET.get('page'))

    # Estadísticas generales
    total_ordenes = OrdenServicio.objects.count()
    en_proceso = OrdenServicio.objects.filter(
        estado__in=['RECIBIDA', 'EN_DIAGNOSTICO', 'EN_REPARACION']
    ).count()
    listas_entrega = OrdenServicio.objects.filter(estado='LISTA_ENTREGA').count()
    entregadas = OrdenServicio.objects.filter(estado='ENTREGADA').count()

    # Obtener listas para filtros
    from clientes.models import Cliente
    from tecnicos.models import Tecnico
    
    clientes = Cliente.objects.filter(activo=True).order_by('nombres')[:100]
    tecnicos = Tecnico.objects.filter(activo=True).order_by('nombres')[:100]

    context = {
        'page_obj': page_obj,
        'total_ordenes': total_ordenes,
        'en_proceso': en_proceso,
        'listas_entrega': listas_entrega,
        'entregadas': entregadas,
        'busqueda': busqueda,
        'estado': estado,
        'prioridad': prioridad,
        'cliente': cliente,
        'tecnico': tecnico,
        'equipo': equipo,
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'clientes': clientes,
        'tecnicos': tecnicos,
    }

    return render(request, 'ordenes/lista.html', context)


def orden_crear(request):
    """Crear nueva orden de servicio"""
    from .forms import OrdenServicioForm
    from clientes.models import Cliente
    from tecnicos.models import Tecnico
    from .notifications import ServicioNotificaciones

    if request.method == 'POST':
        form = OrdenServicioForm(request.POST)
        if form.is_valid():
            orden = form.save()

            # Crear seguimiento inicial
            SeguimientoOrden.objects.create(
                orden=orden,
                estado_anterior='',
                estado_nuevo='RECIBIDA',
                descripcion=f'Orden creada - Equipo recibido: {orden.tipo_equipo} {orden.marca} {orden.modelo}',
                usuario=request.user.username if request.user.is_authenticated else 'Sistema'
            )

            # NOTIFICAR AL ADMINISTRADOR - NUEVO
            try:
                ServicioNotificaciones.notificar_nueva_orden_admin(orden)
            except Exception as e:
                print(f"Error notificando al administrador: {e}")

            # Crear notificación para el cliente
            try:
                from usuarios.models import Notificacion
                Notificacion.objects.create(
                    tipo='ORDEN_CREADA',
                    titulo=f'Orden {orden.numero_orden} creada',
                    mensaje=f'Su equipo {orden.tipo_equipo} {orden.marca} {orden.modelo} ha sido recibido. Fecha estimada de entrega: {orden.fecha_compromiso.strftime("%d/%m/%Y") if orden.fecha_compromiso else "Por definir"}',
                    url=f'/ordenes/{orden.pk}/',
                    icono='fas fa-tools',
                    color='primary'
                )
            except:
                pass

            # Enviar notificaciones multicanal al cliente
            try:
                from notificaciones.services import ServicioNotificaciones as ServicioNotif
                ServicioNotif.enviar_notificacion(
                    orden=orden,
                    evento='ORDEN_CREADA',
                    destinatario_tipo='CLIENTE',
                    destinatario=orden.cliente
                )
            except Exception as e:
                print(f"Error enviando notificación multicanal: {e}")

            # Si hay técnico asignado, notificarle
            if orden.tecnico_asignado:
                try:
                    from notificaciones.services import ServicioNotificaciones as ServicioNotif, ServicioMonitoreo
                    ServicioNotif.enviar_notificacion(
                        orden=orden,
                        evento='ORDEN_ASIGNADA',
                        destinatario_tipo='TECNICO',
                        destinatario=orden.tecnico_asignado
                    )
                    # Actualizar estado del técnico
                    ServicioMonitoreo.actualizar_estado_tecnico(orden.tecnico_asignado)
                except Exception as e:
                    print(f"Error notificando al técnico: {e}")

            messages.success(request, f'✅ Orden {orden.numero_orden} creada exitosamente')
            return redirect('ordenes:detalle', pk=orden.pk)
    else:
        form = OrdenServicioForm()

    clientes = Cliente.objects.filter(activo=True).order_by('nombres')[:100]
    tecnicos = Tecnico.objects.filter(activo=True).order_by('nombres')[:100]

    context = {
        'form': form,
        'clientes': clientes,
        'tecnicos': tecnicos,
    }
    return render(request, 'ordenes/crear.html', context)


def orden_detalle(request, pk):
    """Ver detalle de una orden"""
    orden = get_object_or_404(OrdenServicio, pk=pk)
    repuestos = orden.repuestos.select_related('producto').all()
    seguimientos = orden.seguimientos.all()[:10]

    context = {
        'orden': orden,
        'repuestos': repuestos,
        'seguimientos': seguimientos,
    }
    return render(request, 'ordenes/detalle.html', context)


def orden_editar(request, pk):
    """Editar orden existente"""
    from .forms import OrdenServicioForm
    from clientes.models import Cliente
    from tecnicos.models import Tecnico
    from .notifications import ServicioNotificaciones

    orden = get_object_or_404(OrdenServicio, pk=pk)
    estado_anterior = orden.estado
    tecnico_anterior = orden.tecnico_asignado

    if request.method == 'POST':
        form = OrdenServicioForm(request.POST, instance=orden)
        if form.is_valid():
            orden = form.save()

            # Si cambió el técnico asignado, notificarle
            if orden.tecnico_asignado and orden.tecnico_asignado != tecnico_anterior:
                try:
                    ServicioNotificaciones.notificar_asignacion_tecnico(orden, orden.tecnico_asignado)
                    messages.success(request, f'✅ Técnico {orden.tecnico_asignado.nombre_completo} notificado')
                except Exception as e:
                    print(f"Error notificando al técnico: {e}")

            # Si cambió el estado, crear seguimiento
            if estado_anterior != orden.estado:
                SeguimientoOrden.objects.create(
                    orden=orden,
                    estado_anterior=estado_anterior,
                    estado_nuevo=orden.estado,
                    descripcion=request.POST.get('descripcion_cambio', f'Estado cambiado de {dict(OrdenServicio.ESTADO_CHOICES).get(estado_anterior)} a {dict(OrdenServicio.ESTADO_CHOICES).get(orden.estado)}'),
                    usuario=request.user.username if request.user.is_authenticated else 'Sistema'
                )

                # Notificar cambio de estado
                try:
                    from usuarios.models import Notificacion
                    Notificacion.objects.create(
                        tipo='CAMBIO_ESTADO_ORDEN',
                        titulo=f'Actualización Orden {orden.numero_orden}',
                        mensaje=f'El estado de su equipo {orden.tipo_equipo} cambió a: {dict(OrdenServicio.ESTADO_CHOICES).get(orden.estado)}',
                        url=f'/ordenes/{orden.pk}/',
                        icono='fas fa-sync-alt',
                        color='info'
                    )
                except:
                    pass

            messages.success(request, f'✅ Orden {orden.numero_orden} actualizada exitosamente')
            return redirect('ordenes:detalle', pk=pk)
    else:
        form = OrdenServicioForm(instance=orden)

    clientes = Cliente.objects.filter(activo=True).order_by('nombres')[:100]
    tecnicos = Tecnico.objects.filter(activo=True).order_by('nombres')[:100]

    context = {
        'form': form,
        'orden': orden,
        'clientes': clientes,
        'tecnicos': tecnicos,
    }
    return render(request, 'ordenes/editar.html', context)


def orden_agregar_repuesto(request, pk):
    """Agregar repuestos a una orden"""
    orden = get_object_or_404(OrdenServicio, pk=pk)
    messages.info(request, 'Función en desarrollo')
    return redirect('ordenes:detalle', pk=pk)


def orden_cambiar_estado(request, pk):
    """Cambiar estado de una orden"""
    from .notifications import ServicioNotificaciones

    if request.method == 'POST':
        orden = get_object_or_404(OrdenServicio, pk=pk)
        estado_anterior = orden.estado
        nuevo_estado = request.POST.get('estado')
        descripcion = request.POST.get('descripcion', '')

        if nuevo_estado and nuevo_estado in dict(OrdenServicio.ESTADO_CHOICES):
            orden.estado = nuevo_estado
            orden.save()

            # Crear seguimiento
            SeguimientoOrden.objects.create(
                orden=orden,
                estado_anterior=estado_anterior,
                estado_nuevo=nuevo_estado,
                descripcion=descripcion or f'Estado cambiado de {dict(OrdenServicio.ESTADO_CHOICES).get(estado_anterior)} a {dict(OrdenServicio.ESTADO_CHOICES).get(nuevo_estado)}',
                usuario=request.user.username if request.user.is_authenticated else 'Sistema'
            )

            # NOTIFICAR AL CLIENTE - EMAIL + IN-APP
            try:
                ServicioNotificaciones.notificar_cambio_estado_cliente(
                    orden,
                    estado_anterior,
                    nuevo_estado,
                    descripcion
                )
            except Exception as e:
                print(f"Error notificando al cliente: {e}")

            # Si el estado es LISTA_ENTREGA, enviar notificación especial
            if nuevo_estado == 'LISTA_ENTREGA':
                try:
                    ServicioNotificaciones.notificar_orden_lista_entrega(orden)
                except Exception as e:
                    print(f"Error enviando notificación de orden lista: {e}")

            # Enviar notificación in-app
            try:
                from usuarios.models import Notificacion
                estado_nombre = dict(OrdenServicio.ESTADO_CHOICES).get(nuevo_estado)

                # Mensajes personalizados según el estado
                if nuevo_estado == 'LISTA_ENTREGA':
                    mensaje = f'¡Buenas noticias! Su equipo {orden.tipo_equipo} está listo para ser retirado.'
                    icono = 'fas fa-check-circle'
                    color = 'success'
                elif nuevo_estado == 'EN_REPARACION':
                    mensaje = f'Su equipo {orden.tipo_equipo} está siendo reparado por nuestros técnicos.'
                    icono = 'fas fa-tools'
                    color = 'warning'
                elif nuevo_estado == 'ENTREGADA':
                    mensaje = f'Su equipo {orden.tipo_equipo} ha sido entregado. ¡Gracias por confiar en nosotros!'
                    icono = 'fas fa-handshake'
                    color = 'success'
                else:
                    mensaje = f'El estado de su equipo {orden.tipo_equipo} cambió a: {estado_nombre}'
                    icono = 'fas fa-sync-alt'
                    color = 'info'

                Notificacion.objects.create(
                    tipo='CAMBIO_ESTADO_ORDEN',
                    titulo=f'Orden {orden.numero_orden} - {estado_nombre}',
                    mensaje=mensaje,
                    url=f'/ordenes/{orden.pk}/',
                    icono=icono,
                    color=color
                )
            except Exception as e:
                print(f"Error al crear notificación: {e}")

            messages.success(request, f'✅ Estado actualizado a: {dict(OrdenServicio.ESTADO_CHOICES).get(nuevo_estado)}')
        else:
            messages.error(request, '❌ Estado inválido')

        return redirect('ordenes:detalle', pk=pk)

    return redirect('ordenes:lista')


def ordenes_tablero(request):
    """Tablero kanban de órdenes"""
    ordenes_por_estado = {}

    for estado_code, estado_nombre in OrdenServicio.ESTADO_CHOICES:
        ordenes_por_estado[estado_code] = OrdenServicio.objects.filter(
            estado=estado_code
        ).select_related('cliente', 'tecnico_asignado')[:10]

    context = {
        'ordenes_por_estado': ordenes_por_estado,
        'estados': OrdenServicio.ESTADO_CHOICES,
    }

    return render(request, 'ordenes/tablero.html', context)


def tecnico_notificar_actualizacion(request, pk):
    """
    Vista para que el técnico notifique demoras, adelantos o incidencias al administrador
    """
    from .notifications import ServicioNotificaciones
    from datetime import datetime

    orden = get_object_or_404(OrdenServicio, pk=pk)

    # Verificar que el usuario sea técnico asignado o admin
    if not request.user.is_staff:
        # Verificar si es el técnico asignado
        try:
            from tecnicos.models import Tecnico
            tecnico = Tecnico.objects.get(usuario=request.user)
            if orden.tecnico_asignado != tecnico:
                messages.error(request, '❌ No tienes permiso para notificar esta orden')
                return redirect('ordenes:detalle', pk=pk)
        except:
            messages.error(request, '❌ No tienes permiso para acceder a esta función')
            return redirect('ordenes:lista')

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        mensaje = request.POST.get('mensaje')
        nueva_fecha_str = request.POST.get('nueva_fecha')

        nueva_fecha = None
        if nueva_fecha_str:
            try:
                nueva_fecha = datetime.strptime(nueva_fecha_str, '%Y-%m-%d').date()
                # Si hay nueva fecha, actualizar la orden
                orden.fecha_compromiso = nueva_fecha
                orden.save()
            except:
                pass

        # Obtener el técnico
        try:
            from tecnicos.models import Tecnico
            if request.user.is_staff:
                tecnico = orden.tecnico_asignado
            else:
                tecnico = Tecnico.objects.get(usuario=request.user)
        except:
            messages.error(request, '❌ Error al identificar el técnico')
            return redirect('ordenes:detalle', pk=pk)

        # Registrar en el seguimiento
        SeguimientoOrden.objects.create(
            orden=orden,
            estado_anterior=orden.estado,
            estado_nuevo=orden.estado,
            descripcion=f'[{tipo}] {mensaje}',
            usuario=request.user.username
        )

        # Notificar al administrador
        try:
            ServicioNotificaciones.notificar_tecnico_a_admin(
                orden,
                tecnico,
                tipo,
                mensaje,
                nueva_fecha
            )
            messages.success(request, f'✅ Notificación de {tipo.lower()} enviada al administrador')
        except Exception as e:
            messages.error(request, f'❌ Error al enviar notificación: {e}')

        return redirect('ordenes:detalle', pk=pk)

    context = {
        'orden': orden,
    }
    return render(request, 'ordenes/notificar_tecnico.html', context)


# API para autocompletado
from django.http import JsonResponse

def api_clientes_autocomplete(request):
    """API para autocompletar clientes"""
    term = request.GET.get('term', '')

    if len(term) < 2:
        return JsonResponse([], safe=False)

    from clientes.models import Cliente

    clientes = Cliente.objects.filter(
        Q(nombres__icontains=term) |
        Q(apellidos__icontains=term) |
        Q(numero_documento__icontains=term)
    ).filter(activo=True)[:10]

    results = [
        {
            'id': cliente.id,
            'value': cliente.nombre_completo,
            'label': f"{cliente.nombre_completo} - {cliente.numero_documento}",
            'documento': cliente.numero_documento,
            'telefono': cliente.telefono,
            'correo': cliente.correo,
        }
        for cliente in clientes
    ]

    return JsonResponse(results, safe=False)


def api_tecnicos_autocomplete(request):
    """API para autocompletar técnicos"""
    term = request.GET.get('term', '')

    if len(term) < 2:
        return JsonResponse([], safe=False)

    from tecnicos.models import Tecnico

    tecnicos = Tecnico.objects.filter(
        Q(nombres__icontains=term) |
        Q(apellidos__icontains=term) |
        Q(numero_documento__icontains=term)
    ).filter(activo=True)[:10]

    results = [
        {
            'id': tecnico.id,
            'value': tecnico.nombre_completo,
            'label': f"{tecnico.nombre_completo} - {tecnico.profesion}",
            'documento': tecnico.numero_documento,
            'telefono': tecnico.telefono,
        }
        for tecnico in tecnicos
    ]

    return JsonResponse(results, safe=False)
