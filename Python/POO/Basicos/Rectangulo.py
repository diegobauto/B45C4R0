class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

base = int(input("Digite la base: "))
altura = int(input("Digite la altura: "))

rectangulo1 = Rectangulo(base, altura)
print(f"Área Rectangulo: {rectangulo1.calcularArea()}")
