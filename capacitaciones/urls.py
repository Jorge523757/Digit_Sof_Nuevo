from django.urls import path
from django.http import HttpResponse

app_name = 'capacitaciones'

def index(request):
    return HttpResponse('Capacitaciones')

urlpatterns = [
    path('', index, name='lista'),
    path('crear/', index, name='crear'),
]


