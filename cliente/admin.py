from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('usuario','nombres','apellido_paterno','apellido_materno','identificacion')

admin.site.register(Cliente, ClienteAdmin)