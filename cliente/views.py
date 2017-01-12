from django.shortcuts import render
from .models import Cliente
from regional.models import Region
from .forms import ClienteForm
from django.http import HttpResponseRedirect


def clientes(request):
	clientes = Cliente.objects.filter(usuario=request.user)
	return render(request, 'cliente/clientes.html',{'clientes':clientes,'val':3})

def byclientes(request, id):
	print("estamos en esta vista, por id")
	print("el id es: ",id)
	clientes = Cliente.objects.filter(id=id)
	return render(request, 'cliente/cliente.html',{'clientes':clientes,'val':3})

def addcliente(request):
	regiones = Region.objects.all()
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.usuario = request.user
			post.save()
			return HttpResponseRedirect('/dashboard/clientes/')
	else:
		form = ClienteForm()
	return render(request, 'cliente/nuevocliente.html',{'regiones':regiones,'form':form})


def deletebyid(request, id):
	Cliente.objects.filter(id=id).delete()
	return HttpResponseRedirect('/dashboard/clientes/')
