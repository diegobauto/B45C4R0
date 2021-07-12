class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


print("Esto se imprime si ejecutamos el archivo desde aquí o desde otro archivo")

#Esta comprobación nos indica que si ejecutamos el programa en este archivo, 
#Entonces nos va a ejecutar lo que este adentro
#Si utilizamos la clase desde otro modulo no se ejecutará
if __name__ == "__main__":
    persona1 = Persona("Juan", "Perez")
    print(persona1.nombre)