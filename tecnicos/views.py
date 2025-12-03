"""
DIGT SOFT - Módulo de Técnicos
Views - Vistas para gestión de técnicos
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Tecnico
from .forms import TecnicoForm, TecnicoBusquedaForm


def lista_tecnicos(request):
    """
    Vista para listar técnicos con búsqueda y filtros
    """
    form_busqueda = TecnicoBusquedaForm(request.GET)
    tecnicos = Tecnico.objects.all()

    # Aplicar filtros de búsqueda
    if form_busqueda.is_valid():
        busqueda = form_busqueda.cleaned_data.get('busqueda')
        estado = form_busqueda.cleaned_data.get('estado')

        if busqueda:
            tecnicos = tecnicos.filter(
                Q(nombres__icontains=busqueda) |
                Q(apellidos__icontains=busqueda) |
                Q(numero_documento__icontains=busqueda) |
                Q(telefono__icontains=busqueda) |
                Q(correo__icontains=busqueda) |
                Q(profesion__icontains=busqueda)
            )

        if estado == 'activo':
            tecnicos = tecnicos.filter(activo=True)
        elif estado == 'inactivo':
            tecnicos = tecnicos.filter(activo=False)

    # Paginación
    paginator = Paginator(tecnicos, 10)
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


def crear_tecnico(request):
    """
    Vista para crear un nuevo técnico
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


def editar_tecnico(request, pk):
    """
    Vista para editar un técnico existente
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


def detalle_tecnico(request, pk):
    """
    Vista para ver el detalle de un técnico
    """
    tecnico = get_object_or_404(Tecnico, pk=pk)

    context = {
        'tecnico': tecnico
    }

    return render(request, 'tecnicos/detalle.html', context)


def eliminar_tecnico(request, pk):
    """
    Vista para eliminar un técnico
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


def buscar_tecnico(request):
    """
    Vista para búsqueda de técnicos (AJAX)
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

