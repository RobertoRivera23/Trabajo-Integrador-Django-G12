from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from .models import Jugador, Representante, TipoContratos, Contrato, opciones, opciones_posicion, opciones_tipo_contrato 
from datetime import *

class CustomErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    mail = forms.EmailField(label="Email", required=True)
    fecha_hora = forms.DateField(label="Fecha de consulta", required=True)

class AltaJugadorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class': 'campo_azul'}))
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.IntegerField(label="dni", required=True) 
    fecha_nacimiento = forms.DateField(label="Fecha_nacimiento", required=True) #Lo sacamos para Probar sin Fecha de Nacimiento
    categoria = forms.CharField(label="Categoría", required=True)
    posicion = forms.ChoiceField(label="Posición", required=True, choices=opciones_posicion)
    pais = forms.CharField(label="País", required=True)
    direccion = forms.CharField(label="Dirección", required=True)
    telefono = forms.CharField(label="Teléfono", required=True)
    mail = forms.EmailField(label="Email", required=True)
    
class AltaRepresentanteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'}))
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.IntegerField(label="DNI", required=True) 
    direccion = forms.CharField(label="Dirección", required=True)
    cuit = forms.IntegerField(label="CUIT", required=True)
    telefono = forms.CharField(label="Teléfono", required=True)
    correo = forms.EmailField(label="Email", required=True)

class AltaContratoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    tipo_contrato = forms.ChoiceField(label="Amateur o Profesional", choices=opciones_tipo_contrato)
    descripcion = forms.CharField(required=True, label="Descripción")
    posicion_contratado = forms.ChoiceField(label="Posición Contratada", choices=opciones_posicion)
    fecha_inicio = forms.DateField(label="Fecha de inicio")
    fecha_fin = forms.DateField(label="Fecha de finalización")
    clausula = forms.CharField(label="Clausula", required=True)
    monto = forms.IntegerField(label="Monto")
    representante = forms.IntegerField(label="Representante") #un repre muchos contratos
    jugadores = forms.IntegerField(label="Jugador")

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")
        
        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede estar compuesto por letras")

        return self.cleaned_data["apellido"]

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        
        if nombre == "Daniel" and apellido == "Flores":
            raise ValidationError("El usuario Daniel Flores ya existe")
        
        if self.cleaned_data["dni"] < 1000000:
            raise ValidationError("El dni debe tener 8 digitos")

        return self.cleaned_data
        