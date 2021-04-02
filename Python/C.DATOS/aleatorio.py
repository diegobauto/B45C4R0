from random import randint

aleatorio = randint(0,99)
puntaje = 100

print("\nTendra que adivinar un número")
print("Su puntaje inicial es de "+str(puntaje)+" puntos\n")

for i in range(0,10):
    numero = input("Intento "+str(i+1)+":")
    if(int(numero) == aleatorio):
        print("\nJuego Finalizado, !GANO!")
        print("Puntaje:"+str(puntaje)+" puntos")
        break
    if(int(numero) > aleatorio):
        print("PISTA: Su número es mayor")
        puntaje -= 10
    elif(int(numero) < aleatorio):
        print("PISTA: Su número es menor")
        puntaje -= 10
else:
    print("\nJuego Finalizado, !PERDIO!")
    print("Puntaje:"+str(puntaje)+" puntos")