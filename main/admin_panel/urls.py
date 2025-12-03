from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
from django.shortcuts import render

def index(request):
    return render(request, 'main/facturacion/index.html')

