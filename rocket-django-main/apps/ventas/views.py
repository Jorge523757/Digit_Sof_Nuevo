from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, ComentarioProducto, Cliente, Venta, DetalleVenta, Pedido, DetallePedido
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from decimal import Decimal
from django.utils import timezone

# Listar productos y buscar
def lista_productos(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.all()
    if query:
        productos = productos.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(marca__icontains=query))
    return render(request, 'ventas/productos.html', {'productos': productos, 'query': query})

# Detalle de producto y comentarios
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    comentarios = ComentarioProducto.objects.filter(producto=producto).order_by('-fecha')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        mensaje = request.POST.get('mensaje')
        if nombre and mensaje:
            ComentarioProducto.objects.create(producto=producto, nombre=nombre, mensaje=mensaje)
            messages.success(request, 'Comentario agregado correctamente.')
            return redirect(reverse('ventas:detalle_producto', args=[pk]))
    return render(request, 'ventas/detalle_producto.html', {'producto': producto, 'comentarios': comentarios})

# CRUD de productos (solo ejemplo, puedes proteger con login_required y permisos)
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria = request.POST.get('categoria')
        marca = request.POST.get('marca')
        imagen = request.FILES.get('imagen')
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, categoria=categoria, marca=marca, imagen=imagen)
        messages.success(request, 'Producto creado correctamente.')
        return redirect('ventas:lista_productos')
    return render(request, 'ventas/crear_producto.html')

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.categoria = request.POST.get('categoria')
        producto.marca = request.POST.get('marca')
        if request.FILES.get('imagen'):
            producto.imagen = request.FILES.get('imagen')
        producto.save()
        messages.success(request, 'Producto actualizado correctamente.')
        return redirect('ventas:lista_productos')
    return render(request, 'ventas/editar_producto.html', {'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente.')
    return redirect('ventas:lista_productos')

# Carrito de compras (versión simple en sesión)
def agregar_al_carrito(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    carrito = request.session.get('carrito', {})
    carrito[str(pk)] = carrito.get(str(pk), 0) + 1
    request.session['carrito'] = carrito
    return JsonResponse({'ok': True, 'cantidad': carrito[str(pk)]})

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0
    for pk, cantidad in carrito.items():
        producto = get_object_or_404(Producto, pk=pk)
        subtotal = producto.precio * cantidad
        productos.append({'producto': producto, 'cantidad': cantidad, 'subtotal': subtotal})
        total += subtotal
    return render(request, 'ventas/carrito.html', {'productos': productos, 'total': total})

def eliminar_del_carrito(request, pk):
    carrito = request.session.get('carrito', {})
    if str(pk) in carrito:
        del carrito[str(pk)]
        request.session['carrito'] = carrito
    return redirect('ventas:ver_carrito')

# Registrar venta y mostrar factura
def registrar_venta(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.error(request, 'El carrito está vacío.')
        return redirect('ventas:lista_productos')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cedula = request.POST.get('cedula')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        metodo_pago = request.POST.get('metodo_pago')
        cliente, _ = Cliente.objects.get_or_create(cedula=cedula, defaults={'nombre': nombre, 'telefono': telefono, 'correo': correo, 'direccion': direccion})
        total = Decimal('0.00')
        venta = Venta.objects.create(cliente=cliente, metodo_pago=metodo_pago, total=0)
        # Validar stock suficiente antes de registrar la venta
        sin_stock = []
        for pk, cantidad in carrito.items():
            producto = get_object_or_404(Producto, pk=pk)
            if cantidad > producto.stock:
                sin_stock.append(f"{producto.nombre} (disponible: {producto.stock})")
        if sin_stock:
            messages.error(request, f"No hay suficiente stock para: {', '.join(sin_stock)}")
            return redirect('ventas:ver_carrito')
        # Si hay stock suficiente, registrar la venta
        for pk, cantidad in carrito.items():
            producto = get_object_or_404(Producto, pk=pk)
            subtotal = producto.precio * cantidad
            DetalleVenta.objects.create(venta=venta, producto=producto, cantidad=cantidad, precio_unitario=producto.precio, subtotal=subtotal)
            producto.stock -= cantidad
            producto.save()
            total += subtotal
        venta.total = total
        venta.save()
        request.session['carrito'] = {}
        return redirect('ventas:factura', venta.pk)
    return render(request, 'ventas/registrar_venta.html')

def factura(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    return render(request, 'ventas/factura.html', {'venta': venta})

# === NUEVAS VISTAS PARA SISTEMA DE PEDIDOS ===

# Vista pública del catálogo para clientes
def catalogo_publico(request):
    """Vista pública donde los clientes pueden ver productos y agregarlos al carrito"""
    query = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')
    productos = Producto.objects.filter(stock__gt=0)  # Solo productos con stock
    
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query) | 
            Q(marca__icontains=query)
        )
    
    if categoria:
        productos = productos.filter(categoria=categoria)
    
    categorias = Producto.objects.values_list('categoria', flat=True).distinct()
    
    return render(request, 'ventas/catalogo_publico.html', {
        'productos': productos,
        'query': query,
        'categoria_seleccionada': categoria,
        'categorias': categorias
    })

# Crear pedido desde carrito
def crear_pedido(request):
    """Permite al cliente crear un pedido desde el carrito"""
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.error(request, 'El carrito está vacío.')
        return redirect('ventas:catalogo_publico')
    
    if request.method == 'POST':
        # Datos del cliente
        nombre = request.POST.get('nombre')
        cedula = request.POST.get('cedula')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion', '')
        notas = request.POST.get('notas', '')
        
        # Crear o actualizar cliente
        cliente, created = Cliente.objects.get_or_create(
            cedula=cedula,
            defaults={
                'nombre': nombre,
                'telefono': telefono,
                'correo': correo,
                'direccion': direccion
            }
        )
        
        # Validar stock antes de crear el pedido
        sin_stock = []
        total = Decimal('0.00')
        
        for pk, cantidad in carrito.items():
            try:
                producto = Producto.objects.get(pk=pk)
                if cantidad > producto.stock:
                    sin_stock.append(f"{producto.nombre} (disponible: {producto.stock})")
                else:
                    total += producto.precio * cantidad
            except Producto.DoesNotExist:
                continue
        
        if sin_stock:
            messages.error(request, f"No hay suficiente stock para: {', '.join(sin_stock)}")
            return redirect('ventas:ver_carrito')
        
        # Crear el pedido
        pedido = Pedido.objects.create(
            cliente=cliente,
            total=total,
            notas_cliente=notas
        )
        
        # Crear los detalles del pedido
        for pk, cantidad in carrito.items():
            try:
                producto = Producto.objects.get(pk=pk)
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio
                )
            except Producto.DoesNotExist:
                continue
        
        # Limpiar carrito
        request.session['carrito'] = {}
        
        messages.success(request, f'Pedido #{pedido.pk} creado correctamente. Será procesado por nuestro equipo.')
        return redirect('ventas:detalle_pedido', pedido.pk)
    
    # Mostrar formulario con datos del carrito
    productos_carrito = []
    total = Decimal('0.00')
    
    for pk, cantidad in carrito.items():
        try:
            producto = Producto.objects.get(pk=pk)
            subtotal = producto.precio * cantidad
            productos_carrito.append({
                'producto': producto,
                'cantidad': cantidad,
                'subtotal': subtotal
            })
            total += subtotal
        except Producto.DoesNotExist:
            continue
    
    return render(request, 'ventas/crear_pedido.html', {
        'productos_carrito': productos_carrito,
        'total': total
    })

# Ver detalle de pedido para cliente
def detalle_pedido(request, pedido_id):
    """Vista para que el cliente vea su pedido"""
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    detalles = DetallePedido.objects.filter(pedido=pedido)
    return render(request, 'ventas/detalle_pedido.html', {
        'pedido': pedido,
        'detalles': detalles
    })

# === VISTAS PARA ADMINISTRADORES ===

# Lista de pedidos para administrador
def admin_pedidos(request):
    """Vista para que los administradores vean todos los pedidos"""
    estado_filtro = request.GET.get('estado', '')
    pedidos = Pedido.objects.all()
    
    if estado_filtro:
        pedidos = pedidos.filter(estado=estado_filtro)
    
    return render(request, 'ventas/admin_pedidos.html', {
        'pedidos': pedidos,
        'estado_filtro': estado_filtro,
        'estados': Pedido.ESTADOS_PEDIDO
    })

# Procesar pedido (cambiar estado)
def procesar_pedido(request, pedido_id):
    """Permite al administrador cambiar el estado del pedido"""
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        procesado_por = request.POST.get('procesado_por', 'Administrador')
        
        pedido.estado = nuevo_estado
        pedido.procesado_por = procesado_por
        pedido.fecha_procesamiento = timezone.now()
        pedido.save()
        
        # Obtener el texto del estado
        estados_dict = dict(Pedido.ESTADOS_PEDIDO)
        estado_texto = estados_dict.get(nuevo_estado, nuevo_estado)
        messages.success(request, f'Pedido #{pedido.pk} actualizado a {estado_texto}')
        return redirect('ventas:admin_pedidos')
    
    detalles = DetallePedido.objects.filter(pedido=pedido)
    return render(request, 'ventas/procesar_pedido.html', {
        'pedido': pedido,
        'detalles': detalles,
        'estados': Pedido.ESTADOS_PEDIDO
    })

# Convertir pedido a factura/venta
def facturar_pedido(request, pedido_id):
    """Convierte un pedido en una venta/factura"""
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    
    if not pedido.puede_ser_facturado():
        messages.error(request, 'Este pedido no puede ser facturado.')
        return redirect('ventas:admin_pedidos')
    
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        procesado_por = request.POST.get('procesado_por', 'Administrador')
        
        # Verificar stock nuevamente
        sin_stock = []
        detalles_pedido = DetallePedido.objects.filter(pedido=pedido)
        for detalle in detalles_pedido:
            if detalle.cantidad > detalle.producto.stock:
                sin_stock.append(f"{detalle.producto.nombre} (disponible: {detalle.producto.stock})")
        
        if sin_stock:
            messages.error(request, f"No hay suficiente stock para: {', '.join(sin_stock)}")
            return redirect('ventas:facturar_pedido', pedido_id)
        
        # Crear la venta
        venta = Venta.objects.create(
            cliente=pedido.cliente,
            metodo_pago=metodo_pago,
            total=pedido.total
        )
        
        # Crear detalles de venta y descontar stock
        detalles_pedido = DetallePedido.objects.filter(pedido=pedido)
        for detalle in detalles_pedido:
            DetalleVenta.objects.create(
                venta=venta,
                producto=detalle.producto,
                cantidad=detalle.cantidad,
                precio_unitario=detalle.precio_unitario,
                subtotal=detalle.subtotal
            )
            
            # Descontar stock
            detalle.producto.stock -= detalle.cantidad
            detalle.producto.save()
        
        # Actualizar pedido
        pedido.estado = 'facturado'
        pedido.procesado_por = procesado_por
        pedido.fecha_procesamiento = timezone.now()
        pedido.save()
        
        messages.success(request, f'Pedido #{pedido.pk} facturado correctamente como Venta #{venta.pk}')
        return redirect('ventas:factura', venta.pk)
    
    detalles = DetallePedido.objects.filter(pedido=pedido)
    return render(request, 'ventas/facturar_pedido.html', {
        'pedido': pedido,
        'detalles': detalles,
        'metodos_pago': Venta._meta.get_field('metodo_pago').choices
    })
