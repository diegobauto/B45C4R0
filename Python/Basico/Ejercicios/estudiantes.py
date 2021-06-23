alumnos=[]
notas=[]

def ordenar(lista):
    for x in range(len(lista)-1,0,-1):
        for i in range(x):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista

n = int(input())

for x in range(n):
    nom=input()
    alumnos.append(nom)
    no=float(input())
    notas.append(no)

for k in range(n-1):
    for x in range(n-1-k):
        if notas[x]<notas[x+1]:
            aux1=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux1
            aux2=alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux2


mayores = []
menores = []
for x in range(n):
    if (notas[x] ==  notas[0]):
        mayores.append(alumnos[x])   
    elif (notas[x] ==  notas[-1]):
        menores.append(alumnos[x])


mayores = ordenar(mayores)
menores = ordenar(menores)

for ma in mayores:
    print(ma)

for me in menores:
    print(me)