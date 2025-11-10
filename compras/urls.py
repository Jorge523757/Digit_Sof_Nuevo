"""
DIGT SOFT - URLs del Módulo de Compras
"""

from django.urls import path
from . import views

app_name = 'compras'

urlpatterns = [
    path('', views.compras_lista, name='lista'),
    path('crear/', views.compra_crear, name='crear'),
    path('<int:pk>/', views.compra_detalle, name='detalle'),
    path('<int:pk>/editar/', views.compra_editar, name='editar'),
    path('<int:pk>/eliminar/', views.compra_eliminar, name='eliminar'),
]

