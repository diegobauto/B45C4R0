class Cubo():
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profudidad = profundidad

    def calcularVolumen(self):
        return self.ancho * self.altura * self.profudidad

ancho = int(input("Digite el ancho: "))
altura = int(input("Digite la altura: "))
profundidad = int(input("Digite la profundidad: "))

cubo1 = Cubo(ancho, altura, profundidad)
print(f"Volúmen del cubo: {cubo1.calcularVolumen()} m^3")