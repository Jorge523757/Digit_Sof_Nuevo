"""DIGT SOFT - URLs Capacitaciones"""
from django.urls import path
from . import views

app_name = 'capacitaciones'

urlpatterns = [
    path('', views.capacitaciones_lista, name='lista'),
    path('<int:pk>/', views.capacitacion_detalle, name='detalle'),
]


