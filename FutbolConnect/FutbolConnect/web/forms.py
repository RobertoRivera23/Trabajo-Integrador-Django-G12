from django import forms
from django.core.exceptions import ValidationError

class AltaJugadorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'}))
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.IntegerField(label="DNI", required=True) 
    #fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", required=True) #Lo sacamos para Probar sin Fecha de Nacimiento
    categoria = forms.CharField(label="Categoría", required=True)
    posicion = forms.CharField(label="Posición", required=True),
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
        