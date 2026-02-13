"""
DIGIT SOFT - Vistas de Reportes para Órdenes de Servicio
Vistas para generar y descargar reportes personalizados
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from datetime import datetime

from .reportes import GeneradorReportesOrdenes
from .models import OrdenServicio
from clientes.models import Cliente
from tecnicos.models import Tecnico


@login_required
def reportes_ordenes(request):
    """Vista principal de reportes con formulario de filtros"""

    # Solo admin y staff pueden generar reportes
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, '❌ No tienes permisos para generar reportes.')
        return redirect('dashboard:index')

    # Obtener datos para los filtros
    clientes = Cliente.objects.filter(activo=True).order_by('nombres')
    tecnicos = Tecnico.objects.filter(activo=True, eliminado=False).order_by('nombres')

    # Estados correctos del modelo OrdenServicio
    estados = [
        ('RECIBIDA', 'Recibida'),
        ('EN_DIAGNOSTICO', 'En Diagnóstico'),
        ('DIAGNOSTICADA', 'Diagnosticada'),
        ('EN_REPARACION', 'En Reparación'),
        ('REPARADA', 'Reparada'),
        ('EN_ESPERA_REPUESTOS', 'Esperando Repuestos'),
        ('EN_ESPERA_CLIENTE', 'Esperando Cliente'),
        ('LISTA_ENTREGA', 'Lista para Entrega'),
        ('ENTREGADA', 'Entregada'),
        ('CANCELADA', 'Cancelada'),
    ]

    prioridades = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('URGENTE', 'Urgente'),
    ]

    context = {
        'clientes': clientes,
        'tecnicos': tecnicos,
        'estados': estados,
        'prioridades': prioridades,
    }

    return render(request, 'ordenes/reportes/index.html', context)


@login_required
def generar_reporte_excel(request):
    """Generar y descargar reporte en Excel"""

    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, '❌ No tienes permisos para generar reportes.')
        return redirect('dashboard:index')

    # Obtener filtros del request
    filtros = _obtener_filtros_request(request)

    try:
        # Generar reporte
        generador = GeneradorReportesOrdenes()
        excel_file = generador.generar_excel(filtros, incluir_estadisticas=True)

        # Preparar respuesta
        response = HttpResponse(
            excel_file.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        fecha_actual = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'reporte_ordenes_{fecha_actual}.xlsx'
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response

    except Exception as e:
        messages.error(request, f'Error al generar el reporte Excel: {str(e)}')
        return redirect('ordenes:reportes')


@login_required
def generar_reporte_pdf(request):
    """Generar y descargar reporte en PDF"""

    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, '❌ No tienes permisos para generar reportes.')
        return redirect('dashboard:index')

    # Obtener filtros del request
    filtros = _obtener_filtros_request(request)

    try:
        # Generar reporte
        generador = GeneradorReportesOrdenes()
        orientacion = request.GET.get('orientacion', 'portrait')
        pdf_file = generador.generar_pdf(filtros, orientacion=orientacion)

        # Preparar respuesta
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')

        fecha_actual = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'reporte_ordenes_{fecha_actual}.pdf'
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response

    except ImportError:
        messages.error(
            request,
            '❌ La librería ReportLab no está instalada. '
            'Por favor, ejecuta: pip install reportlab'
        )
        return redirect('ordenes:reportes')

    except Exception as e:
        messages.error(request, f'Error al generar el reporte PDF: {str(e)}')
        return redirect('ordenes:reportes')


def _obtener_filtros_request(request):
    """Extraer filtros del request"""
    filtros = {}

    # Fechas
    if request.GET.get('fecha_desde'):
        filtros['fecha_desde'] = request.GET.get('fecha_desde')

    if request.GET.get('fecha_hasta'):
        filtros['fecha_hasta'] = request.GET.get('fecha_hasta')

    # Estado
    if request.GET.get('estado'):
        filtros['estado'] = request.GET.get('estado')

    # Prioridad
    if request.GET.get('prioridad'):
        filtros['prioridad'] = request.GET.get('prioridad')

    # Cliente
    if request.GET.get('cliente_id'):
        filtros['cliente_id'] = request.GET.get('cliente_id')

    # Técnico
    if request.GET.get('tecnico_id'):
        filtros['tecnico_id'] = request.GET.get('tecnico_id')

    # Tipo de equipo
    if request.GET.get('tipo_equipo'):
        filtros['tipo_equipo'] = request.GET.get('tipo_equipo')

    return filtros


@login_required
def vista_previa_reportes(request):
    """API para vista previa de resultados"""

    if not (request.user.is_staff or request.user.is_superuser):
        return JsonResponse({'error': 'Sin permisos'}, status=403)

    # Obtener filtros
    filtros = _obtener_filtros_request(request)

    try:
        # Generar reporte
        generador = GeneradorReportesOrdenes()
        ordenes = generador.filtrar_ordenes(filtros)

        # Limitar a 50 para vista previa
        ordenes_preview = ordenes[:50]

        # Preparar datos
        ordenes_data = []
        for orden in ordenes_preview:
            # Nombre completo del cliente
            cliente_nombre = 'N/A'
            if orden.cliente:
                cliente_nombre = f"{orden.cliente.nombres} {orden.cliente.apellidos}".strip()

            # Nombre completo del técnico
            tecnico_nombre = 'Sin asignar'
            if orden.tecnico_asignado:
                tecnico_nombre = f"{orden.tecnico_asignado.nombres} {orden.tecnico_asignado.apellidos}".strip()

            ordenes_data.append({
                'numero_orden': orden.numero_orden,
                'fecha': orden.fecha_recepcion.strftime('%d/%m/%Y') if orden.fecha_recepcion else '',
                'cliente': cliente_nombre,
                'tecnico': tecnico_nombre,
                'equipo': f"{orden.tipo_equipo} {orden.marca} {orden.modelo}".strip(),
                'estado': orden.get_estado_display(),
                'prioridad': orden.get_prioridad_display(),
                'costo': float(orden.costo_total) if orden.costo_total else 0,
            })

        # Estadísticas
        total = ordenes.count()

        return JsonResponse({
            'success': True,
            'total': total,
            'mostrando': len(ordenes_preview),
            'ordenes': ordenes_data
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

