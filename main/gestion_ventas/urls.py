from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
from django.shortcuts import render

def index(request):
    return render(request, 'main/gestion_clientes/index.html')

