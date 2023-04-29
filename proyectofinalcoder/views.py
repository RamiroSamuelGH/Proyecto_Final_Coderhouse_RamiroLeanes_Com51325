from django.shortcuts import render


def inicio(request):

    return render(request, "inicio.html")

def sobreMi(request):

    return render(request, "sobreMi.html")




