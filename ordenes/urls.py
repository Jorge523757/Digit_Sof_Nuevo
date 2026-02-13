"""
DIGT SOFT - URLs del Módulo de Órdenes de Servicio
"""

from django.urls import path
from . import views

# Importar views_reportes y views_vistas si existen
try:
    from . import views_reportes
    REPORTES_AVAILABLE = True
except ImportError:
    REPORTES_AVAILABLE = False

try:
    from . import views_vistas
    VISTAS_AVAILABLE = True
except ImportError:
    VISTAS_AVAILABLE = False

app_name = 'ordenes'

urlpatterns = [
    # Lista y búsqueda
    path('', views.ordenes_lista, name='lista'),
    path('tablero/', views.ordenes_tablero, name='tablero'),

    # CRUD
    path('crear/', views.orden_crear, name='crear'),
    path('<int:pk>/', views.orden_detalle, name='detalle'),
    path('<int:pk>/editar/', views.orden_editar, name='editar'),

    # Acciones
    path('<int:pk>/cambiar-estado/', views.orden_cambiar_estado, name='cambiar_estado'),
    path('<int:pk>/repuestos/', views.orden_agregar_repuesto, name='agregar_repuesto'),

    # Notificaciones técnico
    path('<int:pk>/notificar/', views.tecnico_notificar_actualizacion, name='tecnico_notificar'),

    # API para autocompletado
    path('api/clientes/', views.api_clientes_autocomplete, name='api_clientes'),
    path('api/tecnicos/', views.api_tecnicos_autocomplete, name='api_tecnicos'),
]

# Agregar URLs de reportes si están disponibles
if REPORTES_AVAILABLE:
    urlpatterns += [
        path('reportes/', views_reportes.reportes_ordenes, name='reportes'),
        path('reportes/vista-previa/', views_reportes.vista_previa_reportes, name='reportes_vista_previa'),
        path('reportes/excel/', views_reportes.generar_reporte_excel, name='reportes_excel'),
        path('reportes/pdf/', views_reportes.generar_reporte_pdf, name='reportes_pdf'),
    ]

# Agregar URLs de vistas SQL si están disponibles
if VISTAS_AVAILABLE:
    urlpatterns += [
        path('vistas/completa/', views_vistas.vista_ordenes_completa, name='vista_completa'),
        path('vistas/por-estado/', views_vistas.vista_ordenes_por_estado, name='vista_por_estado'),
        path('vistas/por-tecnico/', views_vistas.vista_ordenes_por_tecnico, name='vista_por_tecnico'),
        path('vistas/por-cliente/', views_vistas.vista_ordenes_por_cliente, name='vista_por_cliente'),
        path('vistas/criticas/', views_vistas.vista_ordenes_criticas, name='vista_criticas'),
        path('vistas/equipos/', views_vistas.vista_analisis_equipos, name='vista_equipos'),
        path('vistas/dashboard-ejecutivo/', views_vistas.vista_dashboard_ejecutivo, name='vista_dashboard'),
        path('vistas/timeline/', views_vistas.vista_timeline_ordenes, name='vista_timeline'),
        path('api/vistas/', views_vistas.api_vista_ordenes, name='api_vistas'),
    ]

