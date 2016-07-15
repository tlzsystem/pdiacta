from django.db import models

class Region(models.Model):
	nombre_region = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Regiones"
	def __str__(self):
		return '%s'%(self.nombre_region)


class Provincia(models.Model):
	nombre_provincia = models.CharField(max_length=50)
	region = models.ForeignKey(Region)
	class Meta:
		verbose_name_plural = "Provincias"
	def __str__(self):
		return '%s'%(self.nombre_provincia)

class Comuna(models.Model):
	nombre_comuna = models.CharField(max_length=50)
	provincia = models.ForeignKey(Provincia)
	class Meta:
		verbose_name_plural="Comunas"
	def __str__(self):
		return '%s'%(self.nombre_comuna)