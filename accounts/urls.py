from django.urls import path
from accounts.views import *

urlpatterns = [
    
    path("", inicioAppAccounts, name="inicioAppAccounts"),
    path("crearBlog/", crearBlog, name="crearBlog"),
    path("iniciarSesion/", iniciarSesion, name="iniciarSesion"),
    path("registrarse/", registrarse, name="registrarse"),
    

]