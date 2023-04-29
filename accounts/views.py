from django.shortcuts import render
from accounts.forms import *
from accounts.models import *
# Create your views here.


def inicioAppAccounts(request):
    
    return render(request, "inicioApp.html")

def crearBlog(request):

    if request.method == "POST":

        form = BlogCreadoForm(request.POST)
        if form.is_valid():

            blog = BlogCreado()
            blog.tituloDelBlog = form.cleaned_data["tituloDelBlog"]
            blog.subtituloDelBlog = form.cleaned_data["subtituloDelBlog"]
            blog.cuerpoDelBlog = form.cleaned_data["cuerpoDelBlog"]
            blog.autorDelBlog = form.cleaned_data["autorDelBlog"]
            blog.fechaDelBlog = form.cleaned_data["fechaDelBlog"]
            blog.save()
            blog = BlogCreadoForm(request.POST)
    else:
        
        form = BlogCreadoForm(request.POST)

    blogs = BlogCreado.objects.all() 

    return render(request, "inicio.html", {"blogs": blogs, "form" : form})

def iniciarSesion(request):
    
    return render(request, "iniciarSesion.html")

def registrarse(request):

    return render(request, "registrarse.html")    