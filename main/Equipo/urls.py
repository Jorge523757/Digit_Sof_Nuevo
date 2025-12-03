from django.urls import path
from .views import index, crear_equipo

app_name = 'equipo'
urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', crear_equipo, name='crear_equipo'),
]

