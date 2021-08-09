from personas.PersonaForm import PersonaForm
from personas.models import Persona
from django.shortcuts import get_object_or_404, redirect, render
#from django.forms import modelform_factory

# Create your views here.
def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id) Si no hay un id, sale error
    persona = get_object_or_404(Persona, pk=id) #Si no hay id, nos redirige a pagina no encontrada
    return render(request, "detalle.html", {"persona":persona})

#Crear un objeto de tipo formulario relacionado a la clase de modelo de Persona
# exclude es para indicar si vamos a omitir alguno de los campos de nuestra clase de modelo(Persona)
#Lo podemos crear en una sola linea o como tal en una clase por aparte en dondes nos 
#permite mayor flexibilidad a la hora de trabajar con él

#PersonaForm = modelform_factory(Persona, exclude=[]) #Primera forma


def nuevaPersona(request):
    if request.method == "POST":
        #LLenamos el objeto formaPersona con la info del metodo POST que se envio desde el formulario
        formaPersona = PersonaForm(request.POST) 
        if formaPersona.is_valid(): #Validamos el formulario
            formaPersona.save() #Guardamos la información en la base de datos
            return redirect("index")
    else:
        formaPersona = PersonaForm() #Obtenemos el formulario
    return render(request, "nuevo.html", {"formaPersona":formaPersona})

def actualizarPersona(request, id):
    #Recuperamos el objeto persona
    persona = get_object_or_404(Persona, pk=id)
    if request.method == "POST":
        #Tenemos que pasar la intancia para hacer referencia a cual id apuntar
        #Cuando pasamos la instancia django lo que hace es actualizar
        #Cuando no lo que hace es agregar, por eso es necesario pasar la instancia
        formaPersona = PersonaForm(request.POST, instance=persona) 
        if formaPersona.is_valid(): 
            formaPersona.save()
            return redirect("index")
    else:
        #Le pasamos la informacion de el objeto persona recuperado de la base de datos
        formaPersona = PersonaForm(instance=persona) 
    return render(request, "actualizar.html", {"formaPersona":formaPersona})

def eliminarPersona(request, id):
    #Recuperamos el objeto persona
    persona = get_object_or_404(Persona, pk=id)
    if persona: #Verificamos si la persona existe
        persona.delete() #Eliminamos el objeto de la base de datos
    return redirect("index") #Redireccionamos a la pagina principal