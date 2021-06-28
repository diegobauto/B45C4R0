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
top = Tk() # Create a window
top['bg'] = 'white'
# Paso 3: Crear los widgets
# Paso 4: Agregar los widgets en la ventana 

Button(top, text="Left 1").pack(side='left')
Button(top, text="Left 2").pack(side='left')
Button(top, text="Right 1").pack(side='right')
Button(top, text="Right 2").pack(side='right', padx=10)
Button(top, text="Top 1").pack(side='top')
Button(top, text="Top 2").pack(side='top')
Button(top, text="Bottom 1").pack(side='bottom')
Button(top, text="Bottom 2").pack(side='bottom', pady=10)


# Paso 6: Poner a correr la ventana principal
top.mainloop()



