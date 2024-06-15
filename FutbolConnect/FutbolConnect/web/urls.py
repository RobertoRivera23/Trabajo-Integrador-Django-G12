# urls.py

from django.urls import path, include
from . import views
#from .admin import representante_admin_site  # Import your custom admin site correctly

urlpatterns = [
    path('', views.index, name='index'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    path('listado_jugadores/', views.listado_jugadores, name='listado_jugadores'),
    path('contacto/', views.contacto, name='contacto'),
    path('alta_jugador/', views.alta_jugador, name='alta_jugador'),
    
    #path('representante_admin/', representante_admin_site.urls),  # Use representante_admin_site.urls

    #path('representante_de_jugadores/', include('RepresentanteDeJugadores.urls')),  # Assuming this is correct
    
]
