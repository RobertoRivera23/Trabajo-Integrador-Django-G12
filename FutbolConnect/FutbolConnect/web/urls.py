from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    path('listado_jugadores', views.listado_jugadores, name='listado_jugadores'),
    path('contacto', views.contacto, name='contacto'),
    path('alta_jugador', views.alta_jugador, name='alta_jugador'),
    path('alta_representante', views.alta_representante, name='alta_representante'),
]
