"""
DIGIT SOFT - Módulo de Backups
URLs
"""

from django.urls import path
from . import views

app_name = 'backups'

urlpatterns = [
    path('', views.lista_backups, name='lista'),
    path('crear/', views.crear_backup, name='crear'),
    path('restaurar/<int:backup_id>/', views.restaurar_backup, name='restaurar'),
    path('descargar/<int:backup_id>/', views.descargar_backup, name='descargar'),
    path('eliminar/<int:backup_id>/', views.eliminar_backup, name='eliminar'),
    path('configuracion/', views.configuracion_backups, name='configuracion'),
]

