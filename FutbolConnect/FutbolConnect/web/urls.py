from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # solo agregue el > a la linea 
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    path('listado_jugadores', views.listado_jugadores, name='listado_jugadores'),
    
]