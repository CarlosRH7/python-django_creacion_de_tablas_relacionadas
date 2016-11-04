from django.contrib import admin
from .models import Perfil, Produucto, Cine, Pelicula
# esto es par la base de datos para poder obserbar graficamente en el admin
admin.site.register(Perfil)
admin.site.register(Produucto)
admin.site.register(Cine)
admin.site.register(Pelicula)