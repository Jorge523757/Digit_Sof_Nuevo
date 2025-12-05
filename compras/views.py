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


# REPORTES PDF Y EXCEL
# ==============================================

from django.contrib.auth.decorators import login_required
from usuarios.decorators import staff_required

@login_required
@staff_required
def compra_reporte_pdf(request):
    """Generar reporte de compras en PDF"""
    from utils.reportes import generar_pdf
    from datetime import datetime

    query = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '')

    datos = Compra.objects.all().select_related('proveedor')

    if query:
        datos = datos.filter(
            Q(numero_compra__icontains=query) |
            Q(proveedor__nombre_empresa__icontains=query)
        )

    if estado:
        datos = datos.filter(estado=estado)

    datos = datos.order_by('-fecha_compra')

    context = {
        'datos': datos,
        'fecha': datetime.now(),
        'usuario': request.user,
        'total': datos.count(),
        'total_gastado': datos.aggregate(Sum('total'))['total__sum'] or 0,
    }

    filename = f'reporte_compras_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    return generar_pdf('reportes/compras_pdf.html', context, filename)


@login_required
@staff_required
def compra_reporte_excel(request):
    """Generar reporte de compras en Excel"""
    from utils.reportes import generar_excel_avanzado
    from datetime import datetime

    query = request.GET.get('q', '').strip()
    estado = request.GET.get('estado', '')

    datos_query = Compra.objects.all().select_related('proveedor')

    if query:
        datos_query = datos_query.filter(
            Q(numero_compra__icontains=query) |
            Q(proveedor__nombre_empresa__icontains=query)
        )

    if estado:
        datos_query = datos_query.filter(estado=estado)

    datos_query = datos_query.order_by('-fecha_compra')

    datos = []
    for item in datos_query:
        datos.append({
            'numero_compra': item.numero_compra,
            'proveedor': str(item.proveedor) if item.proveedor else '',
            'fecha_compra': item.fecha_compra,
            'subtotal': float(item.subtotal),
            'impuestos': float(item.impuestos),
            'total': float(item.total),
            'estado': item.get_estado_display(),
        })

    columnas = [
        ('numero_compra', 'Número Compra', 'texto'),
        ('proveedor', 'Proveedor', 'texto'),
        ('fecha_compra', 'Fecha', 'fecha'),
        ('subtotal', 'Subtotal', 'moneda'),
        ('impuestos', 'Impuestos', 'moneda'),
        ('total', 'Total', 'moneda'),
        ('estado', 'Estado', 'texto'),
    ]

    titulo = 'Reporte de Compras'
    filename = f'reporte_compras_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'

    totales = ['subtotal', 'impuestos', 'total']

    return generar_excel_avanzado(datos, columnas, titulo, filename, totales=totales)
