from django.shortcuts import render

# importar la tablas USER desde el administrador
from django.contrib.auth.models import User

# importar librerias de validacion de login de acceso
from django.contrib.auth import authenticate, logout, login

#agregar libreria de decoradores para limitar el ingreso
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home.html")

def inicio(request):
    mensaje=''
    if request.POST:
        usuario = request.POST.get("nom_user")
        contra = request.POST.get("pass")
        us = authenticate(request, username=usuario, password=contra)
        # el usuario no esta vacio y ademas el usuario activo
        if us is not None and us.is_active:
            login(request,us)
            # ir al home
            return render(request, "home.html")
        else:
            mensaje = "usuario o contraseña incorrecta"
    datos = {"mensaje":mensaje}
    return render(request, "inicio.html", datos)

def juegos(request):
    return render(request, "juegos.html")

def recomendacion(request):
    return render(request, "recomendacion.html")

def seguimiento(request):
    return render(request, "seguimiento.html")

def cerrar_seccion(request):
    logout(request)
    return render(request, "home.html")
