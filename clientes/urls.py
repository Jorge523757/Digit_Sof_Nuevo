"""
DIGIT SOFT - Módulo de Clientes
URLs
"""

from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.lista_clientes, name='lista'),
    path('crear/', views.crear_cliente, name='crear'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar'),
    path('detalle/<int:pk>/', views.detalle_cliente, name='detalle'),
]



