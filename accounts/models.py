from django.db import models

# Create your models here.
class UsuarioRegistrado(models.Model):
    nombreDeUsuario=models.CharField(max_length=20, unique=True)
    contrasena=models.CharField(max_length=50)
    email=models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombreDeUsuario} - {self.email}"

class BlogCreado(models.Model):
    tituloDelBlog=models.CharField(max_length=50, unique=True)
    subtituloDelBlog=models.CharField(max_length=100)
    cuerpoDelBlog=models.CharField(max_length=1000)
    autorDelBlog=models.CharField(max_length=50)
    fechaDelBlog=models.DateField()

    def __str__(self):
        return f"{self.tituloDelBlog.capitalize()} - {self.subtituloDelBlog}"