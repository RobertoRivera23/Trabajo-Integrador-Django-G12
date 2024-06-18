
from django.contrib import admin
from .models import Jugador, Paises, TipoContratos, Inscripcion, Representante


# Register your models with the default admin site
admin.site.register(Jugador)
admin.site.register(Representante)
admin.site.register(Paises)
admin.site.register(TipoContratos)
admin.site.register(Inscripcion)


# Create a custom admin site for RepresentanteDeJugadores
#class RepresentanteDeJugadoresAdminSite(admin.AdminSite):
    #site_header = "Administración de Representante de Jugadores"
    #site_title = "Administración para super usuarios"
    #index_title = "Administrador del Sitio"
    #empty_value_display = "No hay nada"

# Instantiate the custom admin site
#representante_admin_site = RepresentanteDeJugadoresAdminSite(name='representante_admin')

# Register RepresentanteDeJugadores model with the custom admin site
#representante_admin_site.register(RepresentanteDeJugadores)

