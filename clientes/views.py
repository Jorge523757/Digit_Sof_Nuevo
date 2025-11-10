"""
DIGT SOFT - Módulo de Clientes
Views - HU1: Gestión de Clientes (RF1-RF4)
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Cliente
from .forms import ClienteForm


@login_required
def lista_clientes(request):
    """RF2: BUSCAR CLIENTES - Lista todos los clientes con búsqueda dinámica y filtros"""
    # Obtener parámetros de búsqueda
    query = request.GET.get('q', '').strip()
    documento = request.GET.get('documento', '').strip()
    estado = request.GET.get('estado', '')

    # Iniciar con todos los clientes
    clientes = Cliente.objects.all()

    # Aplicar filtro de búsqueda general
    if query:
        if len(query) >= 2:  # Validación: mínimo 2 caracteres
            clientes = clientes.filter(
                Q(nombres__icontains=query) |
                Q(apellidos__icontains=query) |
                Q(numero_documento__icontains=query) |
                Q(correo__icontains=query) |
                Q(telefono__icontains=query) |
                Q(direccion__icontains=query)
            )
        else:
            messages.warning(request, 'La búsqueda debe tener al menos 2 caracteres.')

    # Aplicar filtro por documento específico
    if documento:
        if documento.isdigit():  # Validación: solo números
            clientes = clientes.filter(numero_documento__icontains=documento)
        else:
            messages.error(request, 'El número de documento debe contener solo números.')

    # Aplicar filtro por estado
    if estado:
        if estado == 'activo':
            clientes = clientes.filter(activo=True)
        elif estado == 'inactivo':
            clientes = clientes.filter(activo=False)

    # Ordenar por fecha de registro (más recientes primero)
    clientes = clientes.order_by('-fecha_registro')

    context = {
        'clientes': clientes,
        'query': query,
        'documento': documento,
        'estado': estado,
    }
    return render(request, 'clientes/lista.html', context)


@login_required
def crear_cliente(request):
    """RF1: REGISTRAR CLIENTE - Crear un nuevo cliente"""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f'Cliente {cliente.nombre_completo} registrado exitosamente.')
            return redirect('clientes:lista')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = ClienteForm()

    context = {
        'form': form,
        'accion': 'Registrar',
    }
    return render(request, 'clientes/form.html', context)


@login_required
def editar_cliente(request, pk):
    """RF3: MODIFICAR DATOS DEL CLIENTE - Editar cliente existente"""
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente {cliente.nombre_completo} actualizado exitosamente.')
            return redirect('clientes:lista')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'form': form,
        'cliente': cliente,
        'accion': 'Editar',
    }
    return render(request, 'clientes/form.html', context)


@login_required
def eliminar_cliente(request, pk):
    """RF4: ELIMINAR CLIENTE - Eliminar cliente de la base de datos"""
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        nombre_completo = cliente.nombre_completo
        cliente.delete()
        messages.success(request, f'Cliente {nombre_completo} eliminado exitosamente.')
        return redirect('clientes:lista')

    context = {
        'cliente': cliente,
    }
    return render(request, 'clientes/eliminar.html', context)


@login_required
def detalle_cliente(request, pk):
    """Ver detalles completos de un cliente"""
    cliente = get_object_or_404(Cliente, pk=pk)

    context = {
        'cliente': cliente,
    }
    return render(request, 'clientes/detalle.html', context)


# Alias para compatibilidad
index = lista_clientes

