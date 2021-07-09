from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "app001/base.html")

def saludar(request):
    return HttpResponse("Estoy saludando desde la ruta saludar")