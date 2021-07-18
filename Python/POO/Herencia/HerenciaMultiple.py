class FiguraGeometrica:
    def __init__(self, ancho, alto) -> None:
        self.ancho = ancho
        self.alto = alto

class Color:
    def __init__(self, color) -> None:
        self.color = color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)
        Color.__init__(self, color)

    def calcurarArea(self):
        return self.ancho * self.alto


cuadrado1 = Cuadrado(5,"Azul")
print(cuadrado1.calcurarArea())
print(cuadrado1.color)