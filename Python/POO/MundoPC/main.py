from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton
from Computadora import Computadora
from Orden import Orden

if __name__ == "__main__":
    monitor1 = Monitor("Acer", "16.5")
    teclado1 = Teclado("Lenovo", "USB")
    raton1 = Raton("HP", "USB")
    monitor2 = Monitor("HP", "14.5")
    raton2 = Raton("ASUS", "Bluetooth")
    computador1 = Computadora("Gamer", monitor1, teclado1, raton1)
    computador2 = Computadora("Gamer2", monitor2, teclado1, raton2)
    
    computadores = [computador1, computador2]

    orden1 = Orden(computadores)
    print(orden1)

    orden2 = Orden([computador2])
    orden2.agregarComputadora(computador1)
    print(orden2)