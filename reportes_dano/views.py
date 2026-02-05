"""
DIGT SOFT - Vistas para Registro de Daños
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from .models import RegistroDano, ImagenDano
from .forms import RegistroDanoForm
from .services import GeneradorReportePDF, GeneradorReporteExcel
@login_required
def registrar_dano(request):
    equipo_precargado = None
    equipo_id = request.GET.get('equipo_id')
    if equipo_id:
        try:
            from equipos.models import Equipo
            equipo_precargado = Equipo.objects.get(pk=equipo_id)
        except:
            pass
    if request.method == 'POST':
        form = RegistroDanoForm(request.POST)
        if form.is_valid():
            try:
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.numero_factura = f'FD-{timezone.now().strftime("%Y%m%d-%H%M%S")}'

                # Crear orden de servicio automáticamente
                try:
                    from ordenes.models import OrdenServicio
                    from clientes.models import Cliente

                    # Obtener o crear cliente
                    cliente = None
                    try:
                        # Buscar cliente por correo del usuario
                        cliente = Cliente.objects.filter(correo=request.user.email).first()
                        if not cliente:
                            # Si no existe, crear uno nuevo
                            cliente = Cliente.objects.create(
                                nombres=request.user.first_name or request.user.username,
                                apellidos=request.user.last_name or '',
                                numero_documento='TEMP-' + str(request.user.id),
                                telefono='000-0000000',
                                correo=request.user.email or f'{request.user.username}@temp.com',
                                direccion='Por definir'
                            )
                    except Exception as e:
                        messages.warning(request, f'Cliente no encontrado: {str(e)}')
                        cliente = None

                    if cliente:
                        # Crear orden de servicio
                        orden = OrdenServicio.objects.create(
                            cliente=cliente,
                            tipo_equipo=request.POST.get('tipo_equipo', 'Por definir'),
                            marca=request.POST.get('marca', 'Por definir'),
                            modelo=request.POST.get('modelo', 'Por definir'),
                            serie=request.POST.get('serie', ''),
                            falla_reportada=registro.descripcion_dano,
                            estado_fisico='Reportado por cliente con evidencia fotográfica',
                            estado='RECIBIDA',
                            prioridad='MEDIA',
                            fecha_recepcion=timezone.now()
                        )

                        registro.orden = orden
                        messages.info(request, f'Orden de servicio creada: {orden.numero_orden}')

                except Exception as e:
                    messages.warning(request, f'Orden de servicio no creada: {str(e)}')

                registro.save()
                imagenes = request.FILES.getlist('imagenes')
                if imagenes:
                    for idx, imagen in enumerate(imagenes):
                        ImagenDano.objects.create(
                            registro=registro,
                            imagen=imagen,
                            es_principal=(idx == 0)
                        )
                messages.success(request, 'Reporte registrado exitosamente!')
                return redirect('reportes_dano:detalle_reporte', pk=registro.pk)
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
        else:
            messages.error(request, 'Corrija los errores.')
    else:
        form = RegistroDanoForm()
    return render(request, 'reportes_dano/crear_reporte.html', {
        'form': form,
        'equipo_precargado': equipo_precargado,
    })
@login_required
def detalle_reporte(request, pk):
    registro = get_object_or_404(RegistroDano, pk=pk)
    if not request.user.is_staff and registro.usuario != request.user:
        messages.error(request, 'Sin permiso.')
        return redirect('dashboard:inicio')
    return render(request, 'reportes_dano/detalle.html', {
        'registro': registro,
        'imagenes': registro.imagenes.all(),
    })
@login_required
def mis_reportes(request):
    reportes = RegistroDano.objects.filter(usuario=request.user).order_by('-fecha_reporte')
    return render(request, 'reportes_dano/mis_reportes.html', {'reportes': reportes})
@login_required
def descargar_factura(request, pk, tipo='pdf'):
    registro = get_object_or_404(RegistroDano, pk=pk)
    if not request.user.is_staff and registro.usuario != request.user:
        messages.error(request, 'Sin permiso.')
        return redirect('dashboard:inicio')

    try:
        if tipo.lower() == 'pdf':
            # Generar PDF
            buffer = GeneradorReportePDF.generar_reporte_dano(registro)
            response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="reporte_{registro.numero_factura}.pdf"'
            return response

        elif tipo.lower() in ['excel', 'xlsx']:
            # Generar Excel
            buffer = GeneradorReporteExcel.generar_reporte_dano(registro)
            response = HttpResponse(
                buffer.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = f'attachment; filename="reporte_{registro.numero_factura}.xlsx"'
            return response
        else:
            messages.error(request, 'Formato no soportado.')
            return redirect('reportes_dano:detalle_reporte', pk=pk)

    except Exception as e:
        messages.error(request, f'Error al generar reporte: {str(e)}')
        return redirect('reportes_dano:detalle_reporte', pk=pk)
@login_required
def regenerar_factura(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Sin permiso.')
        return redirect('dashboard:inicio')
    messages.info(request, 'Disponible próximamente.')
    return redirect('reportes_dano:detalle_reporte', pk=pk)
@login_required
def lista_reportes_admin(request):
    if not request.user.is_staff:
        messages.error(request, 'Sin permiso.')
        return redirect('dashboard:inicio')
    reportes = RegistroDano.objects.all().order_by('-fecha_reporte')
    return render(request, 'reportes_dano/admin_lista.html', {'reportes': reportes})
@login_required
def marcar_revisado(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Sin permiso.')
        return redirect('dashboard:inicio')
    registro = get_object_or_404(RegistroDano, pk=pk)
    messages.success(request, f'Reporte {registro.numero_factura} marcado.')
    return redirect('reportes_dano:admin_lista')


@login_required
def exportar_reportes_excel(request):
    """Exportar lista de reportes a Excel"""
    if not request.user.is_staff:
        # Exportar solo los reportes del usuario
        reportes = RegistroDano.objects.filter(usuario=request.user).order_by('-fecha_reporte')
        filename = f'mis_reportes_{timezone.now().strftime("%Y%m%d")}.xlsx'
    else:
        # Admin puede exportar todos
        reportes = RegistroDano.objects.all().order_by('-fecha_reporte')
        filename = f'todos_reportes_{timezone.now().strftime("%Y%m%d")}.xlsx'

    try:
        buffer = GeneradorReporteExcel.generar_lista_reportes(reportes)
        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    except Exception as e:
        messages.error(request, f'Error al exportar: {str(e)}')
        if request.user.is_staff:
            return redirect('reportes_dano:admin_lista')
        else:
            return redirect('reportes_dano:mis_reportes')
