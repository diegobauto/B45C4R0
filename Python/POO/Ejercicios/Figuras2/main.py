from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

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