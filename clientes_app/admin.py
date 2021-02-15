from django.contrib import admin
from clientes_app.models import Persona, Sexo, TipoIdentificacion

admin.site.register(Persona)
admin.site.register(Sexo)
admin.site.register(TipoIdentificacion)
# Register your models here.
