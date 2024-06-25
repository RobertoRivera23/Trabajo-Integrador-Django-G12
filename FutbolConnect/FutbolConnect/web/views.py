from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime
from . import forms
from django.contrib import messages
from .models import Jugador, Representante


from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#from .forms import *
from .models import Jugador, Paises



# Create your views here.
# Aca creamos todas las vistas posibles

def index(request):

    context ={
        'nombre': 'Daniel, Pavon',
        'fecha_hora': datetime.datetime.now()
          }
    
    return render(request, '../templates/web/index.html', context)



def user_logout(request):
    logout(request)

    messages.success(request, 'Sesion Cerrada')

    return redirect('index')


def saludar (request, nombre):
    print(request.method)

    return HttpResponse(f"<h1>Bienvenid@ {nombre} </h1>")



def alumnos_por_año(request, year):
    alumnos = ["Carlos", "Maria", "Jose"] # """"Levanta""""" los usuarios de la BBDD
    return HttpResponse(f"listado de alumnos: {year} \n {alumnos}")

jugadores = Jugador.objects.all().order_by('nombre') #QuerySet
@login_required
def listado_jugadores(request):
    
    context ={
        'jugadores': jugadores,
        'cuota_al_dia': True
    }
    return render(request, 'web/listado_jugadores.html', context)


representantes = Representante.objects.all()
@login_required
def listado_representantes(request):
    
    context ={
        'representates': representantes,
        'cuota_al_dia': True
    }
    return render(request, 'web/listado_representantes.html', context)


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
            nuevo_jugador = Jugador(
                nombre = form.cleaned_data['nombre'], 
                apellido = form.cleaned_data['apellido'], 
                dni = form.cleaned_data['dni'], 
                fecha_nacimiento = form.cleaned_data['fecha_nacimiento'], 
                categoria = form.cleaned_data['categoria'], 
                posicion = form.cleaned_data['posicion'], 
                pais = form.cleaned_data['pais'], 
                direccion = form.cleaned_data['direccion'], 
                telefono = form.cleaned_data['telefono'], 
                mail = form.cleaned_data['mail'] 
            )

            nuevo_jugador.save()

            messages.success (request, 'El Jugador fue dado de alta con éxito')

            #print(request.POST)
         # Lo redirijo a una vista segura por ejemplo el index     
            return redirect('index')
       
    return render(request, '../templates/web/alta_jugador.html', context)


def alta_representante(request):
    context = {}

    if request.method == "GET":
        context['alta_representante_form'] = forms.AltaRepresentanteForm() 
   
    else: # En caso de que no sea GET, paso con datos que me paso el usuario
        form = forms.AltaRepresentanteForm(request.POST)
        context['alta_representante_form'] = form 
        
        # Validar el form
        if form.is_valid():
        # Si el form es correcto
        # Lo redirijo a una vista segura por ejemplo el index

            nuevo_representante = Representante(
                nombre = form.cleaned_data['nombre'], 
                apellido = form.cleaned_data['apellido'], 
                dni = form.cleaned_data['dni'], 
                cuit = form.cleaned_data['cuit']
            )

            nuevo_representante.save()




            messages.success (request, 'El Representante fue dado de alta con éxito')

            print(request.POST)
            
            #return redirect('index') #Se lo saco para probar
       
    return render(request, '../templates/web/alta_representante.html', context)
