from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime
from . import forms
from django.contrib import messages

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

def alta_jugador(request):
    context = {}

    if request.method == "GET":
        context['alta_jugador_form'] = forms.AltaJugadorForm()
   
    else: # En caso de que no sea GET, paso con datos que me paso el usuario
        form = forms.AltaJugadorForm(request.POST)
        context['alta_jugador_form'] = form 
        
        # Validar el form
        if form.is_valid():
        # Si el form es correcto
        # Lo redirijo a una vista segura por ejemplo el index
            messages.success (request, 'El Jugador fue dado de alta con éxito')

            print(request.POST)
            
            #return redirect('index') #Se lo saco para probar
       
    return render(request, '../templates/web/alta_jugador.html', context)
