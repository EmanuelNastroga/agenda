from django.contrib import admin

# Register your models here.
from core.models import Evento



class Evento_admin(admin.ModelAdmin):
    list_display = ('titulo','data_evento','data_criacao')
    list_filter = ('titulo','usuario',)

admin.site.register(Evento,Evento_admin)
