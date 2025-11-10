from django.urls import path
from django.http import HttpResponse

app_name = 'ordenes'

def index(request):
    return HttpResponse('Órdenes')

urlpatterns = [
    path('', index, name='lista'),
    path('crear/', index, name='crear'),
]



