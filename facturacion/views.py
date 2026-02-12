"""DIGIT SOFT - Vistas Facturación"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Factura

@login_required
def facturas_lista(request):
    """Lista de facturas con filtro por rol"""

    # FILTRO DE PRIVACIDAD POR ROL
    if request.user.is_staff or request.user.is_superuser:
        # Admin ve todas las facturas
        facturas = Factura.objects.select_related('cliente').all().order_by('-fecha_emision')
    else:
        # Cliente solo ve SUS facturas
        try:
            from clientes.models import Cliente
            cliente = Cliente.objects.filter(correo=request.user.email).first()

            if cliente:
                facturas = Factura.objects.filter(cliente=cliente).select_related('cliente').order_by('-fecha_emision')
            else:
                facturas = Factura.objects.none()
        except Exception as e:
            facturas = Factura.objects.none()

    return render(request, 'facturacion/lista.html', {'facturas': facturas})

@login_required
def factura_detalle(request, pk):
    """Detalle de factura con control de acceso"""
    factura = get_object_or_404(Factura, pk=pk)

    # Verificar permisos
    if not request.user.is_staff and not request.user.is_superuser:
        try:
            from clientes.models import Cliente
            cliente = Cliente.objects.filter(correo=request.user.email).first()

            if not cliente or factura.cliente != cliente:
                messages.error(request, 'No tienes permiso para ver esta factura.')
                return redirect('facturacion:lista')
        except:
            messages.error(request, 'No tienes permiso para ver esta factura.')
            return redirect('facturacion:lista')

    return render(request, 'facturacion/detalle.html', {'factura': factura})


