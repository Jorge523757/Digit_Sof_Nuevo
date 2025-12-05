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

    # Reportes
    path('reporte/pdf/', views.compra_reporte_pdf, name='reporte_pdf'),
    path('reporte/excel/', views.compra_reporte_excel, name='reporte_excel'),
]

