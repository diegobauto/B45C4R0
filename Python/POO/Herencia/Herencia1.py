class Persona:      
    def __init__(self, nombre, edad):        
        self.nombre = nombre        
        self.edad = edad    

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad)
        #super().__init__(nombre, edad)
        self.sueldo = sueldo  


persona1 = Persona("Juan", 20)
print(persona1.nombre)


empleado1 = Empleado("Ana", 30, 200)
print(empleado1.nombre)
print(empleado1.sueldo)