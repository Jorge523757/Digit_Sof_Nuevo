"""
DIGIT SOFT - Vistas del E-commerce
Integración con módulo productos
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
import json

from productos.models import Producto, CategoriaProducto
from main.models import Cart, CartItem


def productos_ecommerce(request):
    """Vista principal del e-commerce mostrando productos"""
    # Filtros
    categoria_id = request.GET.get('categoria')
    buscar = request.GET.get('q')
    ordenar = request.GET.get('orden', 'nombre')

    # Query base - solo productos activos y disponibles en web
    productos = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0  # Solo productos con stock
    )

    # Aplicar filtros
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    if buscar:
        productos = productos.filter(
            Q(nombre_producto__icontains=buscar) |
            Q(descripcion__icontains=buscar) |
            Q(marca__icontains=buscar) |
            Q(modelo_equipo__icontains=buscar)
        )

    # Ordenamiento
    orden_map = {
        'nombre': 'nombre_producto',
        'precio_asc': 'precio_venta',
        'precio_desc': '-precio_venta',
        'nuevo': '-fecha_registro',
        'stock': '-stock_actual'
    }
    productos = productos.order_by(orden_map.get(ordenar, 'nombre_producto'))

    # Paginación
    paginator = Paginator(productos, 12)  # 12 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Obtener categorías para filtros
    categorias = CategoriaProducto.objects.filter(activo=True)

    # Productos destacados
    productos_destacados = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        destacado=True,
        stock_actual__gt=0
    )[:6]

    # Contar items en carrito si está autenticado
    cart_count = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_count = cart.total_items
        except Cart.DoesNotExist:
            cart_count = 0

    context = {
        'page_obj': page_obj,
        'productos': page_obj.object_list,
        'productos_destacados': productos_destacados,
        'categorias': categorias,
        'categoria_actual': categoria_id,
        'buscar': buscar,
        'ordenar': ordenar,
        'cart_count': cart_count,
        'total_productos': paginator.count,
    }

    return render(request, 'ecommerce/productos.html', context)


def producto_detalle(request, producto_id):
    """Vista detalle de un producto"""
    producto = get_object_or_404(
        Producto,
        id=producto_id,
        activo=True,
        disponible_web=True
    )

    # Productos relacionados (misma categoría)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    ).exclude(id=producto.id)[:4]

    # Verificar si está en el carrito
    en_carrito = False
    cantidad_en_carrito = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.get(cart=cart, product=producto)
            en_carrito = True
            cantidad_en_carrito = cart_item.quantity
        except (Cart.DoesNotExist, CartItem.DoesNotExist):
            pass

    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'en_carrito': en_carrito,
        'cantidad_en_carrito': cantidad_en_carrito,
    }

    return render(request, 'ecommerce/producto_detalle.html', context)


@csrf_exempt
def agregar_al_carrito(request):
    """Vista AJAX para agregar productos al carrito"""
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'message': 'Debes iniciar sesión para agregar productos al carrito',
            'redirect': '/login/'
        })

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            producto_id = data.get('producto_id')
            cantidad = int(data.get('cantidad', 1))

            # Verificar producto
            producto = get_object_or_404(
                Producto,
                id=producto_id,
                activo=True,
                disponible_web=True
            )

            # Verificar stock
            if producto.stock_actual < cantidad:
                return JsonResponse({
                    'success': False,
                    'message': f'Stock insuficiente. Solo disponibles: {producto.stock_actual}'
                })

            # Obtener o crear carrito
            cart, created = Cart.objects.get_or_create(user=request.user)

            # Obtener o crear item del carrito
            cart_item, item_created = CartItem.objects.get_or_create(
                cart=cart,
                product=producto,
                defaults={'quantity': cantidad}
            )

            if not item_created:
                # Verificar que no exceda el stock disponible
                nueva_cantidad = cart_item.quantity + cantidad
                if nueva_cantidad > producto.stock_actual:
                    return JsonResponse({
                        'success': False,
                        'message': f'Stock insuficiente. Stock disponible: {producto.stock_actual}, tienes {cart_item.quantity} en el carrito'
                    })

                cart_item.quantity = nueva_cantidad
                cart_item.save()
                mensaje = f'{producto.nombre_producto} cantidad actualizada en el carrito'
            else:
                mensaje = f'{producto.nombre_producto} agregado al carrito'

            # Actualizar totales del carrito
            cart.updated_at = timezone.now()
            cart.save()

            return JsonResponse({
                'success': True,
                'message': mensaje,
                'cart_count': cart.total_items,
                'cart_total': float(cart.total_price),
                'item_quantity': cart_item.quantity
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error al agregar al carrito: {str(e)}'
            })

    return JsonResponse({'success': False, 'message': 'Método no permitido'})


@login_required
def ver_carrito(request):
    """Vista del carrito de compras"""
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.get_items()

        # Verificar disponibilidad y stock de cada item
        items_con_problemas = []
        for item in cart_items:
            if not item.product.activo or not item.product.disponible_web:
                items_con_problemas.append({
                    'item': item,
                    'problema': 'Producto ya no disponible'
                })
            elif item.quantity > item.product.stock_actual:
                items_con_problemas.append({
                    'item': item,
                    'problema': f'Stock insuficiente (disponible: {item.product.stock_actual})'
                })

    except Cart.DoesNotExist:
        cart = None
        cart_items = []
        items_con_problemas = []

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'items_con_problemas': items_con_problemas,
    }

    return render(request, 'ecommerce/carrito.html', context)


@csrf_exempt
@login_required
def actualizar_carrito(request):
    """Vista AJAX para actualizar cantidad en carrito"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            nueva_cantidad = int(data.get('cantidad'))

            cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

            if nueva_cantidad <= 0:
                cart_item.delete()
                mensaje = 'Producto eliminado del carrito'
            else:
                # Verificar stock
                if nueva_cantidad > cart_item.product.stock_actual:
                    return JsonResponse({
                        'success': False,
                        'message': f'Stock insuficiente. Disponible: {cart_item.product.stock_actual}'
                    })

                cart_item.quantity = nueva_cantidad
                cart_item.save()
                mensaje = 'Cantidad actualizada'

            # Recalcular totales
            try:
                cart = Cart.objects.get(user=request.user)
                cart_count = cart.total_items
                cart_total = float(cart.total_price)
            except Cart.DoesNotExist:
                cart_count = 0
                cart_total = 0

            return JsonResponse({
                'success': True,
                'message': mensaje,
                'cart_count': cart_count,
                'cart_total': cart_total,
                'item_total': float(cart_item.total_price) if nueva_cantidad > 0 else 0
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error: {str(e)}'
            })

    return JsonResponse({'success': False, 'message': 'Método no permitido'})


