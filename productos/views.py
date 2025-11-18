"""
DIGT SOFT - Vistas del Módulo de Productos
CRUD Completo: Crear, Leer, Actualizar, Eliminar
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Producto, CategoriaProducto, MovimientoInventario, ReaccionProducto
from .forms import ProductoForm, BuscarProductoForm, MovimientoInventarioForm
from usuarios.decorators import staff_required


@login_required
@staff_required
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


@login_required
@staff_required
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


@login_required
@staff_required
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


@login_required
@staff_required
def producto_detalle(request, pk):
    """Detalle completo de un producto"""
    producto = get_object_or_404(Producto, pk=pk)
    movimientos = producto.movimientos.all()[:10]  # Últimos 10 movimientos

    context = {
        'producto': producto,
        'movimientos': movimientos,
    }
    return render(request, 'productos/detalle.html', context)


@login_required
@staff_required
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


@login_required
@staff_required
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


@login_required
@staff_required
def productos_bajo_stock(request):
    """Lista de productos que necesitan reposición"""
    productos = [p for p in Producto.objects.filter(activo=True) if p.necesita_reposicion]

    context = {
        'productos': productos,
        'titulo': 'Productos con Bajo Stock'
    }
    return render(request, 'productos/bajo_stock.html', context)


@login_required
@staff_required
def producto_toggle_estado(request, pk):
    """Activar/Desactivar producto"""
    producto = get_object_or_404(Producto, pk=pk)
    producto.activo = not producto.activo
    producto.save()

    estado = "activado" if producto.activo else "desactivado"
    messages.success(request, f'✅ Producto "{producto.nombre_producto}" {estado} correctamente.')
    return redirect('productos:lista')


def api_productos_publicos(request):
    """API para obtener productos públicos para el landing page"""
    categoria_filter = request.GET.get('categoria', 'all')

    # Filtrar productos activos y disponibles para web
    productos = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    ).select_related('categoria')

    # Filtrar por categoría si no es "all"
    if categoria_filter != 'all':
        productos = productos.filter(categoria__nombre__icontains=categoria_filter)

    # Convertir a lista de diccionarios
    productos_data = []
    for producto in productos[:20]:  # Limitar a 20 productos
        productos_data.append({
            'id': producto.id,
            'nombre': producto.nombre_producto,
            'codigo': producto.codigo_sku,
            'categoria': producto.categoria.nombre if producto.categoria else 'Sin categoría',
            'marca': producto.marca or 'Sin marca',
            'procesador': producto.procesador or '',
            'memoria_ram': producto.memoria_ram or '',
            'memoria_rom': producto.memoria_rom or '',
            'descripcion': producto.descripcion or '',
            'precio': float(producto.precio_venta),
            'precio_mayorista': float(producto.precio_mayorista) if producto.precio_mayorista else None,
            'stock': producto.stock_actual,
            'imagen': producto.imagen.url if producto.imagen else None,
            'destacado': producto.destacado,
        })

    return JsonResponse({
        'success': True,
        'productos': productos_data,
        'total': len(productos_data)
    })


@csrf_exempt
def api_reaccion_producto(request):
    """API para registrar reacciones (me gusta/no me gusta) de productos"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Método no permitido'})

    try:
        data = json.loads(request.body)
        producto_id = data.get('producto_id')
        tipo = data.get('tipo')  # 'like' o 'dislike'

        if not producto_id or not tipo:
            return JsonResponse({'success': False, 'error': 'Datos incompletos'})

        if tipo not in ['like', 'dislike']:
            return JsonResponse({'success': False, 'error': 'Tipo de reacción inválido'})

        producto = get_object_or_404(Producto, pk=producto_id)

        # Identificar usuario o sesión
        if request.user.is_authenticated:
            usuario = request.user
            session_id = None
        else:
            usuario = None
            if not request.session.session_key:
                request.session.create()
            session_id = request.session.session_key

        # Buscar reacción existente
        if usuario:
            reaccion = ReaccionProducto.objects.filter(producto=producto, usuario=usuario).first()
        else:
            reaccion = ReaccionProducto.objects.filter(producto=producto, session_id=session_id).first()

        if reaccion:
            if reaccion.tipo == tipo:
                # Si es la misma reacción, eliminarla (toggle)
                reaccion.delete()
                mensaje = 'Reacción eliminada'
            else:
                # Si es diferente, cambiarla
                reaccion.tipo = tipo
                reaccion.save()
                mensaje = f'Reacción actualizada a {tipo}'
        else:
            # Crear nueva reacción
            ReaccionProducto.objects.create(
                producto=producto,
                usuario=usuario,
                session_id=session_id,
                tipo=tipo
            )
            mensaje = f'Reacción {tipo} agregada'

        # Obtener contadores actualizados
        contadores = ReaccionProducto.obtener_contadores(producto_id)

        return JsonResponse({
            'success': True,
            'mensaje': mensaje,
            'contadores': contadores
        })

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def producto_detalle_publico(request, pk):
    """Vista pública del detalle de un producto"""
    producto = get_object_or_404(Producto, pk=pk, activo=True, disponible_web=True)

    # Obtener contadores de reacciones
    contadores = ReaccionProducto.obtener_contadores(pk)

    # Obtener reacción del usuario actual si existe
    reaccion_usuario = None
    if request.user.is_authenticated:
        reaccion = ReaccionProducto.objects.filter(producto=producto, usuario=request.user).first()
        if reaccion:
            reaccion_usuario = reaccion.tipo
    else:
        if request.session.session_key:
            reaccion = ReaccionProducto.objects.filter(producto=producto, session_id=request.session.session_key).first()
            if reaccion:
                reaccion_usuario = reaccion.tipo

    # Productos relacionados (misma categoría)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        activo=True,
        disponible_web=True
    ).exclude(id=producto.id)[:4]

    context = {
        'producto': producto,
        'contadores': contadores,
        'reaccion_usuario': reaccion_usuario,
        'productos_relacionados': productos_relacionados,
    }

    return render(request, 'productos/detalle_publico.html', context)


