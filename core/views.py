from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def inicio_seccion(request):
    return render(request, "inicio_seccion.html")