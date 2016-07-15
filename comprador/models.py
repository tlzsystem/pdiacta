from django.db import models
from django.contrib.auth.models import User
from regional.models import Comuna

class Comprador(models.Model):
	usuario = models.ForeignKey(User)
	rut = models.CharField(max_length=50)
	razon_social = models.CharField(max_length=50)
	establecimiento = models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	comuna = models.ForeignKey(Comuna)

	class Meta:
		verbose_name_plural = "Compradores"
	
	def __str__(self):
		return '%s'%(self.rut)

