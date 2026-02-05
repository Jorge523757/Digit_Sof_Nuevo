"""DIGIT SOFT - Vistas Equipos"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Equipo

@login_required
def equipos_lista(request):
    """Lista de equipos - Los clientes solo ven sus equipos"""
    
    if request.user.is_staff or request.user.is_superuser:
        # Staff/Admin ven todos los equipos
        equipos = Equipo.objects.filter(activo=True)
    else:
        # Clientes solo ven sus equipos
        try:
            from clientes.models import Cliente
            cliente = Cliente.objects.filter(correo=request.user.email).first()
            
            if cliente:
                equipos = Equipo.objects.filter(cliente=cliente, activo=True)
            else:
                equipos = Equipo.objects.none()
                messages.info(request, 'No tienes equipos registrados.')
        except Exception as e:
            equipos = Equipo.objects.none()
            messages.warning(request, 'No se pudieron cargar tus equipos.')
    
    return render(request, 'equipos/lista.html', {'equipos': equipos})

@login_required
def equipo_detalle(request, pk):
    """Detalle de equipo - Solo el propietario o staff pueden ver"""
    equipo = get_object_or_404(Equipo, pk=pk)
    
    # Verificar permisos
    if not request.user.is_staff and not request.user.is_superuser:
        try:
            from clientes.models import Cliente
            cliente = Cliente.objects.filter(correo=request.user.email).first()
            
            if not cliente or equipo.cliente != cliente:
                messages.error(request, 'No tienes permiso para ver este equipo.')
                return redirect('equipos:lista')
        except:
            messages.error(request, 'No tienes permiso para ver este equipo.')
            return redirect('equipos:lista')
    
    return render(request, 'equipos/detalle.html', {'equipo': equipo})