@csrf_exempt
@login_required
def eliminar_del_carrito(request):
    """Vista AJAX para eliminar producto del carrito"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')

            cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
            producto_nombre = cart_item.product.nombre_producto
            cart_item.delete()

            # Recalcular totales
            try:
                cart = Cart.objects.get(user=request.user)
                cart_count = cart.total_items
                cart_total = float(cart.total_price)
            except Cart.DoesNotExist:
                cart_count = 0
                cart_total = 0

            return JsonResponse({
                'success': True,
                'message': f'{producto_nombre} eliminado del carrito',
                'cart_count': cart_count,
                'cart_total': cart_total
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error: {str(e)}'
            })

    return JsonResponse({'success': False, 'message': 'Método no permitido'})


@login_required
def limpiar_carrito(request):
    """Limpiar todo el carrito"""
    try:
        cart = Cart.objects.get(user=request.user)
        cart.cartitem_set.all().delete()
        messages.success(request, 'Carrito vaciado exitosamente')
    except Cart.DoesNotExist:
        messages.info(request, 'El carrito ya está vacío')

    return redirect('ecommerce:ver_carrito')


def productos_estilo_exito(request):
    """Vista de productos con diseño estilo e-commerce (Éxito/Amazon)"""
    # Filtros
    categorias_seleccionadas = request.GET.getlist('category')
    marcas_seleccionadas = request.GET.getlist('brand')
    buscar = request.GET.get('q')
    ordenar = request.GET.get('orden', 'relevance')
    precio_rango = request.GET.get('precio')

    # Query base - solo productos activos y disponibles en web
    productos = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    )

    # Aplicar filtros
    if categorias_seleccionadas:
        productos = productos.filter(categoria_id__in=categorias_seleccionadas)

    if marcas_seleccionadas:
        productos = productos.filter(marca__in=marcas_seleccionadas)

    if buscar:
        productos = productos.filter(
            Q(nombre_producto__icontains=buscar) |
            Q(descripcion__icontains=buscar) |
            Q(marca__icontains=buscar) |
            Q(modelo_equipo__icontains=buscar)
        )

    # Filtro de precio
    if precio_rango:
        if precio_rango == '0-500000':
            productos = productos.filter(precio_venta__lt=500000)
        elif precio_rango == '500000-1000000':
            productos = productos.filter(precio_venta__gte=500000, precio_venta__lt=1000000)
        elif precio_rango == '1000000-2000000':
            productos = productos.filter(precio_venta__gte=1000000, precio_venta__lt=2000000)
        elif precio_rango == '2000000-':
            productos = productos.filter(precio_venta__gte=2000000)

    # Ordenamiento
    orden_map = {
        'relevance': '-destacado',
        'price_asc': 'precio_venta',
        'price_desc': '-precio_venta',
        'newest': '-fecha_registro',
    }
    productos = productos.order_by(orden_map.get(ordenar, '-destacado'), 'nombre_producto')

    # Obtener categorías para filtros
    categorias = CategoriaProducto.objects.filter(activo=True)

    # Obtener marcas únicas de productos disponibles
    marcas = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    ).values_list('marca', flat=True).distinct().exclude(marca__isnull=True).exclude(marca='')

    context = {
        'productos': productos,
        'categorias': categorias,
        'marcas': sorted(marcas),
        'categorias_seleccionadas': categorias_seleccionadas,
        'marcas_seleccionadas': marcas_seleccionadas,
        'buscar': buscar,
        'ordenar': ordenar,
    }

    return render(request, 'ecommerce/productos_estilo_exito.html', context)
