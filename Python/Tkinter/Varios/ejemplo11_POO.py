# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:00:02 2021

@author: Usuario
"""

# Paso 1: Importar todo lo que se necesite
from tkinter import *

# Paso 2: Defina la clase que contenga el frame principal
class GUIPateame(Frame):
    
    # Paso 3: Defina el constructor (Aca se inicializaran los elementos)
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.label = Label(self, text = "Welcome to Python") 
        self.button = Button(self, text = "Click Me", command = self.eventoClick)  
        self.distribuirElementosGraficos()
        
    
    def distribuirElementosGraficos(self):
        self.pack()
        self.label.pack()
        self.button.pack()
    
    # Defina los demas metodos
    def eventoClick(self):
        print("Pateame")


# Invoque la clase prinpipal.
if __name__ == "__main__":
    app = GUIPateame()
    app.mainloop()


"""
from tkinter import *

def eventoClick():
  print("Pateame!!!")

root = Tk() 
label = Label(root, text = "Welcome to Python") 
button = Button(root, text = "Click Me", command = eventoClick) 
label.pack()
button.pack() 
root.mainloop()
"""