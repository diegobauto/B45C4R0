#Multiples formas en tiempo de ejecución

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self) -> str:
        return f"Empleado: {self.nombre} - {self.salario}"
    
    def mostrar_detalles(self):
        return self.__str__()

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        Empleado.__init__(self, nombre, salario)
        self.departamento = departamento
        
    def __str__(self):
        return f"{super().__str__()} -- {self.departamento}"
    
    #def mostrar_detalles(self):
    #    return self.__str__()


def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente): #Preguntamos si el objeto es instancia de la clase Gerente
        print(objeto.departamento)

empleado = Empleado("Juan", 500)
imprimir_detalles(empleado)

gerente = Gerente("Ana", 700, "Sistemas")
imprimir_detalles(gerente)