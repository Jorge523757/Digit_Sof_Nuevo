from django.shortcuts import render, redirect
from main.forms import EquipoForm
from main.models import Equipo

def index(request):
    equipos = Equipo.objects.all()
    return render(request, 'main/Equipo/equipo.html', {'equipos': equipos})

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipo:index')
    else:
        form = EquipoForm()
    return render(request, 'main/Equipo/equipo_form.html', {'form': form})

