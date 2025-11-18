from django.shortcuts import render
from productos.models import Producto, CategoriaProducto

def index(request):
    """Vista principal de productos para ecommerce"""
    # Obtener productos activos y disponibles para web
    productos = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        stock_actual__gt=0
    ).select_related('categoria')
    
    # Obtener categorías activas que tienen productos
    categorias = CategoriaProducto.objects.filter(
        activo=True,
        productos__activo=True,
        productos__disponible_web=True
    ).distinct()
    
    # Productos destacados
    productos_destacados = productos.filter(destacado=True)[:4]
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'productos_destacados': productos_destacados,
        'total_productos': productos.count(),
    }
    
    return render(request, 'main/productos/productos.html', context)

