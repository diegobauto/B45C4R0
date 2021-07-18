#ABC = Abstract Base Class
from abc import ABC, abstractmethod

"""
Una clase abstracta tiene las siguientes caracteristicas:
1. Tiene un metodo abstaracto, haciendo que la clase sea abstracta -> este metodo no tiene implementacion
2. No se puede instanciar (no podemos crear objetos)
3. Sus clases hijas tienen(obligartoriamente) que implementar sus metodos abstractos
"""

#Convertimos la clase en una clase abstracta
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    #Se considera como un metodo abstracto
    @abstractmethod
    def calcularArea(self):
        pass #No contiene implementacion

    def __str__(self):
        return f"Ancho: {self._ancho} - Alto: {self._alto}"

if __name__ == "__main__":
    figura = FiguraGeometrica() #No podemos instanciar una clase abstracta