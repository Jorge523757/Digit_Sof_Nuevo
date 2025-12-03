from django.urls import path
from .views import index, crear_proveedor

app_name = 'proveedores'
urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', crear_proveedor, name='crear_proveedor'),
]
