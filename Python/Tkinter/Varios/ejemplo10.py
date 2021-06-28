# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:32:10 2021

@author: Usuario
"""


# Paso 1: Importar todo lo que se necesite
import tkinter as tk

# Paso 5: Agregar eventos
# Funcionalidad (logica de la aplicación)
def count():
    counter.set(counter.get() + 1)   # counter = counter + 1
    if (counter.get() >= 10):
        counter.set(0)      
    print(counter.get())

# Paso 2: Crear y configurar la ventana raiz 
root = tk.Tk()

# Paso 3: Definir variables Tkinter
counter = tk.IntVar()
counter.set(0)

# Paso 3: Crear los widgets
label_counter = tk.Label(root, width=7)
label_counter['textvariable'] = counter

button_counter = tk.Button(root, text="Count")
button_counter['command'] = count

# Paso 4: Agregar los widgets en la ventana 
label_counter.pack()
button_counter.pack()

# Paso 6: Poner a correr la ventana principal
print("Valor inicial de counter", counter.get())
root.mainloop()
