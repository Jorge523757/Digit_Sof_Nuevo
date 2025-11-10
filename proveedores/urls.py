"""
DIGT SOFT - URLs del Módulo de Proveedores
"""

from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.proveedores_lista, name='lista'),
    path('crear/', views.proveedor_crear, name='crear'),
    path('<int:pk>/', views.proveedor_detalle, name='detalle'),
    path('<int:pk>/editar/', views.proveedor_editar, name='editar'),
    path('<int:pk>/eliminar/', views.proveedor_eliminar, name='eliminar'),
]

