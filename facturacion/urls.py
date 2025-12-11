"""DIGIT SOFT - URLs Facturación"""
from django.urls import path
from . import views

app_name = 'facturacion'

urlpatterns = [
    path('', views.facturas_lista, name='lista'),
    path('<int:pk>/', views.factura_detalle, name='detalle'),
]

