"""
DIGT SOFT - Módulo de Técnicos
URLs - Rutas del módulo
"""

from django.urls import path
from . import views

app_name = 'tecnicos'

urlpatterns = [
    path('', views.lista_tecnicos, name='lista'),
    path('crear/', views.crear_tecnico, name='crear'),
    path('editar/<int:pk>/', views.editar_tecnico, name='editar'),
    path('detalle/<int:pk>/', views.detalle_tecnico, name='detalle'),
    path('eliminar/<int:pk>/', views.eliminar_tecnico, name='eliminar'),
    path('buscar/', views.buscar_tecnico, name='buscar'),
]