# =======================
# VISTAS DEL E-COMMERCE
# =======================

def productos_ecommerce(request):
    """Vista principal del catálogo de productos estilo AliExpress"""
    productos = Producto.objects.filter(activo=True, disponible_web=True)

    # Obtener parámetros de filtrado
    categoria = request.GET.get('categoria')
    busqueda = request.GET.get('q')
    orden = request.GET.get('orden', 'nombre')

    # Filtros
    if categoria and categoria != 'todas':
        productos = productos.filter(categoria__nombre__icontains=categoria)

    if busqueda:
        productos = productos.filter(
            Q(nombre_producto__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(marca__icontains=busqueda)
        )

    # Ordenamiento
    if orden == 'precio_asc':
        productos = productos.order_by('precio_venta')
    elif orden == 'precio_desc':
        productos = productos.order_by('-precio_venta')
    elif orden == 'fecha':
        productos = productos.order_by('-fecha_creacion')
    elif orden == 'stock':
        productos = productos.order_by('-stock_actual')
    else:
        productos = productos.order_by('nombre_producto')

    # Paginación
    paginator = Paginator(productos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Categorías para el filtro
    categorias = CategoriaProducto.objects.all()

    context = {
        'productos': page_obj,
        'categorias': categorias,
        'categoria_actual': categoria,
        'busqueda_actual': busqueda,
        'orden_actual': orden,
        'total_productos': productos.count(),
    }

    return render(request, 'ecommerce/productos.html', context)


def producto_detalle_ecommerce(request, producto_id):
    """Vista de detalle de producto para ecommerce"""
    producto = get_object_or_404(Producto, id=producto_id, activo=True, disponible_web=True)

    # Productos relacionados
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        activo=True,
        disponible_web=True
    ).exclude(id=producto.id)[:4]

    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
    }

    return render(request, 'ecommerce/producto_detalle.html', context)


def obtener_carrito(request):
    """Obtener carrito de la sesión"""
    carrito = request.session.get('carrito', {})
    return carrito


def guardar_carrito(request, carrito):
    """Guardar carrito en la sesión"""
    request.session['carrito'] = carrito
    request.session.modified = True


def calcular_total_carrito(carrito):
    """Calcular total del carrito"""
    total = 0
    for item in carrito.values():
        total += item['precio'] * item['cantidad']
    return total


