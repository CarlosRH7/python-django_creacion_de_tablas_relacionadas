from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Produucto,Cine 

class Home(View):
	def get(self,request):
		return render(request,'main/home.html')





# esta clase espara ver el perfil
class Perfil(View):
	def get(self,request):
		return render(request,'main/perfil.html')

	def post(self,request):
		new_p=Produucto()
		new_p.nombre= request.POST.get('nombre')
		new_p.desc=request.POST.get('desc')
		new_p.precio=request.POST.get('precio')
		new_p.usuario=request.user
		new_p.save()
		return redirect('perfil')	


# esta clase es para ver mandar el objeto cine a la plantilla cines.html
class Cines(View):
	def get(self,request):
		context={
		'cines':Cine.objects.all()
		}
		return render(request,'main/cines.html',context)

	def post(self,request):
		id=request.POST.get('cine')
		cine=Cine.objects.get(id=id)
		pelis=cine.peliculas.all()
		context={
		'cines':Cine.objects.all(),
		'pelis':pelis,
		'cine':cine
		}
		return render(request,'main/cines.html',context)

			
		
