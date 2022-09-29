from django.contrib import admin
from .models import TipoUsuario, Paciente, TipoJuego, Familiar, EstadoAnimo

# Register your models here.

admin.site.register(TipoUsuario)
admin.site.register(Paciente)
admin.site.register(TipoJuego)
admin.site.register(Familiar)
admin.site.register(EstadoAnimo)
