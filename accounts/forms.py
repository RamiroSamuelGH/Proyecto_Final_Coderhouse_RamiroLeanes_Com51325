from django import forms

class UsuarioRegistradoForm(forms.Form):
    nombreDeUsuario=forms.CharField(max_length=20)
    contrasena=forms.CharField(max_length=50)
    email=forms.EmailField()

class BlogCreadoForm(forms.Form):
    tituloDelBlog=forms.CharField(max_length=50)
    subtituloDelBlog=forms.CharField(max_length=100)
    cuerpoDelBlog=forms.CharField(max_length=1000)
    autorDelBlog=forms.CharField(max_length=50)
    fechaDelBlog=forms.DateField()