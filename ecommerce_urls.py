"""
URLs del E-commerce
"""
from django.urls import path
from productos import views as productos_views

app_name = 'ecommerce'

urlpatterns = [
    # Catálogo de productos
    path('', productos_views.productos_ecommerce, name='productos'),
    path('producto/<int:producto_id>/', productos_views.producto_detalle_ecommerce, name='producto_detalle'),

    # Carrito de compras
    path('carrito/', productos_views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/', productos_views.agregar_al_carrito, name='agregar_carrito'),
    path('carrito/actualizar/', productos_views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/', productos_views.eliminar_del_carrito, name='eliminar_carrito'),
    path('carrito/limpiar/', productos_views.limpiar_carrito, name='limpiar_carrito'),
]
