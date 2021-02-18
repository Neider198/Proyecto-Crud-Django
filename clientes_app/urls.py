from django.urls import  include ,path
from rest_framework import routers
from clientes_app import views

router = routers.DefaultRouter()
router.register('persona', views.PersonaLista)
router.register('sexo', views.SexoLista)
router.register('tipo-identificacion', views.TipoIdentificacionLista)


# urlpatterns = router.urls
# urlpatterns += path('loginn', views.loginn),
urlpatterns = [
   path('', include(router.urls)),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
