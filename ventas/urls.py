from django.urls import path
from django.http import HttpResponse

app_name = 'ventas'

def index(request):
    return HttpResponse('Ventas')

urlpatterns = [
    path('', index, name='lista'),
    path('crear/', index, name='crear'),
]



