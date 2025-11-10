from django.shortcuts import render

def index(request):
    return render(request, 'main/servicio_tecnico/index.html')

