from django.contrib.auth.forms import PasswordChangeForm, UserModel
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from clientes_app.models import Persona, Sexo, TipoIdentificacion
from clientes_app.serializers import PersonaLeerSerializer, PersonaSerializer, SexoSerializer, TipoIdentificacionSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

  def post(self, request, *args, **kwargs):
      serializer = self.serializer_class(data=request.data,
                                          context={'request': request})
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data['user']
      token, created = Token.objects.get_or_create(user=user)
      return Response({
          'token': token.key,
          'user_id': user.pk,
          'email': user.email
      })




# @api_view(['POST'])
# def loginn(request):
#   username = request.POST.get('usuario')
#   password = request.POST.get('password') 


#   try:
#     usuario= User.objects.get(username=username)
#   except User.DoesNotExist:
#     return Response("Usuario Incorrecto")

#   password_valid = check_password(password,usuario.password)  

#   if not password_valid:
#     return Response("Contraseña Incorrecto")
      
#   token, created = Token.objects.get_or_create(user =usuario)
#   return Response(token.key)
class PersonaLista (viewsets.ModelViewSet):
  queryset = Persona.objects.all()
  # permission_classes = [IsAuthenticated]

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
  # permission_classes = [IsAuthenticated]

class TipoIdentificacionLista (viewsets.ModelViewSet):
  queryset = TipoIdentificacion.objects.all()
  serializer_class = TipoIdentificacionSerializer
  # permission_classes = [IsAuthenticated]




      
  


