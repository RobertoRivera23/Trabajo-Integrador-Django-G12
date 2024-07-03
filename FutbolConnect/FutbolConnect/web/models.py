from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from FutbolConnect import settings

#Clase padre con atributos comunes para Jugadores y Representantes

# opciones para el choice de jugador
opciones = [
    (1, " "),
    (2, "Si"),
    (3, "No")
]
class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=False)
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=False)
    direccion = models.CharField(verbose_name="Dirección", null=False)
    telefono = models.CharField(verbose_name="Teléfono", null=False)    
    mail = models.EmailField(verbose_name="Email", null=False, blank=True)
    activo = models.BooleanField("Activo", default=True, null=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    class Meta:
        abstract = True
    # Metodo que retornara nombre y apellido
    def nombre_completo(self):
        return f"{self.apellido} {self.nombre}"

    def __str__(self):
        return f"{self.nombre_completo()} | DNI: {self.dni} | dirección: {self.direccion} | teléfono: {self.telefono} | email: {self.mail} | Activo: {self.activo}"

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
        null=True, blank=True,
        choices=opciones)
    fecha_nacimiento = models.DateField(verbose_name="Fecha_nacimiento", null=True)
    categoria = models.CharField(verbose_name="Categoría")
    posicion = models.IntegerField(verbose_name="Posición ", 
                                   null=True, blank=True, 
                                   choices=opciones_posicion)
    pais = models.CharField(verbose_name="País")

   
    def __str__(self):
        return f"nombre: {self.nombre_completo()} | DNI: {self.dni} | F.Nac.: {self.fecha_nacimiento} | Pase: {self.estado} | Posición: {self.posicion} | email: {self.mail} | Activo: {self.activo}" 
   
    #Lo sacamos para Probar sin Fecha de Nacimiento
    
   
   
    
#Clase representante que hereda de persona y devuelve (atributos de persona y representante)
class Representante(Persona):
    cuit = models.BigIntegerField(verbose_name="CUIT", unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.nombre_completo()} | DNI: {self.dni} | CUIT: {self.cuit} | Telefono: {self.telefono} | email: {self.mail} Activo: {self.activo}"


#opciones tipo de contrato
opciones_tipo_contrato = [
    (1, "Amateur"), 
    (2, "Profesional"),
]

#
class TipoContratos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    tipo_contrato = models.IntegerField(verbose_name="Tipo de contrato", 
                                        null=False, blank=False,
                                        choices=opciones_tipo_contrato)
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    posicion_contratado = models.IntegerField(verbose_name="Posición Contratada", 
                                              null=False, blank=False, 
                                              choices=opciones_posicion)
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    clausula = models.CharField(max_length=1000, verbose_name="Clausula")
    monto = models.IntegerField(verbose_name="Monto")
    activo = activo = models.BooleanField("Activo", default=True, null=True)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE, null=True, blank=True) #un repre muchos contratos
    jugadores = models.ManyToManyField(Jugador, through='Contrato')

    def __str__(self):
        return f"Contrato Tipo: {self.tipo_contrato} | Clausula: {self.clausula} | Posición Contratada: {self.posicion_contratado} | Descripción: {self.descripcion} | Representante: {self.representante} | Jugador: {self.jugadores} | Activo: {self.activo}"

#Tabla intermedia
class Contrato(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    TipoContratos = models.ForeignKey(TipoContratos, on_delete=models.CASCADE)
    fecha_contratacion = models.DateField(verbose_name="Fecha de contratación", auto_now_add=True)
    activo = activo = models.BooleanField("Activo", default=True, null=True)
        
    def __str__(self):
        return f"Representante: {self.TipoContratos.representante.nombre_completo} | Jugador: {self.jugador.nombre_completo} | Tipo de Contrato: {self.TipoContratos.tipo_contrato} | Activo: {self.activo}"


   # class Meta:
    #    db_table = 'Contrato'

    #def __str__(self):
     #   return f"Contrato de {self.jugador.nombre_completo()} | en posición: {self.jugador.posicion} | Representante: {self.representante.nombre_completo} | tipo de contratación: {self.TipoContratos.tipo_contrato}"
  
#Fomulario de Contacto VEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRR
  
class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    mail = models.EmailField(verbose_name="Email", null=False, blank=True)
    fecha_hora = models.DateField(verbose_name="Fecha de contacto", auto_now_add=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Email: {self.mail} | Fecha y Hora: {self.fecha_hora}"


############################ Hasta aca teniamos #####################################

#class Jugador(models.Model):
#    nombre = models.CharField(max_length=100, verbose_name="Nombre")
#    apellido = models.CharField(max_length=100, verbose_name="Apellido")
#    dni = models.IntegerField(verbose_name="DNI", unique=True)

#class Paises(models.Model):
 #   nombre = models.CharField(max_length=100, verbose_name="Nombre")
  #  apellido = models.CharField(max_length=100, verbose_name="Apellido")
   # dni = models.IntegerField(verbose_name="DNI", unique=True)
    #cuit = models.IntegerField(verbose_name="CUIT", unique=True)  # Changed field name to2
    #  lowercase

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

