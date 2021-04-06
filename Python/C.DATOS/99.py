import numpy as np

a = np.arange(729).reshape(9,9,9)

num1 = int(input("Digite el bloque 1: "))
num2 = int(input("Digite el bloque 2: "))

numero = int(num1/3)*3

#a[[numero, numero+1, numero+3]]

print(a)