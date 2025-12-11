"""DIGIT SOFT - Vistas Facturación"""
from django.shortcuts import render, get_object_or_404
from .models import Factura

def facturas_lista(request):
    facturas = Factura.objects.select_related('cliente').all()
    return render(request, 'facturacion/lista.html', {'facturas': facturas})

def factura_detalle(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    return render(request, 'facturacion/detalle.html', {'factura': factura})
