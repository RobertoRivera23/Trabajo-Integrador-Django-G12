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
    activo = forms.BooleanField(label="Estado", required=False)

class AltaJugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type':'date'})}

    
class AltaRepresentanteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'}))
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.IntegerField(label="DNI", required=True) 
    direccion = forms.CharField(label="Dirección", required=True)
    cuit = forms.IntegerField(label="CUIT", required=True)
    telefono = forms.CharField(label="Teléfono", required=True)
    mail = forms.EmailField(label="Email", required=True)
    activo = forms.BooleanField(label="Estado", required=False)

class AltaContratoForm(forms.ModelForm):
    class Meta:
        model = TipoContratos
        fields = '__all__'
        widgets = {'fecha_inicio': forms.DateInput(attrs={'type':'date'}), 
                   'fecha_fin': forms.DateInput(attrs={'type':'date'})}


class FirmaContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'
        widgets = {'fecha_contratacion': forms.DateInput(attrs={'type':'date'})}



    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede estar compuesto por letras")
        
        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede estar compuesto por letras")

        return self.cleaned_data["apellido"]

    def clean_dni(self):
        if self.cleaned_data["dni"] < 1000000:
            raise ValidationError("El dni debe tener 8 digitos")

        return self.cleaned_data["dni"]

