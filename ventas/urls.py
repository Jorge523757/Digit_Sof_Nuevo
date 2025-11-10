"""
DIGT SOFT - URLs del Módulo de Ventas
"""

from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.ventas_lista, name='lista'),
    path('<int:pk>/', views.venta_detalle, name='detalle'),
    path('crear/', views.venta_crear, name='crear'),
]

