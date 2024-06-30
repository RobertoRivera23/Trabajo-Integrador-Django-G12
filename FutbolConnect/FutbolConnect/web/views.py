from django.shortcuts import redirect, render
from django.contrib import messages
from . import forms
from .models import Jugador, Representante, Contacto, TipoContratos

# Vistas relacionadas con el menú y otras páginas

def index(request):
    context = {
        'nombre': 'Daniel Pavon',
    }
    return render(request, 'web/index.html', context)

def user_logout(request):
    # Cerrar sesión y redireccionar al inicio
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('index')

def contacto(request):
    context = {}
    if request.method == "GET":
        context['envio_contacto_form'] = forms.ContactoForm()
    else:
        form = forms.ContactoForm(request.POST)
        context['envio_contacto_form'] = form 
        if form.is_valid():
            nuevo_contacto = Contacto(
                nombre=form.cleaned_data['nombre'], 
                apellido=form.cleaned_data['apellido'], 
                mail=form.cleaned_data['mail'],
                fecha_hora=datetime.now()  # Añadido la fecha y hora actual
            )
            nuevo_contacto.save()
            messages.success(request, 'Su petición de contacto fue realizada con éxito')
            return redirect('index')
    return render(request, 'web/contacto.html', context)

def alta_jugador(request):
    context = {}
    if request.method == "GET":
        context['alta_jugador_form'] = forms.AltaJugadorForm()
    else:
        form = forms.AltaJugadorForm(request.POST)
        context['alta_jugador_form'] = form 
        if form.is_valid():
            nuevo_jugador = Jugador(
                nombre=form.cleaned_data['nombre'], 
                apellido=form.cleaned_data['apellido'], 
                dni=form.cleaned_data['dni'], 
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'], 
                categoria=form.cleaned_data['categoria'], 
                posicion=form.cleaned_data['posicion'], 
                pais=form.cleaned_data['pais'], 
                direccion=form.cleaned_data['direccion'], 
                telefono=form.cleaned_data['telefono'], 
                mail=form.cleaned_data['mail'] 
            )
            nuevo_jugador.save()
            messages.success(request, 'El Jugador fue dado de alta con éxito')
            return redirect('index')
    return render(request, 'web/alta_jugador.html', context)

def alta_representante(request):
    context = {}
    if request.method == "GET":
        context['alta_representante_form'] = forms.AltaRepresentanteForm()
    else:
        form = forms.AltaRepresentanteForm(request.POST)
        context['alta_representante_form'] = form 
        if form.is_valid():
            nuevo_representante = Representante(
                nombre=form.cleaned_data['nombre'], 
                apellido=form.cleaned_data['apellido'], 
                dni=form.cleaned_data['dni'], 
                cuit=form.cleaned_data['cuit']
            )
            nuevo_representante.save()
            messages.success(request, 'El Representante fue dado de alta con éxito')
            return redirect('index')
    return render(request, 'web/alta_representante.html', context)

def listado_jugadores(request):
    jugadores = Jugador.objects.all().order_by('nombre')
    context = {
        'jugadores': jugadores,
        'cuota_al_dia': True  # Ejemplo de contexto adicional
    }
    return render(request, 'web/listado_jugadores.html', context)

def listado_representantes(request):
    representantes = Representante.objects.all()
    context = {
        'representantes': representantes,
        'cuota_al_dia': True  # Ejemplo de contexto adicional
    }
    return render(request, 'web/listado_representantes.html', context)

def listado_contratos(request):
    contratos = TipoContratos.objects.all()
    context = {
        'contratos': contratos,
    }
    return render(request, 'web/lista_contratos.html', context)

def alta_contrato(request):
    context = {}
    if request.method == "GET":
        context['alta_contrato_form'] = forms.AltaContratoForm()
    else:
        form = forms.AltaContratoForm(request.POST)
        context['alta_contrato_form'] = form 
        if form.is_valid():
            nuevo_contrato = TipoContratos(
                nombre=form.cleaned_data['nombre'],
                tipo_contrato=form.cleaned_data['tipo de contrato'],
                descripcion=form.cleaned_data['descripcion'],
                posicion_contratado=form.cleaned_data['posicion contratada'],
                fecha_inicio=form.cleaned_data['fecha de inicio'],
                fecha_fin=form.cleaned_data['fecha de fin'],
                clausula=form.cleaned_data['clausula'],
                monto=form.cleaned_data['monto'],
                representante=form.cleaned_data['representante'],
                jugadores=form.cleaned_data['jugador']
            )
            nuevo_contrato.save()
            messages.success(request, 'El Contrato fue realizado con éxito')
            return redirect('index')
    return render(request, 'web/alta_contrato.html', context)
