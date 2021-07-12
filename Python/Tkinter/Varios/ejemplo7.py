from tkinter import *

# Crear y configurar la ventana raiz 
ventana = Tk()
ventana['bg'] = 'light gray'

# Paso 3: Crear los widgets y Agregar los widgets en la ventana 
Button(ventana, text="One").grid(row=0, column=0)
Button(ventana, text="Two").grid(row=0, column=1, pady=10)
Button(ventana, text="Three").grid(row=0, column=2)
Button(ventana, text="Four").grid(row=1, column=2)
Button(ventana, text="Five").grid(row=1, column=1)
Button(ventana, text="Six").grid(row=1, column=0)

# Correr la ventana principal
ventana.mainloop()