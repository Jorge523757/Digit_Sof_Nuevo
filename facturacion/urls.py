from django.urls import path
from . import views

app_name = 'facturacion'

urlpatterns = [
    path('', views.facturas_lista, name='lista'),
    path('crear/', views.factura_crear, name='crear'),
    path('<int:pk>/', views.factura_detalle, name='detalle'),
    path('<int:pk>/editar/', views.factura_editar, name='editar'),
    path('<int:pk>/eliminar/', views.factura_eliminar, name='eliminar'),
]



