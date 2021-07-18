from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

"""
Una clase abstracta tiene las siguientes caracteristicas:
1. Tiene un metodo abstaracto, haciendo que la clase sea abstracta -> este metodo no tiene implementacion
2. No se puede instanciar (no podemos crear objetos)
3. Sus clases hijas tienen(obligartoriamente) que implementar sus metodos abstractos
"""

if __name__ == "__main__":
    print("Cuadrado".center(50, "-"))
    cuadrado1 = Cuadrado(5, "Rojo")
    print(cuadrado1)
    print(f"Area: {cuadrado1.calcularArea()}")

    print()

    print("Rectangulo".center(50, "-"))
    rectangulo1 = Rectangulo(3,8,"Verde")
    print(rectangulo1)
    print(f"Area: {rectangulo1.calcularArea()}")

    #Methon Resolution Order, saber la jerarquia de clases
    print(Cuadrado.mro())