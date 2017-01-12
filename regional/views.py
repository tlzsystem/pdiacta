from django.shortcuts import render
from .models import Region,Provincia,Comuna
from django.http import HttpResponse
from django.core import serializers
import json

def getregiones(request):
    regiones = Region.objects.order_by('id')
    data = '['
    for region in regiones:
    	data = data + '{"id":'+str(region.id)+',"nombre_region":'+region.nombre_region+'},'
    data = data.rstrip(',')
    data = data+']'
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")

def getprovincia(request, id):
	provincias = Provincia.objects.filter(region=id)
	data = '['
	for provincia in provincias:
		data = data + '{"id":"'+str(provincia.id)+'","nombre_provincia":"'+provincia.nombre_provincia+'"},'
	data = data.rstrip(',')
	data = data+']'
	data = json.dumps(data)
	return HttpResponse(data, content_type="application/json")
	
def getcomuna(request, id):
	comunas = Comuna.objects.filter(provincia=id)
	data = '['
	for comuna in comunas:
		data = data + '{"id":"'+str(comuna.id)+'","nombre_comuna":"'+comuna.nombre_comuna+'"},'
	data = data.rstrip(',')
	data = data+']'
	data = json.dumps(data) 
	return HttpResponse(data, content_type="application/json")
