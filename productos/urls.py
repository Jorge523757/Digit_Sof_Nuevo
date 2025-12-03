"""
DIGT SOFT - URLs del Módulo de Productos
"""

from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    # API pública
    path('api/publicos/', views.api_productos_publicos, name='api_publicos'),
    path('api/reaccion/', views.api_reaccion_producto, name='api_reaccion'),
    path('detalle/<int:pk>/', views.producto_detalle_publico, name='detalle_publico'),

    # Lista y búsqueda
    path('', views.productos_lista, name='lista'),
    path('bajo-stock/', views.productos_bajo_stock, name='bajo_stock'),

    # CRUD
    path('crear/', views.producto_crear, name='crear'),
    path('<int:pk>/', views.producto_detalle, name='detalle'),
    path('<int:pk>/editar/', views.producto_editar, name='editar'),
    path('<int:pk>/eliminar/', views.producto_eliminar, name='eliminar'),

    # Inventario
    path('<int:pk>/movimiento/', views.movimiento_inventario, name='movimiento'),

    # Acciones
    path('<int:pk>/toggle-estado/', views.producto_toggle_estado, name='toggle_estado'),
]

