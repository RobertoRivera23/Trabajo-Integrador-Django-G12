from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=True)

    class Meta:
        abstract = True

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre_completo()} | DNI: {self.dni}"


class Jugador(Persona):
    LE = models.IntegerField(verbose_name="Pase del club", unique=True, null=True)

    def __str__(self):
        return f"{self.nombre_completo()} | DNI: {self.dni} | LE: {self.LE}"


class Paises(models.Model):
    pais = models.CharField(max_length=100, verbose_name="País", unique=True)
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad", null=True, blank=True)

    def __str__(self):
        return f"{self.pais} | Ciudad: {self.ciudad}"


class Clausula(models.Model):
    clausula = models.CharField(max_length=100, verbose_name="Clausula", unique=True)

    def __str__(self):
        return self.clausula
    

class TipoContratos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    tipo_contrato = models.IntegerField(verbose_name="Amateur o Profesional", validators=[MinValueValidator(0), MaxValueValidator(100)])
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    clausula = models.ForeignKey(Clausula, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} | Clausula: {self.clausula} | Descripción: {self.descripcion}"


class Posicion_Jugador(models.Model):
    posicion = models.CharField(max_length=100, verbose_name="Posición", unique=True)

    def __str__(self):
        return self.posicion


class Inscripcion(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    posicion_jugador = models.ForeignKey(Posicion_Jugador, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción", auto_now_add=True)

    class Meta:
        db_table = 'inscripcion'

    def __str__(self):
        return f"Inscripción de {self.jugador.nombre_completo()} en posición: {self.posicion_jugador}"


 


############################ Hasta aca teniamos #####################################

#class Jugador(models.Model):
#    nombre = models.CharField(max_length=100, verbose_name="Nombre")
#    apellido = models.CharField(max_length=100, verbose_name="Apellido")
#    dni = models.IntegerField(verbose_name="DNI", unique=True)

#class Paises(models.Model):
 #   nombre = models.CharField(max_length=100, verbose_name="Nombre")
  #  apellido = models.CharField(max_length=100, verbose_name="Apellido")
   # dni = models.IntegerField(verbose_name="DNI", unique=True)
    #cuit = models.IntegerField(verbose_name="CUIT", unique=True)  # Changed field name to lowercase

#class TipoContratos(models.Model):
 #   nombre = models.CharField(max_length=100, verbose_name="Nombre")
  #  descripcion = models.CharField(max_length=200, verbose_name="Descripción")
   # turno = models.CharField(max_length=50, verbose_name="Turno")
    #cupos = models.IntegerField(verbose_name="Cupos",
     #   validators=[
      #      MaxValueValidator(100),
       #     MinValueValidator(0)
        #]   
    #)
    #fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    #fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    #paises = models.ForeignKey(Paises, on_delete=models.CASCADE, null=True)
    #jugador = models.ManyToManyField(Jugador, through='Inscripcion')

#class Inscripcion(models.Model):
 #   jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
  #  tipocontratos = models.ForeignKey(TipoContratos, on_delete=models.CASCADE, default=1)  # Assuming default value is 1
   # fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción", auto_now_add=True)

