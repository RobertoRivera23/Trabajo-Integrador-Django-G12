from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#Clase padre con atributos comunes para Jugadores y Representantes
class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=False)
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=True)
    direccion = models.CharField(verbose_name="Dirección", null=False)
    telefono = models.CharField(verbose_name="Teléfono", null=False)    
    mail = models.EmailField(verbose_name="Email", null=False, blank=True)

    class Meta:
        abstract = True
    # Metodo que retornara nombre y apellido
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre_completo()} | DNI: {self.dni} | dirección: {self.direccion} | teléfono: {self.telefono} | email: {self.mail}"

# opciones para el choice de jugador
opciones = [
    (1, " "),
    (2, "Si"),
    (3, "No")
]

#Opciones de Posición
opciones_posicion = [
    (1," "),
    (2, "Arquero"), 
    (3, "Defensor Central"),
    (4, "Lateral Izquierdo"), 
    (5, "Lateral Derecho"), 
    (6, "Mediocampista Central"), 
    (7, "Mediocampista Izquierdo"),
    (8, "Mediocampista Derecho"),
    (9, "Delantero")   
]
#Clase jugdor que hereda de Persona y devuele (atributos de persona y jugador)
class Jugador(Persona):
    estado = models.IntegerField(
        verbose_name="Pase del club", 
        unique=True, null=True, blank=True,
        choices=opciones)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento"),
    categoria = models.CharField(verbose_name="Categoría")
    posicion = models.IntegerField(verbose_name="Posición Contratada: ", null=False, blank=False, 
                                   choices=opciones_posicion)
    pais = models.CharField(verbose_name="País")
   
    def __str__(self):
        return f"{self.nombre_completo()} | DNI: {self.dni} | Pase: {self.estado} | Posición: {self.posicion} | email: {self.mail}" 
   
    #Lo sacamos para Probar sin Fecha de Nacimiento
    
   
   
    
#Clase representante que hereda de persona y devuelve (atributos de persona y representante)
class Representante(Persona):
    cuit = models.BigIntegerField(verbose_name="CUIT", unique=True, null= False, blank=False,
                                  validators=[MinValueValidator(9999999999), MaxValueValidator(99999999999)])

    def __str__(self):
        return f"{self.nombre_completo()} | DNI: {self.dni} | Pase: {self.cuit}"


class Paises(models.Model):
    pais = models.CharField(max_length=100, verbose_name="País", unique=True)
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad", null=True, blank=True)

    def __str__(self):
        return f"{self.pais} | Ciudad: {self.ciudad}"

#Se redactan las clausulas especiales del contrato
class Clausula(models.Model):
    Clausula = models.CharField(max_length=1000, verbose_name="Clausula", unique=True)

    def __str__(self):
        return self.clausula
    

#opciones tipo de contrato
opciones_tipo_contrato = [
    (1, " "),
    (2, "Amateur"), 
    (3, "Profesional")
]



#
class TipoContratos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    tipo_contrato = models.IntegerField(verbose_name="Amateur o Profesional", null=False, blank=False,
                                        choices=opciones_tipo_contrato)
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    posicion_contratado = models.IntegerField(verbose_name="Posición Contratada: ", null=False, blank=False, 
                                   choices=opciones_posicion)
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    clausula = models.ForeignKey(Clausula, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Contrato Tipo: {self.tipo_contrato} | Jugador: {self.nombre} | Clausula: {self.clausula} | Posición Contratada: {self.posicion_contratado} | Descripción: {self.descripcion}"


#opciones para posiciones de los  jugadores

class Contrato(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    fecha_contratacion = models.DateField(verbose_name="Fecha de contratación", auto_now_add=True)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE)
    TipoContratos = models.ForeignKey(TipoContratos, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'contrato'

    def __str__(self):
        return f"Contrato de {self.jugador.nombre_completo()} | en posición: {self.jugador.posicion} | Representante: {self.representante.nombre_completo} | tipo de contratación: {self.TipoContratos.tipo_contrato}"
  


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

