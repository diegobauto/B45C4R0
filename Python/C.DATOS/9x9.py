import numpy as np

a = np.arange(729).reshape(9,9,9)
num1 = int(input("Digite el bloque 1: "))
num2 = int(input("Digite el bloque 2: "))

def obtenerBloque(num):
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
    i,e = obtenerBloque(num1)
    f,k = obtenerBloque(num2)
    if(num1>=9 and num1<=17):
        num1 = num1-9
    if(num1>=18 and num1<=26):
        num1 = num1-18
    
    print(f)
    

    k[0:3, num2*3:num2*3+3] = i[0:3, num2*3:num2*3+3]
    
    e[6:9, (num1-6)*3:(num1-6)*3+3] = f[0:3, 0:3]
    
    print("\nRESULTADO FINAL: ")
    #print(a)
    print(a)
    

intercambiar(num1,num2)