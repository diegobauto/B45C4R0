# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:49:00 2021

@author: Usuario
"""

# Paso 1: Importar todo lo que se necesite
from tkinter import *

# Paso 2: Defina la clase que contenga el frame principal
class ImcGUI(Frame):
    
    # Paso 3: Defina el constructor (Aca se inicializaran los elementos)
    def __init__(self, master = None):
        Frame.__init__(self, master)
        # Code
        
        # Variables para el calculo de la IMC
        # self.imc = DoubleVar()
        
        # Frames
        self.fPeso = Frame(self)
        self.lPeso = Label(self.fPeso, text = "Peso (kg): ")
        self.ePeso = Entry(self.fPeso)
        
        
        self.fAltura = Frame(self)
        self.lAltura = Label(self.fAltura, text = "Altura (cm): ")
        self.eAltura = Entry(self.fAltura)
        
        
        self.fIMC = Frame(self)
        self.bIMC = Button(self.fIMC, text = "Calcular IMC", command = self.calcularIMC)
        #self.lIMC = Label(self.fIMC, textvariable = self.imc, bg = "white")
        self.lIMC = Label(self.fIMC, bg = "white")
        #self.lPeso = Label()
        
        self.inicializarFrames()
        
    def inicializarFrames(self):
        self.pack()
        
        self.fPeso.pack()
        self.lPeso.pack(side='left')
        self.ePeso.pack(side='left')
        
        self.fAltura.pack()
        self.lAltura.pack(side='left')
        self.eAltura.pack(side='left')
        
        self.fIMC.pack()
        self.bIMC.pack(side='left')
        self.lIMC.pack(side='left')
        
    
        
    def calcularIMC(self):
        print("Calculo del IMC")
        # 1. Obtener los valores del peso y la altura
        peso = float(self.ePeso.get())
        altura = float(self.eAltura.get())
        altura_m = altura/100
        # 2. Calculos
        imc = peso/altura_m**2
        # 3. Despliega el resultado
        #self.imc.set(imc)
        self.lIMC['text'] = str(imc)
        


# Invoque la clase prinpipal.
if __name__ == "__main__":
    appIMC = ImcGUI()
    appIMC.mainloop()