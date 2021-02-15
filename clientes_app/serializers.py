from rest_framework import serializers
from clientes_app.models import Persona, Sexo, TipoIdentificacion

class PersonaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Persona
    fields = '__all__'

class PersonaLeerSerializer(PersonaSerializer):
  tipoidentificacion = serializers.CharField(source = 'tipoidentificacion.nombre')
  sexo = serializers.CharField(source = 'Sexos.nombre')

class SexoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sexo
    fields = '__all__'

class TipoIdentificacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoIdentificacion
    fields = '__all__'