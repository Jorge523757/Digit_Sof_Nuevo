from django.urls import path
from django.http import HttpResponse

app_name = 'facturacion'

def index(request):
    return HttpResponse('Facturación')

urlpatterns = [
    path('', index, name='lista'),
    path('crear/', index, name='crear'),
]



