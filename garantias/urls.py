"""
DIGT SOFT - URLs del Módulo de Garantías
"""

from django.urls import path
from . import views

app_name = 'garantias'

urlpatterns = [
    # Lista y búsqueda
    path('', views.garantias_lista, name='lista'),
    path('buscar/', views.garantia_buscar, name='buscar'),
    path('por-vencer/', views.garantias_por_vencer, name='por_vencer'),
    path('vencidas/', views.garantias_vencidas, name='vencidas'),

    # CRUD
    path('crear/', views.garantia_crear, name='crear'),
    path('<int:pk>/', views.garantia_detalle, name='detalle'),
    path('<int:pk>/editar/', views.garantia_editar, name='editar'),
    path('<int:pk>/eliminar/', views.garantia_eliminar, name='eliminar'),
]

