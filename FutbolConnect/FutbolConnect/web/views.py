from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# Aca creamos todas las vistas posibles

def index(request):

    context ={
        'nombre': 'Daniel, Pavon',
        'fecha_hora': datetime.datetime.now()
          }
    
    return render(request, '../templates/web/index.html', context)

def saludar (request, nombre):
    print(request.method)

    return HttpResponse(f"<h1>Bienvenid@ {nombre} </h1>")

def listado_jugadores(request):
    
    context ={
         'nombre': 'Daniel, Pavon',
        'jugadores':[
            'Lionel Messi',
            'Diego Armando Maradona',
            'DiMaria',
        ],
        'cuota_al_dia': True

    }

    return render(request, 'web/listado_jugadores.html', context)

def contacto(request):

    context = {
        'nombre': 'Daniel, Pavon',
        'fecha_hora': datetime.datetime.now()
    }
    return render(request, '../templates/web/contacto.html', context)