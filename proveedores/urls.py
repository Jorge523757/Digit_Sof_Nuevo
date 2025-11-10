from django.urls import path
from django.http import HttpResponse

app_name = 'proveedores'

def index(request):
    return HttpResponse('Proveedores')

urlpatterns = [
    path('', index, name='lista'),
    path('crear/', index, name='crear'),
]



