from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from .models import Jugador, Representante, TipoContratos, Contrato, opciones, opciones_posicion, opciones_tipo_contrato 


class CustomErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])



class AltaJugadorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'}))
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
    telefono = forms.CharField(label="Teléfono", required=True)
    correo = forms.EmailField(label="Email", required=True)

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
        