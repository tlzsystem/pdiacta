from django.db import models
from django.contrib.auth.models import User
from regional.models import Comuna

class Cliente(models.Model):
	usuario = models.ForeignKey(User)
	nombres = models.CharField(max_length=50)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	identificacion = models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	comuna = models.ForeignKey(Comuna)
	telefono = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural="Clientes"

	def __str__(self):
		return '%s'%(self.identificacion)



