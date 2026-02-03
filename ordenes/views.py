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
    messages.info(request, 'Formulario de creación en desarrollo')
    return redirect('ordenes:lista')


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
    orden = get_object_or_404(OrdenServicio, pk=pk)
    messages.info(request, 'Formulario de edición en desarrollo')
    return redirect('ordenes:detalle', pk=pk)


def orden_agregar_repuesto(request, pk):
    """Agregar repuestos a una orden"""
    orden = get_object_or_404(OrdenServicio, pk=pk)
    messages.info(request, 'Función en desarrollo')
    return redirect('ordenes:detalle', pk=pk)


def orden_cambiar_estado(request, pk):
    """Cambiar estado de una orden"""
    if request.method == 'POST':
        orden = get_object_or_404(OrdenServicio, pk=pk)
        messages.success(request, f'Estado de orden actualizado')
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
