lista=[]
alumnos=[]

def inicial():
    n = int(input("Digite el numero de estudiantes: "))
    for i in range(1,n+1):
        nombre =input("Nombre: ")
        nota = int(input("Nota:"))
        alumnos.append([nombre, nota])
    lista = alumnos
    return lista

def ordenarNotas(list):
    for x in range(len(list)-1,0,-1):
        for i in range(x):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

def imprimirMenores(list):
    nombresMenor = ""
    menor = list[0][1]
    for i in range(len(list)-1):
        if(list[i][1] == menor):
            nombresMenor += list[i][0] 
    return nombresMenor

def imprimirMayores(list):
    nombresMayor = ""
    menor = list[-1][1]
    for i in range(len(list)-1, 0, -1):
        if(list[i][1] == menor):
            nombresMayor += list[i][0] 
    return nombresMayor

lista  = inicial()
print(lista)
lista = ordenarNotas(lista)
print(lista)
nombresMenor = imprimirMenores(lista)
nombresMayor = imprimirMayores(lista)
print("Menor Calificación: ", nombresMenor)
print("Mayor Calificación: ", nombresMayor)