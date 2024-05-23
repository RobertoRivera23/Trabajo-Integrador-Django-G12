from django import forms



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
    
class AltaRepresentanteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", required=True)
    categoria = forms.CharField(label="Categoría", required=True)
    posicion = forms.CharField(label="Posición", required=True),
    direccion = forms.CharField(label="Dirección", required=True)
    telefono = forms.CharField(label="Teléfono", required=True)
    correo = forms.EmailField(label="Email", required=True)
        