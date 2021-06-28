# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:49:28 2021

@author: Usuario
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:47:46 2021

@author: Usuario
"""

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
f1 = Frame(fMain)
f2 = Frame(fMain)
lb1 = Label(f1, text = "Label 1")
lb2 = Label(f1, text = "Label 2")
lb3 = Label(f1, text = "Label 3")
lb4 = Label(f2, text = "Label 4")
lb5 = Label(f2, text = "Label 5")
lb6 = Label(f2, text = "Label 6")

# Paso 4: Agregar los widgets en la ventana 
fMain.pack()
f1.pack()
f2.pack()
lb1.pack(side='left')
lb2.pack(side='left')
lb3.pack(side='left')
lb4.pack(side='right')
lb5.pack(side='right')
lb6.pack(side='right')

# Paso 6: Poner a correr la ventana principal
ventana.mainloop()