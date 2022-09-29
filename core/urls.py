from django.contrib import admin
from django.urls import path
#importar los "views" desde archivos views.py
from .views import home, inicio_seccion


urlpatterns = [
    
    path('',home,name='HOME'),
    path('inicio_seccion/',inicio_seccion,name='INICIO'),
]