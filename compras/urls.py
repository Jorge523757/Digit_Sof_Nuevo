"""
DIGT SOFT - URLs del Módulo de Compras
"""

from django.urls import path
from . import views

app_name = 'compras'

urlpatterns = [
    path('', views.compras_lista, name='lista'),
    path('crear/', views.compra_crear, name='crear'),
    path('<int:pk>/', views.compra_detalle, name='detalle'),
    path('<int:pk>/editar/', views.compra_editar, name='editar'),
    path('<int:pk>/eliminar/', views.compra_eliminar, name='eliminar'),
]
"""
DIGT SOFT - Vistas del Módulo de Compras
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .models import Compra, DetalleCompra
from .forms import CompraForm, BuscarCompraForm


def compras_lista(request):
    """Lista de compras"""
    form = BuscarCompraForm(request.GET or None)
    compras = Compra.objects.select_related('proveedor').all()

    if form.is_valid():
        busqueda = form.cleaned_data.get('busqueda')
        estado = form.cleaned_data.get('estado')
        proveedor = form.cleaned_data.get('proveedor')

        if busqueda:
            compras = compras.filter(
                Q(numero_compra__icontains=busqueda) |
                Q(proveedor__nombre_empresa__icontains=busqueda)
            )
        if estado:
            compras = compras.filter(estado=estado)
        if proveedor:
            compras = compras.filter(proveedor=proveedor)

    paginator = Paginator(compras, 20)
    page_obj = paginator.get_page(request.GET.get('page'))

    # Estadísticas
    total_compras = Compra.objects.count()
    pendientes = Compra.objects.filter(estado='PENDIENTE').count()
    completadas = Compra.objects.filter(estado='COMPLETADA').count()
    total_gastado = Compra.objects.filter(estado='COMPLETADA').aggregate(
        total=Sum('total')
    )['total'] or 0

    context = {
        'page_obj': page_obj,
        'form': form,
        'total_compras': total_compras,
        'pendientes': pendientes,
        'completadas': completadas,
        'total_gastado': total_gastado,
    }
    return render(request, 'compras/lista.html', context)


def compra_crear(request):
    """Crear nueva compra"""
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            messages.success(request, f'✅ Compra "{compra.numero_compra}" creada exitosamente.')
            return redirect('compras:detalle', pk=compra.pk)
    else:
        form = CompraForm()

    return render(request, 'compras/form.html', {
        'form': form,
        'titulo': 'Registrar Nueva Compra',
        'accion': 'Crear'
    })


def compra_detalle(request, pk):
    """Ver detalle de compra"""
    compra = get_object_or_404(Compra, pk=pk)
    detalles = compra.items.select_related('producto').all()

    return render(request, 'compras/detalle.html', {
        'compra': compra,
        'detalles': detalles,
    })


def compra_editar(request, pk):
    """Editar compra"""
    compra = get_object_or_404(Compra, pk=pk)

    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            compra = form.save()
            messages.success(request, f'✅ Compra actualizada correctamente.')
            return redirect('compras:detalle', pk=compra.pk)
    else:
        form = CompraForm(instance=compra)

    return render(request, 'compras/form.html', {
        'form': form,
        'compra': compra,
        'titulo': 'Editar Compra',
        'accion': 'Actualizar'
    })


def compra_eliminar(request, pk):
    """Eliminar compra"""
    compra = get_object_or_404(Compra, pk=pk)

    if request.method == 'POST':
        numero = compra.numero_compra
        compra.delete()
        messages.success(request, f'✅ Compra "{numero}" eliminada correctamente.')
        return redirect('compras:lista')

    return render(request, 'compras/eliminar.html', {'compra': compra})

