from Producto import Producto
from Orden import Orden

if __name__ == "__main__":
    p1 = Producto("LAPIZ", 800)
    p2 = Producto("BORRADOR", 650)
    p3 = Producto("TAJALAPIZ", 400) 

    productos1 = [p1, p2, p3]

    orden1 = Orden(productos1) #Para varios productos
    orden1.agregarProducto(p2)
    print(orden1)
    print(orden1.calcularTotal())
    
    orden2 = Orden([p2]) #Toca pasarlo como lista ya que deberian ser varios productos (iterable)
    orden2.agregarProducto(p1) #Solo un producto
    print(orden2)
    print(orden2.calcularTotal())