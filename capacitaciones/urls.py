from django.urls import path
from . import views

app_name = 'capacitaciones'

urlpatterns = [
    path('', views.capacitaciones_lista, name='lista'),
    path('crear/', views.capacitacion_crear, name='crear'),
    path('<int:pk>/', views.capacitacion_detalle, name='detalle'),
    path('<int:pk>/editar/', views.capacitacion_editar, name='editar'),
    path('<int:pk>/eliminar/', views.capacitacion_eliminar, name='eliminar'),
]


