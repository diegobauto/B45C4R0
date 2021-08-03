from personas.models import Domicilio
from personas.models import Persona
from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)