import numpy as np

a = np.arange(729).reshape(9,9,9)
aux = np.arange(729).reshape(9,9,9)
num1 = int(input("Digite el bloque 1: "))
num2 = int(input("Digite el bloque 2: "))
print(a)

def bloques(b1,b2,num):
    if(num>=0 and num<=2): 
        b1[0:3, num*3:num*3+3] = b2[0:3, 0:3]
    elif(num>=3 and num<=5):  
        b1[3:6, (num-3)*3:(num-3)*3+3] = b2[0:3, 0:3]
    elif(num>=6 and num<=8): 
        b1[6:9, (num-6)*3:(num-6)*3+3] = b2[0:3, 0:3]

def obtenerNum(num):
    if(num>=9 and num<=17):
        num = num-9
    if(num>=18 and num<=26):
        num = num-18
    return num

def obtenerBloque(a,num):
    #numero del bloque divido en 3, Obtendria el elemento #? de mi matriz
    elemento = a[int(num/9)]
    num = obtenerNum(num)
    #Obtener bloque
    if(num>=0 and num<=2):
        bloque = elemento[0:3, num*3:num*3+3].reshape(3,3)
    elif(num>=3 and num<=5):
        bloque = elemento[3:6, (num-3)*3:(num-3)*3+3].reshape(3,3)
    elif(num>=6 and num<=8):
        bloque = elemento[6:9, (num-6)*3:(num-6)*3+3].reshape(3,3)
    return bloque, elemento
    
def intercambiar(num1, num2):
    i,e = obtenerBloque(a, num1)
    f,k = obtenerBloque(a, num2)
    m,n = obtenerBloque(aux, num2)
    num1 = obtenerNum(num1)
    num2 = obtenerNum(num2)
    bloques(k,i,num2)
    bloques(e,m,num1)
    print("\nRESULTADO FINAL:\n")
    print(a)
    
intercambiar(num1,num2)