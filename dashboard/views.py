from django.shortcuts import render

def dashboard(request):
	print("vamos a enviar al dashboard")
	return render(request,'dashboard/index.html')
