from django.shortcuts import render

def index(request):
    return render(request, 'main/gestion_productos/index.html')

