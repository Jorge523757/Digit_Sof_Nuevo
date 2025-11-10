from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    """Página principal del sistema - Landing Page"""
    return render(request, 'core/landing.html')

def about(request):
    """Página acerca de"""
    return render(request, 'core/about.html')
