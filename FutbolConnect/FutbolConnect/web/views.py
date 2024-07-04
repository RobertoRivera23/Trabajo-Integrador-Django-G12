from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.http import HttpResponse
from .models import Jugador, Representante, Contacto, TipoContratos, Contrato
from .forms import AltaJugadorForm, AltaRepresentanteForm, AltaContratoForm, FirmaContratoForm, ContactoForm
from datetime import datetime
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'web/index.html')       


def user_logout(request):
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('index')

def contacto(request):
    context = {}
    if request.method == "GET":
        context['envio_contacto_form'] = ContactoForm()
    else:
        form = ContactoForm(request.POST)
        context['envio_contacto_form'] = form 
        if form.is_valid():
            nuevo_contacto = Contacto(
                nombre=form.cleaned_data['nombre'], 
                apellido=form.cleaned_data['apellido'], 
                mail=form.cleaned_data['mail'],
                fecha_hora=datetime.now()
            )
            nuevo_contacto.save()
            messages.success(request, 'Su petición de contacto fue realizada con éxito')
            return redirect('index')
    return render(request, 'web/contacto.html', context)


@login_required
def alta_jugador(request):
    context = {}
    if request.method == "GET":
        context['alta_jugador_form'] = AltaJugadorForm()
    else:
        form = AltaJugadorForm(request.POST)
        context['alta_jugador_form'] = form 
        if form.is_valid():
            nuevo_jugador = form.save()
            messages.success(request, 'El Jugador fue dado de alta con éxito')
            return redirect('index')
    return render(request, 'web/alta_jugador.html', context)

@login_required
def alta_representante(request):
    context = {}
    if request.method == "GET":
        context['alta_representante_form'] = AltaRepresentanteForm()
    else:
        form = AltaRepresentanteForm(request.POST)
        context['alta_representante_form'] = form 
        if form.is_valid():
            nuevo_representante = form.save()
            messages.success(request, 'El Representante fue dado de alta con éxito')
            return redirect('index')
    return render(request, 'web/alta_representante.html', context)

@login_required
def alta_contrato(request):
    context = {}
    if request.method == "GET": 
        context['alta_contrato_form'] = AltaContratoForm()
    else:
        form = AltaContratoForm(request.POST)
        context['alta_contrato_form'] = form
        if form.is_valid():
            nuevo_contrato = form.save()
            messages.success(request, 'El Contrato fue creado con éxito')
            return redirect('index')
    return render(request, 'web/alta_contrato.html', context)

@login_required
def listado_jugadores(request):
    jugadores = Jugador.objects.all().order_by('nombre')
    context = {
        'jugadores': jugadores,
        'cuota_al_dia': True  # Ejemplo de contexto adicional
    }
    return render(request, 'web/listado_jugadores.html', context)

@login_required
def listado_representantes(request):
    representantes = Representante.objects.all()
    context = {
        'representantes': representantes,
        'cuota_al_dia': True  # Ejemplo de contexto adicional
    }
    return render(request, 'web/listado_representantes.html', context)

@login_required
def listado_contratos(request):
    contratos = TipoContratos.objects.all()
    context = {
        'contratos': contratos,
    }
    return render(request, 'web/lista_contratos.html', context)


@login_required
def firma_contrato(request):
    context = {}
    if request.method == "GET": 
        context['firma_contrato_form'] = FirmaContratoForm()
    else:
        form = FirmaContratoForm(request.POST)
        context['firma_contrato_form'] = form
        if form.is_valid():
            nuevo_contrato_firmado = form.save()
            messages.success(request, 'El Contrato fue firmado con éxito')
            return redirect('index')
    return render(request, 'web/firma_contrato.html', context)

@login_required
def lista_contratos_firmados(request):
    contratos = Contrato.objects.all()
    context = {
        'contratos': contratos,
    }
    return render(request, 'web/lista_contratos_firmados.html', context)

#MODIFICA

@login_required
def edit_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    if request.method == "POST":
        form = AltaJugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            messages.success(request, 'El Jugador fue modificado con éxito')
            return redirect('listado_jugadores')
    else:
        form = AltaJugadorForm(instance=jugador)
    
    context = {
        'jugador': jugador,
        'edit_jugador_form': form
    }
    return render(request, 'web/edit_jugador.html', context)