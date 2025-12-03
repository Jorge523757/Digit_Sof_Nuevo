from django.shortcuts import render
from productos.models import Producto, CategoriaProducto

def home(request):
    """Página principal del sistema - Landing Page con productos destacados"""

    # Obtener productos destacados (máximo 6 para la página principal)
    productos_destacados = Producto.objects.filter(
        activo=True,
        disponible_web=True,
        destacado=True
    ).select_related('categoria').order_by('-fecha_registro')[:6]

    # Si no hay productos destacados, mostrar los más recientes
    if not productos_destacados.exists():
        productos_destacados = Producto.objects.filter(
            activo=True,
            disponible_web=True
        ).select_related('categoria').order_by('-fecha_registro')[:6]

    # Obtener todas las categorías activas
    categorias = CategoriaProducto.objects.filter(
        activo=True,
        productos__activo=True,
        productos__disponible_web=True
    ).distinct().order_by('nombre')

    # Contar total de productos disponibles
    total_productos = Producto.objects.filter(
        activo=True,
        disponible_web=True
    ).count()

    context = {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
        'total_productos': total_productos,
    }
    return render(request, 'core/home.html', context)


def test_carrito(request):
    """Página de prueba del carrito"""
    return render(request, 'test_carrito_simple.html')


def about(request):
    """Página acerca de"""
    return render(request, 'core/about.html')


