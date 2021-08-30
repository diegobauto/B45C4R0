n = int(input())
lista = []
lista1 = []

for i in range(n):
    sexo, edad, per, valoracion = map(str, input().split(" ")) 
    if( per == "positiva"):
        lista.append((edad, per.upper(), valoracion))

lista = sorted(lista, key=lambda x: x[2])

for i in range(0, len(lista)-1):
    if lista[i][2] == lista[i+1][2]:
        lista1.append(lista[i])
        lista.pop(i)
        
print(lista)
print(lista1)
