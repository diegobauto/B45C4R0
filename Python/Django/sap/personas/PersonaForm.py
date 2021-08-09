from personas.models import Persona
from django.forms import ModelForm, EmailInput

class PersonaForm(ModelForm):
    class Meta:
        model = Persona #El modelo para el formulario va a ser de Persona
        fields = "__all__" #Vamos a añadir todos los campos
        widgets = { #Especificar a nivel de html como quiero que sean mis campos
            "email": EmailInput(attrs={"type":"email"})
        }