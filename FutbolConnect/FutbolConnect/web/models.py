from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Jugador(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=True)

class Paises(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=True)
    cuit = models.IntegerField(verbose_name="CUIT", unique=True)  # Changed field name to lowercase

class TipoContratos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    turno = models.CharField(max_length=50, verbose_name="Turno")
    cupos = models.IntegerField(verbose_name="Cupos",
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]   
    )
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    paises = models.ForeignKey(Paises, on_delete=models.CASCADE, null=True)
    jugador = models.ManyToManyField(Jugador, through='Inscripcion')

class Inscripcion(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    tipocontratos = models.ForeignKey(TipoContratos, on_delete=models.CASCADE, default=1)  # Assuming default value is 1
    fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción", auto_now_add=True)

