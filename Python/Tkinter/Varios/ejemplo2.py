# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:18:07 2021

@author: Usuario
"""
# Paso 5: Agregar eventos
# Funcionalidad (logica de la aplicación)


# Paso 1: Importar todo lo que se necesite
from tkinter import *

# Paso 2: Crear y configurar la ventana raiz 
ventanaPrincipal = Tk() # Create a window

# Paso 3: Crear los widgets
frame = Frame(ventanaPrincipal)
lb1 = Label(frame, text = "Label 1")
lb2 = Label(frame, text = "Label 2")
lb3 = Label(frame, text = "Label 3")

# Paso 4: Agregar los widgets en la ventana 
frame.pack()
lb1.pack()
lb2.pack()
lb3.pack()

# Paso 6: Poner a correr la ventana principal
ventanaPrincipal.mainloop()


