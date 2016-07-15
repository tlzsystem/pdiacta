from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente
from comprador.models import Comprador


class Libro(models.Model):
	usuario = models.ForeignKey(User)
	numero = models.CharField(max_length=10)
	fecha_creacion = models.DateField(auto_now=True)
	fecha_asignacion = models.DateField()
	abierto = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural="Libros"
	def __str__(self):
		return '%s'%(self.numero)

class Hoja(models.Model):
	libro = models.ForeignKey(Libro)
	comprador = models.ForeignKey(Comprador)
	cliente = models.ForeignKey(Cliente)
	numero = models.IntegerField()

	class Meta:
		verbose_name_plural="Hojas"
	def __str__(self):
		return '%s'%(self.numero)

class DetalleHoja(models.Model):
	hoja = models.ForeignKey(Hoja)
	producto = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural="Detalles"
	def __str__(self):
		return '%s'%(self.id)



