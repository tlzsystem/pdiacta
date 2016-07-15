from django.contrib import admin
from .models import Region, Provincia, Comuna

class RegionAdmin(admin.ModelAdmin):
	list_display=('id','nombre_region')

class ProvinciaAdmin(admin.ModelAdmin):
	list_display=('id','nombre_provincia','region')

class ComunaAdmin(admin.ModelAdmin):
	list_display=('id','nombre_comuna','provincia')

admin.site.register(Region, RegionAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comuna, ComunaAdmin)