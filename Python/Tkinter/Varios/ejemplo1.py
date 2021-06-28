# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:18:07 2021

@author: Usuario
"""
# Paso 5: Agregar eventos
# Funcionalidad (logica de la aplicación)
def eventoClick():
    print("Pateame!!!")

# Paso 1: Importar todo lo que se necesite
from tkinter import *

# Paso 2: Crear y configurar la ventana raiz 
root = Tk() # Create a window
root.title("Ejemplo 1")
# Paso 3: Crear los widgets
label = Label(root, text = "Welcome to Python") # Creando un label
button = Button(root, text = "Click Me", command = eventoClick) # Creando un boton

# Paso 4: Agregar los widgets en la ventana 
label.pack() # Colocando el label en la ventana raiz
button.pack() # Colocando el boton en la ventana raiz

# Paso 6: Poner a correr la ventana principal
root.mainloop()
