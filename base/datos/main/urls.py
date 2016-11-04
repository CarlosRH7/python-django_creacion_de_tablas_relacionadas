# este archivo de creo manulamente
from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^$',views.Home.as_view(),name="home"),
# esta url es para ver el perfil 
# (para crear un link solo es modificar urls, views, home(en donde va el boton del link y crear perfil(la plantilla html)))
	url(r'^perfil/',views.Perfil.as_view(),name="perfil"),

#url para ver los cines en la plantillas cines.html
	url(r'^cines/',views.Cines.as_view(),name="cines"),


]