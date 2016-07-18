from django.shortcuts import render
from .models import Cliente

def clientes(request):
	clientes = Cliente.objects.filter(usuario=request.user)

	return render(request, 'cliente/clientes.html',{'clientes':clientes})

def byclientes(request, offset):
	clientes = Clientes.objects.filter(usuario=request.user, id=offset)
	return render(request, 'cliente/cliente.html')
