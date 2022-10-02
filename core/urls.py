from django.contrib import admin
from django.urls import path
#importar los "views" desde archivos views.py
from .views import cerrar_seccion, home, inicio, juegos, recomendacion, seguimiento


urlpatterns = [
    
    path('',home,name='HOME'),
    path('inicio/',inicio,name='INICIO'),
    path('juegos/',juegos,name='JUEGO'),
    path('recomendacion/',recomendacion,name='RECOMENDACION'),
    path('seguimiento/',seguimiento,name='SEGUIMIENTO'),
    path('cerrar_sesion/',cerrar_seccion,name='CERRAR'),
    
    
    
]