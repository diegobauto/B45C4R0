SLOW = 1
MEDIUM = 2
FAST = 3

class Fan():
    
    # Constructor
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False):
        # Lo que se define como privado se le coloca raya baja (_) al atributo
        self._speed = speed
        self._on = on
        self._radius = radius
        self._color = color
    
    # Metodos accesor
    def getSpeep(self):
        return self._speed
    
    def isON(self):
        return self._on
    
    def getRadius(self):
        return self._radius
    
    def getColor(self):
        return self._color
    
    # Metodos mutator
    def setSpeep(self, speed):
        self._speed = speed
    
    def turnON(self):
        self._on = True
    
    def turnOFF(self):
        self._on = False
    
    def setRadius(self, radius):
        self._radius = radius
    
    def setColor(self, color):
        self._color = color
        
    def printInfo(self):
        print("-Estado:", self._on)    
        print("-Velocidad:",self._speed)    
        print("-Radio: " + str(self._radius))   
        print("-Color: " + self._color)   
        
    
# Usando objetos
ventilador1 = Fan(FAST, 10, "yellow", True)
ventilador2 = Fan(MEDIUM) # ventilador2 = Fan(MEDIUM, 5, "blue", False)

print("Informacion del ventilador 1")
print("-Estado:",ventilador1.isON())    
print("-Velocidad:",ventilador1.getSpeep())    
print("-Radio: " + str(ventilador1.getRadius()))   
print("-Color: " + ventilador1.getColor())   
print("\nInformacion del ventilador 2")
ventilador2.printInfo()
 # Cambiar el ventilador 2 a encedido
ventilador2.turnON()
print("\nInformacion del ventilador 2 ahora")
ventilador2.printInfo()


                
        
        