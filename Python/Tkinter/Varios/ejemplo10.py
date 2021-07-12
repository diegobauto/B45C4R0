from tkinter import *

def restar():
    contador.set(contador.get() - 1)
    if (contador.get() == 0):
        contador.set(10)      
    print(contador.get())

# Crear y configurar la ventana raiz 
ventana = Tk()

# Creacion de variable en Tkinter
contador = IntVar()
contador.set(10)

# Crear los widgets
label_contador = Label(ventana, width=7, textvariable=contador)
button_contador = Button(ventana, text="sumar", command=restar)

# Agregar los widgets en la ventana
label_contador.pack()
button_contador.pack()

# Correr la ventana principal
ventana.mainloop()