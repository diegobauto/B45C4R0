"""
La Sobreescritura es la forma por la cual una clase que hereda 
puede re-definir los métodos de su clase Padre
"""

class Persona:      
    def __init__(self, nombre, edad):        
        self.nombre = nombre        
        self.edad = edad    

    def __str__(self):        
        return self.nombre  + " -> " + str(self.edad) + " años"


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad)
        #super().__init__(nombre, edad)
        self.sueldo = sueldo  

    def __str__(self):
        return super().__str__() + ", $" + str(self.sueldo)


persona1 = Persona("Juan", 20)
print(persona1)


empleado1 = Empleado("Ana", 30, 200)
print(empleado1)
