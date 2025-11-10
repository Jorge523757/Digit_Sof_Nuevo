"""
DIGT SOFT - Vistas del Módulo de Productos
CRUD Completo: Crear, Leer, Actualizar, Eliminar
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Producto, CategoriaProducto, MovimientoInventario
from .forms import ProductoForm, BuscarProductoForm, MovimientoInventarioForm


def productos_lista(request):
    """RF2: Lista de productos con búsqueda y filtros"""
    form = BuscarProductoForm(request.GET or None)
    productos = Producto.objects.select_related('categoria').all()

    # Aplicar filtros
    if form.is_valid():
        busqueda = form.cleaned_data.get('busqueda')
        categoria = form.cleaned_data.get('categoria')
        estado = form.cleaned_data.get('estado')

        if busqueda:
            productos = productos.filter(
                Q(nombre_producto__icontains=busqueda) |
                Q(codigo_sku__icontains=busqueda) |
                Q(marca__icontains=busqueda) |
                Q(modelo_equipo__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )

        if categoria:
            productos = productos.filter(categoria=categoria)

        if estado == 'activo':
            productos = productos.filter(activo=True)
        elif estado == 'inactivo':
            productos = productos.filter(activo=False)
        elif estado == 'bajo_stock':
            productos = [p for p in productos if p.necesita_reposicion]
        elif estado == 'sin_stock':
            productos = productos.filter(stock_actual=0)

    # Paginación
    paginator = Paginator(productos, 12)  # 12 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Estadísticas
    total_productos = Producto.objects.count()
    productos_activos = Producto.objects.filter(activo=True).count()
    bajo_stock = len([p for p in Producto.objects.all() if p.necesita_reposicion])
    sin_stock = Producto.objects.filter(stock_actual=0).count()

    context = {
        'page_obj': page_obj,
        'form': form,
        'total_productos': total_productos,
        'productos_activos': productos_activos,
        'bajo_stock': bajo_stock,
        'sin_stock': sin_stock,
    }

    return render(request, 'productos/lista.html', context)


def producto_crear(request):
    """RF1: Crear nuevo producto"""
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'✅ Producto "{producto.nombre_producto}" creado exitosamente.')
            return redirect('productos:detalle', pk=producto.pk)
    else:
        form = ProductoForm()

    context = {
        'form': form,
        'titulo': 'Registrar Nuevo Producto',
        'accion': 'Crear'
    }
    return render(request, 'productos/form.html', context)


def producto_editar(request, pk):
    """RF3: Editar producto existente"""
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'✅ Producto "{producto.nombre_producto}" actualizado correctamente.')
            return redirect('productos:detalle', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)

    context = {
        'form': form,
        'producto': producto,
        'titulo': f'Editar Producto: {producto.nombre_producto}',
        'accion': 'Actualizar'
    }
    return render(request, 'productos/form.html', context)


def producto_detalle(request, pk):
    """Detalle completo de un producto"""
    producto = get_object_or_404(Producto, pk=pk)
    movimientos = producto.movimientos.all()[:10]  # Últimos 10 movimientos

    context = {
        'producto': producto,
        'movimientos': movimientos,
    }
    return render(request, 'productos/detalle.html', context)


def producto_eliminar(request, pk):
    """RF4: Eliminar producto"""
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        nombre = producto.nombre_producto
        producto.delete()
        messages.success(request, f'🗑️ Producto "{nombre}" eliminado correctamente.')
        return redirect('productos:lista')

    context = {
        'producto': producto
    }
    return render(request, 'productos/eliminar.html', context)


def movimiento_inventario(request, pk):
    """Registrar movimiento de inventario"""
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = MovimientoInventarioForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.stock_anterior = producto.stock_actual

            # Actualizar stock según tipo de movimiento
            if movimiento.tipo_movimiento in ['ENTRADA', 'DEVOLUCION']:
                producto.stock_actual += movimiento.cantidad
            elif movimiento.tipo_movimiento in ['SALIDA', 'AJUSTE']:
                producto.stock_actual -= movimiento.cantidad

            movimiento.stock_nuevo = producto.stock_actual
            producto.save()
            movimiento.save()

            messages.success(request, f'✅ Movimiento de inventario registrado correctamente.')
            return redirect('productos:detalle', pk=producto.pk)
    else:
        form = MovimientoInventarioForm(initial={'producto': producto})

    context = {
        'form': form,
        'producto': producto,
    }
    return render(request, 'productos/movimiento.html', context)


def productos_bajo_stock(request):
    """Lista de productos que necesitan reposición"""
    productos = [p for p in Producto.objects.filter(activo=True) if p.necesita_reposicion]

    context = {
        'productos': productos,
        'titulo': 'Productos con Bajo Stock'
    }
    return render(request, 'productos/bajo_stock.html', context)


def producto_toggle_estado(request, pk):
    """Activar/Desactivar producto"""
    producto = get_object_or_404(Producto, pk=pk)
    producto.activo = not producto.activo
    producto.save()

    estado = "activado" if producto.activo else "desactivado"
    messages.success(request, f'✅ Producto "{producto.nombre_producto}" {estado} correctamente.')
    return redirect('productos:lista')

