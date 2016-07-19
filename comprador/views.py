from django.shortcuts import render
from .models import Comprador


def compradores(request):
    compradores = Comprador.objects.filter(usuario = request.user)
    return render(request,'comprador/compradores.html',{'compradores':compradores,'val':4})

def byid(request, id):
	print("estamos en esta vista, por id")
	print("el id es: ",id)
	compradores = Comprador.objects.filter(id=id)
	return render(request, 'comprador/comprador.html',{'compradores':compradores})