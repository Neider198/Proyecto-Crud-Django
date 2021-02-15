from django.db import models


class Sexo(models.Model):
  nombre = models.CharField(max_length=20)

  class Meta:
    managed=True
    db_table='"basicos\".\"Sexo"'

class TipoIdentificacion(models.Model):
  nombre = models.CharField(max_length=30) 
  
  class Meta:
    managed=True
    db_table = '"basicos\".\"tipoidentificacion"'

class Persona(models.Model):
  nombres = models.CharField(max_length=30)
  apellidos = models.CharField(max_length=60)
  identificacion = models.CharField(max_length=20)
  tipoidentificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
  sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
  direccion = models.CharField(max_length=60)
  telefono = models.CharField(max_length=10)
  # usuario = models.CharField(max_length=30)
  # password = models.CharField(max_length=250)


