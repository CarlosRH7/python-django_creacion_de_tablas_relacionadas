from django.contrib import admin
from .models import Perfil, Produucto
# esto es par la base de datos para poder obserbar graficamente en el admin
admin.site.register(Perfil)
admin.site.register(Produucto)