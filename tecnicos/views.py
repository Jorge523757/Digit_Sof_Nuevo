"""
DIGIT SOFT - Módulo de Técnicos
Views - Vistas para gestión de técnicos con filtros avanzados
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Tecnico
from .forms import TecnicoForm, TecnicoFiltroForm


def es_staff(user):
    """Verifica si el usuario es staff o superusuario"""
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def lista_tecnicos(request):
    """
    Vista para listar técnicos con búsqueda y filtros avanzados
    Solo accesible para staff/admin

    Filtros disponibles:
    - Búsqueda por: ID, teléfono, correo, nombre
    - Estado: Habilitado, Inhabilitado, Eliminado
    """

    # Formulario de filtros
    form_filtro = TecnicoFiltroForm(request.GET or None)

    # Obtener todos los técnicos (incluidos eliminados para admin)
    tecnicos = Tecnico.objects.all().order_by('-fecha_registro')

    # Aplicar filtros
    if form_filtro.is_valid():
        busqueda = form_filtro.cleaned_data.get('busqueda')
        estado = form_filtro.cleaned_data.get('estado')

        # Filtro de búsqueda
        if busqueda:
            tecnicos = tecnicos.filter(
                Q(id__icontains=busqueda) |
                Q(nombres__icontains=busqueda) |
                Q(apellidos__icontains=busqueda) |
                Q(numero_documento__icontains=busqueda) |
                Q(telefono__icontains=busqueda) |
                Q(correo__icontains=busqueda) |
                Q(profesion__icontains=busqueda)
            )

        # Filtro de estado
        if estado == 'habilitado':
            tecnicos = tecnicos.filter(activo=True, eliminado=False)
        elif estado == 'inhabilitado':
            tecnicos = tecnicos.filter(activo=False, eliminado=False)
        elif estado == 'eliminado':
            tecnicos = tecnicos.filter(eliminado=True)

    # Estadísticas
    total_tecnicos = Tecnico.objects.filter(eliminado=False).count()
    habilitados = Tecnico.objects.filter(activo=True, eliminado=False).count()
    inhabilitados = Tecnico.objects.filter(activo=False, eliminado=False).count()
    eliminados = Tecnico.objects.filter(eliminado=True).count()

    # Paginación
    paginator = Paginator(tecnicos, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form_filtro': form_filtro,
        'tecnicos': page_obj,
        'page_obj': page_obj,
        'total_tecnicos': total_tecnicos,
        'habilitados': habilitados,
        'inhabilitados': inhabilitados,
        'eliminados': eliminados,
    }

    return render(request, 'tecnicos/lista.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def crear_tecnico(request):
    """Vista para crear un nuevo técnico"""

    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            tecnico = form.save()
            messages.success(
                request,
                f'✅ Técnico {tecnico.nombre_completo} creado exitosamente.'
            )
            return redirect('tecnicos:detalle', tecnico_id=tecnico.id)
        else:
            messages.error(request, '❌ Por favor corrige los errores en el formulario.')
    else:
        form = TecnicoForm()

    context = {
        'form': form,
        'accion': 'Crear',
    }
    return render(request, 'tecnicos/form.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def editar_tecnico(request, tecnico_id):
    """Vista para editar un técnico existente"""

    tecnico = get_object_or_404(Tecnico, id=tecnico_id)

    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            tecnico = form.save()
            messages.success(
                request,
                f'✅ Técnico {tecnico.nombre_completo} actualizado exitosamente.'
            )
            return redirect('tecnicos:detalle', tecnico_id=tecnico.id)
        else:
            messages.error(request, '❌ Por favor corrige los errores en el formulario.')
    else:
        form = TecnicoForm(instance=tecnico)

    context = {
        'form': form,
        'tecnico': tecnico,
        'accion': 'Editar',
    }
    return render(request, 'tecnicos/form.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def detalle_tecnico(request, tecnico_id):
    """Vista para ver detalle de un técnico"""

    tecnico = get_object_or_404(Tecnico, id=tecnico_id)

    # Obtener órdenes asignadas
    from ordenes.models import OrdenServicio
    ordenes_activas = OrdenServicio.objects.filter(
        tecnico_asignado=tecnico,
        estado__in=['RECIBIDA', 'EN_DIAGNOSTICO', 'DIAGNOSTICADA', 'EN_REPARACION']
    ).count()

    ordenes_completadas = OrdenServicio.objects.filter(
        tecnico_asignado=tecnico,
        estado__in=['REPARADA', 'ENTREGADA']
    ).count()

    total_ordenes = OrdenServicio.objects.filter(tecnico_asignado=tecnico).count()

    context = {
        'tecnico': tecnico,
        'ordenes_activas': ordenes_activas,
        'ordenes_completadas': ordenes_completadas,
        'total_ordenes': total_ordenes,
    }
    return render(request, 'tecnicos/detalle.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def deshabilitar_tecnico(request, tecnico_id):
    """Vista para deshabilitar un técnico (no eliminarlo)"""

    if request.method != 'POST':
        messages.error(request, 'Método no permitido.')
        return redirect('tecnicos:lista')

    tecnico = get_object_or_404(Tecnico, id=tecnico_id)

    if tecnico.eliminado:
        messages.warning(request, 'Este técnico ya está eliminado.')
        return redirect('tecnicos:lista')

    # Cambiar estado activo
    tecnico.activo = not tecnico.activo
    tecnico.save()

    if tecnico.activo:
        messages.success(request, f'✅ Técnico {tecnico.nombre_completo} habilitado.')
    else:
        messages.success(request, f'⚠️ Técnico {tecnico.nombre_completo} inhabilitado.')

    return redirect('tecnicos:detalle', tecnico_id=tecnico.id)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def eliminar_tecnico(request, tecnico_id):
    """Vista para eliminar un técnico (soft delete)"""

    if request.method != 'POST':
        messages.error(request, 'Método no permitido.')
        return redirect('tecnicos:lista')

    tecnico = get_object_or_404(Tecnico, id=tecnico_id)

    if tecnico.eliminado:
        messages.warning(request, 'Este técnico ya está eliminado.')
        return redirect('tecnicos:lista')

    # Obtener motivo de eliminación
    motivo = request.POST.get('motivo', 'Sin motivo especificado')

    # Eliminar lógicamente
    tecnico.eliminar_logicamente(motivo)

    messages.success(
        request,
        f'🗑️ Técnico {tecnico.nombre_completo} eliminado exitosamente.'
    )

    return redirect('tecnicos:lista')


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def restaurar_tecnico(request, tecnico_id):
    """Vista para restaurar un técnico eliminado"""

    if request.method != 'POST':
        messages.error(request, 'Método no permitido.')
        return redirect('tecnicos:lista')

    tecnico = get_object_or_404(Tecnico, id=tecnico_id)

    if not tecnico.eliminado:
        messages.warning(request, 'Este técnico no está eliminado.')
        return redirect('tecnicos:detalle', tecnico_id=tecnico.id)

    # Restaurar
    tecnico.restaurar()

    messages.success(
        request,
        f'✅ Técnico {tecnico.nombre_completo} restaurado exitosamente.'
    )

    return redirect('tecnicos:detalle', tecnico_id=tecnico.id)
    page_number = request.GET.get('page')
    tecnicos_paginados = paginator.get_page(page_number)

    context = {
        'tecnicos': tecnicos_paginados,
        'form_busqueda': form_busqueda,
        'total_tecnicos': tecnicos.count(),
        'tecnicos_activos': Tecnico.objects.filter(activo=True).count(),
        'tecnicos_inactivos': Tecnico.objects.filter(activo=False).count(),
    }

    return render(request, 'tecnicos/lista.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def crear_tecnico(request):
    """
    Vista para crear un nuevo técnico
    Solo accesible para staff/admin
    """
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            tecnico = form.save()
            messages.success(request, f'Técnico {tecnico.nombre_completo} registrado exitosamente.')
            return redirect('tecnicos:lista')
    else:
        form = TecnicoForm()

    context = {
        'form': form,
        'accion': 'Registrar'
    }

    return render(request, 'tecnicos/form.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def editar_tecnico(request, pk):
    """
    Vista para editar un técnico existente
    Solo accesible para staff/admin
    """
    tecnico = get_object_or_404(Tecnico, pk=pk)

    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            tecnico = form.save()
            messages.success(request, f'Técnico {tecnico.nombre_completo} actualizado exitosamente.')
            return redirect('tecnicos:lista')
    else:
        form = TecnicoForm(instance=tecnico)

    context = {
        'form': form,
        'tecnico': tecnico,
        'accion': 'Cambiar'
    }

    return render(request, 'tecnicos/form.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def detalle_tecnico(request, pk):
    """
    Vista para ver el detalle de un técnico
    Solo accesible para staff/admin
    """
    tecnico = get_object_or_404(Tecnico, pk=pk)

    context = {
        'tecnico': tecnico
    }

    return render(request, 'tecnicos/detalle.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def eliminar_tecnico(request, pk):
    """
    Vista para eliminar un técnico
    Solo accesible para staff/admin
    """
    tecnico = get_object_or_404(Tecnico, pk=pk)

    if request.method == 'POST':
        nombre = tecnico.nombre_completo
        tecnico.delete()
        messages.success(request, f'Técnico {nombre} eliminado exitosamente.')
        return redirect('tecnicos:lista')

    context = {
        'tecnico': tecnico
    }

    return render(request, 'tecnicos/eliminar.html', context)


@login_required
@user_passes_test(es_staff, login_url='dashboard:index')
def buscar_tecnico(request):
    """
    Vista para búsqueda de técnicos (AJAX)
    Solo accesible para staff/admin
    """
    if request.method == 'GET':
        busqueda = request.GET.get('busqueda', '')
        tecnicos = Tecnico.objects.filter(
            Q(nombres__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(numero_documento__icontains=busqueda)
        ).filter(activo=True)[:10]

        resultados = [{
            'id': t.id,
            'nombre': t.nombre_completo,
            'documento': t.numero_documento,
            'telefono': t.telefono,
            'profesion': t.profesion
        } for t in tecnicos]

        from django.http import JsonResponse
        return JsonResponse({'tecnicos': resultados})
