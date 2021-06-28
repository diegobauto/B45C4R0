
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
ventana = Tk() # Create a window

# Paso 3: Crear los widgets

fMain = Frame(ventana)
lb1 = Label(fMain , text = "Label 1")
lb2 = Label(fMain , text = "Label 2")
lb3 = Label(fMain , text = "Label 3")
lb4 = Label(fMain , text = "Label 4")
lb5 = Label(fMain , text = "Label 5")
lb6 = Label(fMain , text = "Label 6")

# Paso 4: Agregar los widgets en la ventana 
fMain.pack()

lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)
lb3.grid(row=0, column=2)
lb4.grid(row=1, column=2)
lb5.grid(row=1, column=1)
lb6.grid(row=1, column=0)


# Paso 6: Poner a correr la ventana principal
ventana.mainloop()