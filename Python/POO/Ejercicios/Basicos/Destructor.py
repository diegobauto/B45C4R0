class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #Eliminar un objeto
    def __del__(self):
        print(f"Eliminado: {self.nombre}")


persona1 = Persona("Juan", "Gonzales")
print(persona1.nombre + " " + persona1.apellido)

print("Eliminar".center(30, "-"))
del persona1