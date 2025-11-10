from django.urls import path
from django.http import HttpResponse

app_name = 'compras'

def index(request):
    return HttpResponse('Compras')

urlpatterns = [
    path('', index, name='lista'),
    path('crear/', index, name='crear'),
]



