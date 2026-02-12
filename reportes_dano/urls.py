"""
DIGIT SOFT - URLs de Reportes de Daño
"""

from django.urls import path
from . import views

app_name = 'reportes_dano'

urlpatterns = [
    # Cliente
    path('crear/', views.crear_reporte, name='crear'),
    path('mis-reportes/', views.mis_reportes, name='mis_reportes'),
    path('detalle/<int:reporte_id>/', views.detalle_reporte, name='detalle'),

    # Admin
    path('admin/lista/', views.lista_reportes_admin, name='lista_admin'),
]

