import numpy as np
from numpy.lib import math
from numpy.matrixlib import mat

a = np.arange(729).reshape(9,9,9)
aux = np.arange(729).reshape(9,9,9)
num1 = int(input("Digite el bloque 1: "))
num2 = int(input("Digite el bloque 2: "))

print(a)

def obtenerBloque(a,num):
    #numero del bloque divido en 3, Obtendria el elemento #? de mi matriz
    elemento = a[int(num/9)]
    if(num>=9 and num<=17):
        num = num-9
    if(num>=18 and num<=26):
        num = num-18
    #Obtener mi primer bloque
    if(num>=0 and num<=2):
        bloque_inicial = elemento[0:3, num*3:num*3+3].reshape(3,3)
    elif(num>=3 and num<=5):
        bloque_inicial = elemento[3:6, (num-3)*3:(num-3)*3+3].reshape(3,3)
    elif(num>=6 and num<=8):
        bloque_inicial = elemento[6:9, (num-6)*3:(num-6)*3+3].reshape(3,3)
    return bloque_inicial, elemento
    
def intercambiar(num1, num2):
    i,e = obtenerBloque(a, num1)
    f,k = obtenerBloque(a, num2)
    m,n = obtenerBloque(aux, num2)

    if(num1>=9 and num1<=17):
        num1 = num1-9
    if(num1>=18 and num1<=26):
        num1 = num1-18

    if(num2>=9 and num2<=17):
        num2 = num2-9
    if(num2>=18 and num2<=26):
        num2 = num2-18

    #k[0:3, num2*3:num2*3+3] = i[0:3, num2*3:num2*3+3]
    #e[6:9, (num1-6)*3:(num1-6)*3+3] = m[0:3, 0:3]

    if(num2>=0 and num2<=2): 
        k[0:3, num2*3:num2*3+3] = i[0:3, 0:3]
    elif(num2>=3 and num2<=5):  
        k[3:6, (num2-3)*3:(num2-3)*3+3] = i[0:3, 0:3]
    elif(num2>=6 and num2<=8): 
        k[6:9, (num2-6)*3:(num2-6)*3+3] = i[0:3, 0:3]

    if(num1>=0 and num1<=2): 
        e[0:3, num1*3:num1*3+3] = m[0:3, 0:3]
    elif(num1>=3 and num1<=5):  
        e[3:6, (num1-3)*3:(num1-3)*3+3] = m[0:3, 0:3]
    elif(num1>=6 and num1<=8): 
        e[6:9, (num1-6)*3:(num1-6)*3+3] = m[0:3, 0:3]
    
    print("\nRESULTADO FINAL: ")
    print(a)
    
intercambiar(num1,num2)