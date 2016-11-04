from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	SEXO=(('hombre','HOMBRE'),('mujer','MUJER'))
	OCUP=(
		  ('estudiante','ESTUDIANTE'),
		  ('academico','Academico'),
		  ('publico','Servidor Publico'),
		  ('godinez', 'Empleado')
		  )

	edad = models.IntegerField()
	tel= models.CharField(max_length=13)
	genero= models.CharField(max_length=6,choices=SEXO)
	alias=models.CharField(max_length=10)
	domicilio=models.TextField()
	ocupacion=models.CharField(max_length=140,choices=OCUP)
	usuario=models.OneToOneField(User)

class Produucto(models.Model):
	nombre= models.CharField(max_length=140)
	desc=models.TextField()
	precio=models.CharField(max_length=50)
	usuario=models.ForeignKey(User,related_name='home')	

	def __str__(self):
		return self.nombre



# clase para agrgar a la base cines y peliculas
class Cine(models.Model):
	nombre=models.CharField(max_length=20)
	lugar=models.TextField()

	def __str__(self):
		return self.nombre


class Pelicula(models.Model):
	GENEROS=(
		('terror', 'Terror'),
		('SciFi','Ciencia Ficción')
	)
	director=models.CharField(max_length=140)
	genero=models.CharField(max_length=50,choices=GENEROS)
	titulo= models.CharField(max_length=20)
	sinopsis=models.TextField()
	cines = models.ForeignKey(Cine,related_name='peliculas')

	def __str__(self):
		return self.titulo








