from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = 0
while opcion>1 or opcion<4:
    print()
    print("Menu".center(30, "-"))
    print("1. Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar pelicula")
    print("4. Eliminar archivo de películas")
    print("5. Salir")
    opcion = int(input("Opción: "))

    if opcion == 1:
        nombre = input("Digite el nombre: ")
        pelicula = Pelicula(nombre)
        CatalogoPeliculas.agregarPelicula(pelicula)
    elif opcion == 2:
        CatalogoPeliculas.listarPeliculas()
    elif opcion == 3:
        indice = int(input("Digite el indice de la pelicula a eliminar: "))
        CatalogoPeliculas.eliminarPelicula(indice)
    elif opcion == 4:
        CatalogoPeliculas.eliminarArchivo()
    elif opcion == 5:
        print("Saliendo")
        break