texto = "La tercera forma de eliminar un eliminar elementos de una lista con Python es la sentencia"

for i in texto.split():
    if(i[0:4] == "elim"):
        texto.split().remove(i)

print(texto.split())