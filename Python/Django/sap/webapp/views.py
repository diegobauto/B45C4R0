from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona

# Create your views here.
def bienvenido(request): #request es como la respuesta que nos da django del servidor
    num_personas = Persona.objects.count()
    #personas = Persona.objects.all() #No ordena la tabla, solo como se presenta en la base de datos
    personas = Persona.objects.order_by("id") #Vamos a ordenar la tabla por el id
    diccionario = {
        "num_personas":num_personas,
        "personas": personas,
    }
    return render(request, "bienvenido.html", diccionario)

def despedida(request):
    return HttpResponse("Hasta luego")