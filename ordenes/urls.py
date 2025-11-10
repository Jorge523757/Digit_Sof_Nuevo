"""
DIGT SOFT - URLs del Módulo de Órdenes de Servicio
"""

from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('', views.ordenes_lista, name='lista'),
    path('crear/', views.orden_crear, name='crear'),
    path('<int:pk>/', views.orden_detalle, name='detalle'),
    path('<int:pk>/editar/', views.orden_editar, name='editar'),
    path('<int:pk>/eliminar/', views.orden_eliminar, name='eliminar'),
]

