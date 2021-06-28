# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:15:56 2021

@author: Usuario
"""

# Paso 5: Agregar eventos
# Funcionalidad (logica de la aplicación)


# Paso 1: Importar todo lo que se necesite
from tkinter import *

# Paso 2: Crear y configurar la ventana raiz 
root = Tk() # Create a window

# Paso 3: Crear los widgets
frame1 = Frame(root, bg = '#46BDBD')         # Colores en: https://htmlcolorcodes.com/es/
b1_1 = Button(frame1, text="One", fg='red')
b1_2 = Button(frame1, text="Two")
b1_3 = Button(frame1, text="Three")

frame2 = Frame(root, bg='cyan')
b2_1 = Button(frame2, text="Big Fat Four")
b2_2 = Button(frame2, text="Five")
b2_3 = Button(frame2, text="Six")

# Paso 4: Agregar los widgets en la ventana 
frame1.pack(side = LEFT)
b1_1.grid(row = 0,column = 0, padx = 20)
b1_2.grid(row = 0, column = 1, pady=10)
b1_3.grid(row=0, column=2)

frame2.pack(side = 'right')
b2_1.pack(side=TOP)
b2_2.pack(side='top')
b2_3.pack(side='top')

# Paso 6: Poner a correr la ventana principal
root.mainloop()


