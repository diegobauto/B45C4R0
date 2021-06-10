from circulo import Circulo
from cuadrado import Cuadrado
from funciones import menu

if __name__ == '__main__':
    print("PROGRAMA PARA CALCULAR AREAS")
    while(True):
        opc = menu()
        if (opc == 1):
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            cuadrado.printInfo()
        elif (opc == 2):
            radio = float(input("Ingrese el radio del circulo: "))
            circulo = Circulo(radio)
            circulo.printInfo()
        elif (opc == 3):
            print("Saliendo ...")
            break
        else:
            print("ERROR: Opcion invalida")
        print()