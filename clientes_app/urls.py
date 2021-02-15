from django.urls import  include ,path
from rest_framework import routers
from clientes_app import views

router = routers.DefaultRouter()
router.register(r'persona', views.PersonaLista)
router.register(r'sexo', views.SexoLista)
router.register(r'tipo-identificacion', views.TipoIdentificacionLista)


urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]