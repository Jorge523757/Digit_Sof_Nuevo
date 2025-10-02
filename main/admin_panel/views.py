from django.shortcuts import render

def index(request):
    return render(request, 'main/admin_panel/index.html')

