"""
URLs para el proceso de ventas y checkout
"""
from django.urls import path
from . import views_checkout

app_name = 'ventas_checkout'

urlpatterns = [
    # Checkout
    path('checkout/', views_checkout.checkout_view, name='checkout'),
    path('procesar-orden/', views_checkout.procesar_orden, name='procesar_orden'),
    
    # Facturación
    path('factura/<int:orden_id>/', views_checkout.ver_factura, name='ver_factura'),
    path('factura/<int:orden_id>/pdf/', views_checkout.descargar_factura_pdf, name='descargar_factura'),
    path('mis-ordenes/', views_checkout.mis_ordenes, name='mis_ordenes'),
]

