from django.shortcuts import render
from rest_framework import viewsets
from clientes_app.models import Persona, Sexo, TipoIdentificacion
from clientes_app.serializers import PersonaLeerSerializer, PersonaSerializer, SexoSerializer, TipoIdentificacionSerializer

class PersonaLista (viewsets.ModelViewSet):
  queryset = Persona.objects.all()

  def get_serializer_class(self):
        # Define your HTTP method-to-serializer mapping freely.
        # This also works with CoreAPI and Swagger documentation,
        # which produces clean and readable API documentation,
        # so I have chosen to believe this is the way the
        # Django REST Framework author intended things to work:
        if self.request.method in ('GET', ):
            # Since the ReadSerializer does nested lookups
            # in multiple tables, only use it when necessary
            return PersonaLeerSerializer
        return PersonaSerializer
  # serializer_class = PersonaSerializer

class SexoLista (viewsets.ModelViewSet):
  queryset = Sexo.objects.all()
  serializer_class = SexoSerializer

class TipoIdentificacionLista (viewsets.ModelViewSet):
  queryset = TipoIdentificacion.objects.all()
  serializer_class = TipoIdentificacionSerializer



      
  


