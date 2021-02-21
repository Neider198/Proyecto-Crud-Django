from django.contrib.auth.forms import UserModel
from django.contrib.auth.models import User
from rest_framework import serializers
from clientes_app.models import Persona, Sexo, TipoIdentificacion

class PersonaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Persona
    fields = '__all__'

class PersonaLeerSerializer(PersonaSerializer):
  tipoidentificacion = serializers.CharField(source = 'tipoidentificacion.nombre')
  sexo = serializers.CharField(source = 'sexo.nombre')

class SexoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sexo
    fields = '__all__'

class TipoIdentificacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoIdentificacion
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'