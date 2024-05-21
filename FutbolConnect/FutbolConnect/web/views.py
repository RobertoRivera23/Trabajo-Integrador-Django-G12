from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Aca creamos todas las vistas posibles

def index(request):
    return render(request, '../templates/web/index.html')
