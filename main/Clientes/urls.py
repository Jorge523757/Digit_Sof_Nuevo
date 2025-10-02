from django.urls import path
from .views import index, crear_cliente

app_name = 'clientes'
urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', crear_cliente, name='crear_cliente'),
]
