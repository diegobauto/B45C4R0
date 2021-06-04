lista = ["O", "S", "O"]

for i in lista:
    if( i == "O"):
        print(lista.index(i))
        lista[lista.index(i)] = "*"

print(lista)