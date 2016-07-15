from django.contrib import admin
from .models import Comprador

class CompradorAdmin(admin.ModelAdmin):
	list_display=('usuario','rut','razon_social','establecimiento')

admin.site.register(Comprador, CompradorAdmin)
	
