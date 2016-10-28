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

# class Produucto(models.Model):
# 	new_p=Produucto()
# 	new_p.nombre= request.POST.get('nombre')
# 	new_p.desc=request.POST.get('desc')
# 	new_p.precio=request.POST.get('precio')
# 	new_p.usuario=request.user
# 	new_p.save()


# 	def __str__(self):
# 		return self.nombre		
