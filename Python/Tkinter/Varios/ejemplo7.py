# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:06:16 2021

@author: Usuario
"""

# Paso 5: Agregar eventos
# Funcionalidad (logica de la aplicación)


# Paso 1: Importar todo lo que se necesite
from tkinter import *

# Paso 2: Crear y configurar la ventana raiz 
top = Tk() # Create a window
top['bg'] = 'light gray'

# Paso 3: Crear los widgets
# Paso 4: Agregar los widgets en la ventana 
Button(top, text="One").grid(row=0, column=0)
Button(top, text="Two").grid(row=0, column=1, pady=10)
Button(top, text="Three").grid(row=0, column=2)
Button(top, text="Four").grid(row=1, column=2)
Button(top, text="Five").grid(row=1, column=1)
Button(top, text="Six").grid(row=1, column=0)

# Paso 6: Poner a correr la ventana principal
top.mainloop()


