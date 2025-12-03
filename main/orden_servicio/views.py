from django.shortcuts import render

def index(request):
    return render(request, 'main/orden_servicio/index.html')

