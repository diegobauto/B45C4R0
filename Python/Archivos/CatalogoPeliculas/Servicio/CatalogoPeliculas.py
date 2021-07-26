import os
from sys import path

class CatalogoPeliculas:
    rutaArchivo = "Python\\Archivos\\CatalogoPeliculas\\peliculas.txt"

    @classmethod #Un metodo de clase me permite con cls acceder a las variables de clase
    def agregarPelicula(cls, Pelicula):
        with  open(f"{cls.rutaArchivo}", "a", encoding="utf8") as archivo:
            archivo.write(f"{Pelicula.__str__()}\n")


    @classmethod
    def listarPeliculas(cls):
        try:
            with open(cls.rutaArchivo, "r") as archivo:
                print()
                print("Catalogo de Peliculas".center(50,"-"))
                #print(archivo.read()) #Me imprime las peliculas normal
                lineas = archivo.readlines()
                for i in range(len(lineas)):
                    print(f"{i+1}.{lineas[i]}")
        except:
            print("Verifique que el archivo exista")
        
    @classmethod
    def eliminarPelicula(cls, indice):
        try: 
            with open(cls.rutaArchivo, "r") as f:
                    lines = f.readlines()
                    nombreEliminar = lines[indice-1]
                    lines.remove(nombreEliminar)
            with open(cls.rutaArchivo, "w") as f:
                for line in lines:
                    f.write(line)
            print(f"Pelicula: {nombreEliminar} -> Eliminada correctamente")
            if len(lines) == 0:
                cls.eliminarArchivo()
        except:
            print("La pelicula no existe")


    @classmethod 
    def eliminarArchivo(cls):
        try:
            os.remove(cls.rutaArchivo)
            print("Archivo eliminado correctamente")
        except:
            print("Verifique que el archivo exista")