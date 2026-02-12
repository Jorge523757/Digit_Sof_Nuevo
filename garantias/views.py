"""
DIGT SOFT - Vistas del Módulo de Garantías
CRUD Completo: Crear, Leer, Actualizar, Eliminar
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import date, timedelta
from .models import Garantia, SeguimientoGarantia
from .forms import GarantiaForm, BuscarGarantiaForm


@login_required
def garantias_lista(request):
    """RF2: Lista de garantías con búsqueda y filtros - FILTRADA POR ROL"""
    form = BuscarGarantiaForm(request.GET or None)

    # FILTRO DE PRIVACIDAD POR ROL
    if request.user.is_staff or request.user.is_superuser:
        # Admin ve todas las garantías
        garantias = Garantia.objects.select_related('producto', 'cliente').all()
    else:
        # Cliente solo ve SUS garantías
        try:
            from clientes.models import Cliente
            cliente = Cliente.objects.filter(correo=request.user.email).first()

            if cliente:
                garantias = Garantia.objects.filter(cliente=cliente).select_related('producto', 'cliente')
            else:
                garantias = Garantia.objects.none()
        except Exception as e:
            garantias = Garantia.objects.none()

    # Aplicar filtros
    if form.is_valid():
        busqueda = form.cleaned_data.get('busqueda')
        estado = form.cleaned_data.get('estado')
        vigencia = form.cleaned_data.get('vigencia')

        if busqueda:
            garantias = garantias.filter(
                Q(id__icontains=busqueda) |
                Q(nombre_producto__icontains=busqueda) |
                Q(nombre_comprador__icontains=busqueda) |
                Q(cedula__icontains=busqueda) |
                Q(numero_serie__icontains=busqueda) |
                Q(factura_compra__icontains=busqueda)
            )

        if estado:
            garantias = garantias.filter(estado=estado)

        if vigencia == 'vigente':
            garantias = garantias.filter(fecha_vencimiento__gte=date.today(), estado='ACTIVA')
        elif vigencia == 'vencidas':
            garantias = garantias.filter(fecha_vencimiento__lt=date.today())
        elif vigencia == 'por_vencer':
            fecha_limite = date.today() + timedelta(days=30)
            garantias = garantias.filter(
                fecha_vencimiento__gte=date.today(),
                fecha_vencimiento__lte=fecha_limite,
                estado='ACTIVA'
            )

    # Paginación
    paginator = Paginator(garantias, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Estadísticas según el rol
    if request.user.is_staff or request.user.is_superuser:
        # Admin ve estadísticas globales
        total_garantias = Garantia.objects.count()
        activas = Garantia.objects.filter(estado='ACTIVA', fecha_vencimiento__gte=date.today()).count()
        vencidas = Garantia.objects.filter(fecha_vencimiento__lt=date.today()).count()
        en_revision = Garantia.objects.filter(estado='EN_REVISION').count()
    else:
        # Cliente ve solo sus estadísticas
        total_garantias = garantias.count()
        activas = garantias.filter(estado='ACTIVA', fecha_vencimiento__gte=date.today()).count()
        vencidas = garantias.filter(fecha_vencimiento__lt=date.today()).count()
        en_revision = garantias.filter(estado='EN_REVISION').count()

    context = {
        'page_obj': page_obj,
        'form': form,
        'total_garantias': total_garantias,
        'activas': activas,
        'vencidas': vencidas,
        'en_revision': en_revision,
    }

    return render(request, 'garantias/lista.html', context)


@login_required
def garantia_crear(request):
    """RF1: Registrar nueva garantía"""
    if request.method == 'POST':
        form = GarantiaForm(request.POST)
        if form.is_valid():
            garantia = form.save()

            # Crear seguimiento inicial
            SeguimientoGarantia.objects.create(
                garantia=garantia,
                estado_anterior='',
                estado_nuevo=garantia.estado,
                comentarios='Garantía registrada en el sistema',
                usuario=request.user.username if request.user.is_authenticated else 'Sistema'
            )

            messages.success(request, f'✅ Garantía registrada exitosamente. ID: {garantia.id}')
            return redirect('garantias:detalle', pk=garantia.pk)
    else:
        form = GarantiaForm()

    context = {
        'form': form,
        'titulo': 'Registrar Nueva Garantía',
        'accion': 'Crear'
    }
    return render(request, 'garantias/form.html', context)


@login_required
def garantia_editar(request, pk):
    """Editar garantía existente"""
    garantia = get_object_or_404(Garantia, pk=pk)
    estado_anterior = garantia.estado

    if request.method == 'POST':
        form = GarantiaForm(request.POST, instance=garantia)
        if form.is_valid():
            garantia = form.save()

            # Si cambió el estado, crear seguimiento
            if estado_anterior != garantia.estado:
                SeguimientoGarantia.objects.create(
                    garantia=garantia,
                    estado_anterior=estado_anterior,
                    estado_nuevo=garantia.estado,
                    comentarios=f'Estado actualizado de {estado_anterior} a {garantia.estado}',
                    usuario=request.user.username if request.user.is_authenticated else 'Sistema'
                )

            messages.success(request, f'✅ Garantía #{garantia.id} actualizada correctamente.')
            return redirect('garantias:detalle', pk=garantia.pk)
    else:
        form = GarantiaForm(instance=garantia)

    context = {
        'form': form,
        'garantia': garantia,
        'titulo': f'Editar Garantía #{garantia.id}',
        'accion': 'Actualizar'
    }
    return render(request, 'garantias/form.html', context)


@login_required
def garantia_detalle(request, pk):
    """Detalle completo de una garantía con control de acceso"""
    garantia = get_object_or_404(Garantia, pk=pk)

    # Verificar permisos
    if not request.user.is_staff and not request.user.is_superuser:
        try:
            from clientes.models import Cliente
            cliente = Cliente.objects.filter(correo=request.user.email).first()

            if not cliente or garantia.cliente != cliente:
                messages.error(request, 'No tienes permiso para ver esta garantía.')
                return redirect('garantias:lista')
        except:
            messages.error(request, 'No tienes permiso para ver esta garantía.')
            return redirect('garantias:lista')

    seguimientos = garantia.seguimientos.all()

    context = {
        'garantia': garantia,
        'seguimientos': seguimientos,
    }
    return render(request, 'garantias/detalle.html', context)


@login_required
def garantia_eliminar(request, pk):
    """RF3: Eliminar garantía"""
    garantia = get_object_or_404(Garantia, pk=pk)

    if request.method == 'POST':
        garantia_id = garantia.id

        # Verificar si requiere permiso del fabricante
        if garantia.estado in ['EN_REVISION', 'APROBADA']:
            messages.warning(request, '⚠️ Esta garantía está en proceso. Requiere autorización del fabricante.')
            return redirect('garantias:detalle', pk=pk)

        garantia.delete()
        messages.success(request, f'🗑️ Garantía #{garantia_id} eliminada correctamente.')
        return redirect('garantias:lista')

    context = {
        'garantia': garantia
    }
    return render(request, 'garantias/eliminar.html', context)


@login_required
def garantia_buscar(request):
    """RF2: Buscar garantía por múltiples criterios"""
    garantias = []
    busqueda_realizada = False

    if request.GET:
        form = BuscarGarantiaForm(request.GET)
        if form.is_valid():
            busqueda_realizada = True
            busqueda = form.cleaned_data.get('busqueda')

            if busqueda:
                garantias = Garantia.objects.filter(
                    Q(id__icontains=busqueda) |
                    Q(nombre_producto__icontains=busqueda) |
                    Q(cedula__icontains=busqueda) |
                    Q(numero_serie__icontains=busqueda) |
                    Q(factura_compra__icontains=busqueda)
                )
    else:
        form = BuscarGarantiaForm()

    context = {
        'form': form,
        'garantias': garantias,
        'busqueda_realizada': busqueda_realizada,
    }
    return render(request, 'garantias/buscar.html', context)


@login_required
def garantias_por_vencer(request):
    """Lista de garantías próximas a vencer (30 días)"""
    fecha_limite = date.today() + timedelta(days=30)
    garantias = Garantia.objects.filter(
        estado='ACTIVA',
        fecha_vencimiento__gte=date.today(),
        fecha_vencimiento__lte=fecha_limite
    ).order_by('fecha_vencimiento')

    context = {
        'garantias': garantias,
        'titulo': 'Garantías por Vencer (30 días)'
    }
    return render(request, 'garantias/por_vencer.html', context)


@login_required
def garantias_vencidas(request):
    """Lista de garantías vencidas"""
    garantias = Garantia.objects.filter(
        fecha_vencimiento__lt=date.today()
    ).order_by('-fecha_vencimiento')

    context = {
        'garantias': garantias,
        'titulo': 'Garantías Vencidas'
    }
    return render(request, 'garantias/vencidas.html', context)

