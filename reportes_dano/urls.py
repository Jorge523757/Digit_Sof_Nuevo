"""
DIGT SOFT - URLs para Registro de Daños
"""

from django.urls import path
from . import views

app_name = 'reportes_dano'

urlpatterns = [
    # Flujo de registro de clientes
    path('registrar/', views.registrar_dano, name='registrar'),
    path('detalle/<int:pk>/', views.detalle_reporte, name='detalle_reporte'),
    path('mis-reportes/', views.mis_reportes, name='mis_reportes'),

    # Descargar facturas
    path('descargar/<int:pk>/<str:tipo>/', views.descargar_factura, name='descargar_factura'),
    path('regenerar/<int:pk>/', views.regenerar_factura, name='regenerar_factura'),

    # Exportar a Excel
    path('exportar/excel/', views.exportar_reportes_excel, name='exportar_excel'),

    # Administración (staff only)
    path('admin/lista/', views.lista_reportes_admin, name='admin_lista'),
    path('admin/marcar-revisado/<int:pk>/', views.marcar_revisado, name='marcar_revisado'),
]

