"""
DIGIT SOFT - Módulo de Técnicos
URLs - Rutas del módulo con gestión completa
"""

from django.urls import path
from . import views

app_name = 'tecnicos'

urlpatterns = [
    # Lista y gestión
    path('', views.lista_tecnicos, name='lista'),
    path('crear/', views.crear_tecnico, name='crear'),
    path('editar/<int:tecnico_id>/', views.editar_tecnico, name='editar'),
    path('detalle/<int:tecnico_id>/', views.detalle_tecnico, name='detalle'),

    # Acciones
    path('deshabilitar/<int:tecnico_id>/', views.deshabilitar_tecnico, name='deshabilitar'),
    path('eliminar/<int:tecnico_id>/', views.eliminar_tecnico, name='eliminar'),
    path('restaurar/<int:tecnico_id>/', views.restaurar_tecnico, name='restaurar'),
]

