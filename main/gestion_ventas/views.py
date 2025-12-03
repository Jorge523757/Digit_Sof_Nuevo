from django.shortcuts import render

def index(request):
    return render(request, 'main/gestion_ventas/index.html')

