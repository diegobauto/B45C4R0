from math import pi

''' Clase circulo ''' 
class Circulo():
    
    ''' Constructor '''
    def __init__(self,r = 0.0):
        # Miembros
        self.radio = r
    
    ''' Metodos '''
    # Asignar radio
    def asignarRadio(self, r):
        self.radio = r
    
    # Obtener radio
    def obtenerRadio(self):
        return self.radio
        
    # Calcular perimetro
    def calculatePerimeter(self):
        per = 2*pi*self.radio
        return per
        
    # Calcular Area
    def calculateArea(self):
        return pi*(self.radio**2)
    
    def printInfo(self):
        print("\n->Radio:",self.radio)
        print("->Perimetro:",self.calculatePerimeter())
        print("->Area:",self.calculateArea())

    
# Programa principal
# Usamos objetos de la clase creada (prueba).
if __name__ == '__main__':
    
    ''' Creando objetos '''
    c1 = Circulo(1)
    c2 = Circulo(4.5)
    
    ''' Calculando area y perimetro del circulo '''
    a1 = c1.calcularArea()
    a2 = c2.calcularArea()
    p1 = c1.calcularPerimetro()
    p2 = c2.calcularPerimetro()
    
    ''' Imprimiento informacion de los  circulos '''
    print("Circulo 1: ")
    print("- Radio:" + str(c1.radio)) # No recomendada
    print("- Perimetro:" + str(p1)) 
    print("- Area:" + str(a1)) 
    print()
    print("Circulo 2: ")
    print("- Radio:" + str(c2.obtenerRadio())) # Recomendada
    print("- Perimetro:" + str(p2)) 
    print("- Area:" + str(a2))