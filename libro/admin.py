from django.contrib import admin
from .models import Libro, Hoja, DetalleHoja

class LibroAdmin(admin.ModelAdmin):
	list_display=('usuario','id','numero','abierto')

class HojaAdmin(admin.ModelAdmin):
	list_display=('id','libro','numero')

class DetalleHojaAdmin(admin.ModelAdmin):
	list_display=('id','hoja','producto')


admin.site.register(Libro, LibroAdmin)
admin.site.register(Hoja, HojaAdmin)
admin.site.register(DetalleHoja, DetalleHojaAdmin)
