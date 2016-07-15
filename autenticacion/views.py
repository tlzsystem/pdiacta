from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def log_in(request):
	if request.method =='POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect(reverse('dashboard:index'))
				else:
					return HttpResponse("Usuario no activo")
			else:
				return HttpResponseRedirect('/login/')
	else:
		formulario = AuthenticationForm()
	return render(request, 'autenticacion/login.html')

@login_required()
def log_out(request):
	logout(request)
	return HttpResponseRedirect('/login/')