from django.shortcuts import render
from .models import Cliente

def clientes(request):
	print("estamos en la vista normal")
	clientes = Cliente.objects.filter(usuario=request.user)
	return render(request, 'cliente/clientes.html',{'clientes':clientes,'val':3})

def byclientes(request, id):
	print("estamos en esta vista, por id")
	print("el id es: ",id)
	clientes = Cliente.objects.filter(id=id)
	return render(request, 'cliente/cliente.html',{'clientes':clientes,'val':3})
