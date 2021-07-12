from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image
from random  import *

ventana = Tk()
ventana.title("JUEGO - AHORCADO") #ventana Principal
frameContendor = Frame(ventana) #Frame para contener todos los elementos

# Variables
filas = 0 #Controlar las filas del teclado
columnas = 0 #Controlar las columnas del teclado
normal = ["HOLA", "OSO", "AMOR", "ADIOS"]
hard = ["DELICIOSO", "ROMANTICO", "TAMARINDO", "PROGRAMACION"]
botones = "abcdefghijklmnñopqrstuvwxyz".upper()
#Número de intentos
contador = IntVar()
contador.set(10)

#Menu de selección, normal o dificil, se escoge aleatorio
option = randint(1,2)
if option == 1:
    palabra = choice(normal)
elif option == 2:
    palabra = choice(hard)
palabraAdivinar = list(palabra) #Palabra que se debe adivinar (lista)
listaLineas = list("_"*len(palabra)) #Palabra a adivinar con lineas lista)


def restarIntentos():
    contador.set(contador.get() - 1)   # contador = contador + 1
    if (contador.get() == 0):
        MessageBox.showerror("¡GAME OVER!", "Lo sentimos, ha perdido el juego")      
        ventana.destroy()


def click(event):
    letraOprimida = event.widget["text"]
    #letraOprimida = event.widget.cget("text")
    event.widget["text"] = " " #Pone el boton en vacío

    if letraOprimida in palabraAdivinar:
        for i in palabraAdivinar:
            if i == letraOprimida:
                listaLineas[palabraAdivinar.index(i)] = i
                label["text"] = listaLineas
                palabraAdivinar[palabraAdivinar.index(i)] = "*"
        if palabraAdivinar.count("*") == len(palabraAdivinar) :
            MessageBox.showinfo("¡GANADOR!", "Has ganado la partida")
            ventana.destroy()
    else:
        if letraOprimida == " ":
            MessageBox.showwarning("Alerta!", "Ya habias seleccionado la letra anteriormente")
        else:
            MessageBox.showerror("Intento fallido", "La letra digitada no es correcta")
            restarIntentos() 

    """ Eventos para ocultar el boton """
    #event.widget.destroy()
    #event.widget.grid_forget()
    #event.widget.grid_remove()
    #Segunda opcion, cambiarle el texto a vacio
    #event.widget["text"] = " "
    #print(event.widget.config(COMMAND=print(" ")))


"""------------------ IMAGENES ------------------ """
imagen = ImageTk.PhotoImage(Image.open("Python\Tkinter\Ahorcado\imagen.jpg"))
panel = Label(frameContendor, image = imagen)
panel.pack(side = "left", fill = "both", expand = "yes")


"""------------------ INTENTOS ------------------ """
frameIntentos = Frame(frameContendor)
intentos = Label(frameIntentos, font="lucida 10 bold", text="INTENTOS:", fg="red")
label_contador = Label(frameIntentos, font="lucida 10 bold", textvariable=contador, fg="red")
intentos.pack(side=LEFT)
label_contador.pack(side=RIGHT)
frameIntentos.pack()

"""------------------ AÑADIR LA PALABRA A ADIVINAR ------------------"""
label = Label(frameContendor, text=listaLineas, font="lucida 50 bold")
label.pack(fill = "both", expand = "yes")


"""------------- TECLADO ---------------"""
frame = Frame(frameContendor, bg="gray", padx=30, pady=30) #Frame para añadir el teclado
#Ubicar los botones de a 9 por fila
for i in botones:   
    boton = Button(frame, text=i, padx=10, pady=10, font="lucida 20 bold")
    boton.grid(row=filas, column=columnas, padx=5, pady=5)
    columnas += 1
    boton.bind("<Button-1>", click)
    if columnas % 9 == 0:
        filas += 1
        columnas = 0
frame.pack(padx=30, pady=30)


#Despues de añadir todos los elementos agrego el frame contenedor a la ventana
frameContendor.pack(padx=20, pady=20) 

# Correr la ventana
ventana.mainloop()