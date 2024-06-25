
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
#from .admin import representante_admin_site  # Import your custom admin site correctly

urlpatterns = [
    path('', views.index, name='index'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/registration/login.html"), name="login"),
    path("accounts/logout/", views.user_logout, name="logout"),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="web/registration/password_reset.html"), name="password_reset"),


    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    path('listado_jugadores/', views.listado_jugadores, name='listado_jugadores'),
    path('contacto/', views.contacto, name='contacto'),
    path('alta_jugador/', views.alta_jugador, name='alta_jugador'),
    path('listado_representantes/', views.listado_representantes, name='listado_representantes'),
    path('alta_representante/', views.alta_representante, name='alta_representante'),
    

    #path('listado_docentes', views.DocenteListView.as_view(), name='lista_docentes'),
    #path('alta_docente', views.alta_docente, name='alta_docente'),
  
]