def ver_carrito(request):
    """Vista del carrito de compras"""
    carrito = obtener_carrito(request)
    productos_carrito = []
    total = 0

    for producto_id, item in carrito.items():
        try:
            producto = Producto.objects.get(id=producto_id, activo=True)
            productos_carrito.append({
                'producto': producto,
                'cantidad': item['cantidad'],
                'subtotal': item['precio'] * item['cantidad']
            })
            total += item['precio'] * item['cantidad']
        except Producto.DoesNotExist:
            continue

    context = {
        'productos_carrito': productos_carrito,
        'total': total,
        'cantidad_items': len(productos_carrito)
    }

    return render(request, 'ecommerce/carrito.html', context)


@csrf_exempt
def agregar_al_carrito(request):
    """Agregar producto al carrito via AJAX"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Método no permitido'})

    try:
        data = json.loads(request.body)
        producto_id = str(data.get('producto_id'))
        cantidad = int(data.get('cantidad', 1))

        producto = get_object_or_404(Producto, id=producto_id, activo=True)

        # Verificar stock disponible
        carrito = obtener_carrito(request)
        cantidad_actual = carrito.get(producto_id, {}).get('cantidad', 0)
        nueva_cantidad = cantidad_actual + cantidad

        if nueva_cantidad > producto.stock_actual:
            return JsonResponse({
                'success': False,
                'error': f'Stock insuficiente. Disponible: {producto.stock_actual}'
            })

        # Agregar o actualizar producto en carrito
        if producto_id in carrito:
            carrito[producto_id]['cantidad'] = nueva_cantidad
        else:
            carrito[producto_id] = {
                'nombre': producto.nombre_producto,
                'precio': float(producto.precio_venta),
                'cantidad': cantidad
            }

        guardar_carrito(request, carrito)

        # Calcular totales
        total_items = sum(item['cantidad'] for item in carrito.values())
        total_precio = calcular_total_carrito(carrito)

        return JsonResponse({
            'success': True,
            'message': f'✅ {producto.nombre_producto} agregado al carrito',
            'total_items': total_items,
            'total_precio': total_precio
        })

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@csrf_exempt
def actualizar_carrito(request):
    """Actualizar cantidad de producto en carrito"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Método no permitido'})

    try:
        data = json.loads(request.body)
        producto_id = str(data.get('producto_id'))
        nueva_cantidad = int(data.get('cantidad'))

        if nueva_cantidad <= 0:
            return JsonResponse({'success': False, 'error': 'Cantidad inválida'})

        producto = get_object_or_404(Producto, id=producto_id, activo=True)

        # Verificar stock
        if nueva_cantidad > producto.stock_actual:
            return JsonResponse({
                'success': False,
                'error': f'Stock insuficiente. Disponible: {producto.stock_actual}'
            })

        carrito = obtener_carrito(request)

        if producto_id in carrito:
            carrito[producto_id]['cantidad'] = nueva_cantidad
            guardar_carrito(request, carrito)

            # Calcular nuevos totales
            subtotal = carrito[producto_id]['precio'] * nueva_cantidad
            total_precio = calcular_total_carrito(carrito)
            total_items = sum(item['cantidad'] for item in carrito.values())

            return JsonResponse({
                'success': True,
                'subtotal': subtotal,
                'total_precio': total_precio,
                'total_items': total_items
            })
        else:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado en carrito'})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@csrf_exempt
def eliminar_del_carrito(request):
    """Eliminar producto del carrito"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Método no permitido'})

    try:
        data = json.loads(request.body)
        producto_id = str(data.get('producto_id'))

        carrito = obtener_carrito(request)

        if producto_id in carrito:
            nombre_producto = carrito[producto_id]['nombre']
            del carrito[producto_id]
            guardar_carrito(request, carrito)

            # Calcular nuevos totales
            total_precio = calcular_total_carrito(carrito)
            total_items = sum(item['cantidad'] for item in carrito.values())

            return JsonResponse({
                'success': True,
                'message': f'✅ {nombre_producto} eliminado del carrito',
                'total_precio': total_precio,
                'total_items': total_items
            })
        else:
            return JsonResponse({'success': False, 'error': 'Producto no encontrado en carrito'})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@csrf_exempt
def limpiar_carrito(request):
    """Limpiar todo el carrito"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Método no permitido'})

    try:
        request.session['carrito'] = {}
        request.session.modified = True

        return JsonResponse({
            'success': True,
            'message': '✅ Carrito vaciado correctamente',
            'total_items': 0,
            'total_precio': 0
        })

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


