"""
DIGT SOFT - URLs del Módulo de Equipos
"""

from django.urls import path
from . import views

app_name = 'equipos'

urlpatterns = [
    path('', views.equipos_lista, name='lista'),
    path('<int:pk>/', views.equipo_detalle, name='detalle'),
    path('crear/', views.equipo_crear, name='crear'),
]

