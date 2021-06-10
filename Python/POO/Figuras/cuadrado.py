# Definicion Clase Cuadrado
''' Clase Cuadrado ''' 
class Cuadrado():
    
    ''' Constructor '''
    def __init__(self,s = 1.0):
        # Atributos
        self.side = s
    
    ''' Metodos '''
    # Asignar lado
    def setSide(self, s):
        self.side = s
    
    # Obtener lado
    def getSide(self):
        return self.side
        
    # Calcular perimetro
    def calculatePerimeter(self):
        P = 4*self.side
        return P
        
    # Calcular area
    def calculateArea(self):
        A = self.side**2
        return A
    
    def printInfo(self):
        print("\n->Lado:",self.side)
        print("->Perimetro:",self.calculatePerimeter())
        print("->Area:",self.calculateArea())


'''Programa principal'''
if __name__ == '__main__':    
    # Creando los objetos tipo cuadrado
    c1 =  Cuadrado(1)
    c2 =  Cuadrado(2)
    c3 =  Cuadrado(4)
    c4 =  Cuadrado(8)
    
    # Imprimiendo la informacion de cada objeto
    print("Cuadrado 1:")
    c1.printInfo()
    print("\nCuadrado 2:")
    c2.printInfo()
    print("\nCuadrado 3:")
    c3.printInfo()
    print("\nCuadrado 4:")
    c4.printInfo()