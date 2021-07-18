from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.ancho * self.alto

    def __str__(self):
        return Color.__str__(self) + "\n"+ FiguraGeometrica.__str__(self)