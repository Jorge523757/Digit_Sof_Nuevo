"""
DIGT SOFT - URLs del Módulo de Proveedores
"""

from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    # Lista y búsqueda
    path('', views.proveedores_lista, name='lista'),

    # CRUD
    path('crear/', views.proveedor_crear, name='crear'),
    path('<int:pk>/', views.proveedor_detalle, name='detalle'),
    path('<int:pk>/editar/', views.proveedor_editar, name='editar'),
    path('<int:pk>/eliminar/', views.proveedor_eliminar, name='eliminar'),

    # Acciones
    path('<int:pk>/toggle-estado/', views.proveedor_toggle_estado, name='toggle_estado'),
]

