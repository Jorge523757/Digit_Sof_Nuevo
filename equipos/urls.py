from django.urls import path
from django.http import HttpResponse

app_name = 'equipos'

def index(request):
    return HttpResponse('Equipos')

urlpatterns = [
    path('', index, name='lista'),
    path('crear/', index, name='crear'),
]



