#No poder accerder a los atributos de nuestra clase
#Para poder hacerlo creamos los metodos get y set

class Persona():
    def __init__(self, nombre, apellido):
        #El guion bajo es para encapsular el atributo -> Privado
        self._nombre = nombre
        self._apellido = apellido

    #Decorador que lo que hace es que la función la tome como si fuera un atributo de nuestra clase 
    @property
    def nombre(self):
        return self._nombre

    #Debe contener el mismo nombre del property 
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

persona1 = Persona("Juan", "Perez")

persona1.nombre = "Juanito"

print(persona1.nombre)
