from django import forms
from django.core.exceptions import ValidationError


class AltaJugadorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", required=True)
    categoria = forms.CharField(label="Categoría", required=True)
    posicion = forms.CharField(label="Posición", required=True),
    direccion = forms.CharField(label="Dirección", required=True)
    telefono = forms.CharField(label="Teléfono", required=True)
    correo = forms.EmailField(label="Email", required=True)
    

    def clean_nombre(self):
        if not self.cleaned_data['nombre'].isalpha:
            raise ValidationError("El nombre solo puede estar compuesto por letras")
        
        return self.cleaned_data['nombre']
        