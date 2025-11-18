from django.shortcuts import render
from productos.models import Producto, CategoriaProducto

def home(request):
    """Página principal del sistema - Landing Page con productos activos"""
    # Obtener todas las categorías activas que tengan productos activos
    categorias = CategoriaProducto.objects.filter(
        activo=True,
        productos__activo=True,
        productos__disponible_web=True
    ).distinct().order_by('nombre')

    # Crear un diccionario con categorías y sus productos activos
    categorias_con_productos = []
    for categoria in categorias:
        productos = Producto.objects.filter(
            categoria=categoria,
            activo=True,
            disponible_web=True
        ).select_related('categoria')[:8]  # Máximo 8 productos por categoría

        if productos.exists():
            categorias_con_productos.append({
                'categoria': categoria,
                'productos': productos
            })

    context = {
        'categorias_con_productos': categorias_con_productos,
    }
    return render(request, 'core/landing.html', context)


def test_carrito(request):
    """Página de prueba del carrito"""
    return render(request, 'test_carrito_simple.html')


def about(request):
    """Página acerca de"""
    return render(request, 'core/about.html')


