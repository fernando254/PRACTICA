from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
        

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=50)
    whatsaap = models.CharField(max_length=20)
    telegram = models.CharField(max_length=30)
    diabetes = models.BooleanField()
    hipertencion = models.BooleanField()
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class TipoJuego(models.Model):
    nombre_juego = models.CharField(max_length=30)
    fecha_juego = models.DateField()
    puntaje_juego = models.IntegerField()
    paciente = models.ForeignKey(Paciente,on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_juego


class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=50)
    whatsaap = models.CharField(max_length=20)
    telegram = models.CharField(max_length=30)
    diabetes = models.BooleanField()
    hipertencion = models.BooleanField()
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class EstadoAnimo(models.Model):
    nombre_estado_animo = models.CharField(max_length=50)
    fecha = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_estado_animo
