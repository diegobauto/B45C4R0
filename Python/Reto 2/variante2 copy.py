import numpy as np

def solucion(a):
    con = 3
    num = 0

    for i in range(10,len(a)+1,5):
        con += 1

    lista = np.zeros((con,con))
    print(lista)

    for i in range(len(lista)):
        for j in range(len(lista)):
            if(num<=9):
                if j <= i:
                    lista[i][j] = a[num]
                num += 1
    print(lista)

l = [8, 60, 72, 35, 26, 75, 15, 12, 33, 54]
np.array(solucion(l))
