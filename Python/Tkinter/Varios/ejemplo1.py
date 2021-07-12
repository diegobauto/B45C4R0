from tkinter import *

def eventoClick():
    print("Pateame!!!")

# Crear y configurar la ventana raiz 
root = Tk() # Create a window
root.title("Ejemplo 1")

# Crear los widgets
label = Label(root, text = "Welcome to Python") # Creando un label
button = Button(root, text = "Click Me", command = eventoClick) # Creando un boton

# Agregar los widgets en la ventana 
label.pack() # Colocando el label en la ventana raiz
button.pack() # Colocando el boton en la ventana raiz

# Correr la ventana principal
root.mainloop()