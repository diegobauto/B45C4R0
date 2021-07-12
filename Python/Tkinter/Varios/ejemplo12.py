from tkinter import *

# Definir la clase que contenga el frame principal
class ImcGUI(Frame):
    
    # Definir el constructor (Aca se inicializaran los elementos)
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        # Frames
        self.fPeso = Frame(self)
        self.lPeso = Label(self.fPeso, text = "Peso (kg): ")
        self.ePeso = Entry(self.fPeso)
        
        self.fAltura = Frame(self)
        self.lAltura = Label(self.fAltura, text = "Altura (cm): ")
        self.eAltura = Entry(self.fAltura)
        
        self.fIMC = Frame(self)
        self.bIMC = Button(self.fIMC, text = "Calcular IMC", command = self.calcularIMC)
        self.lIMC = Label(self.fIMC, bg = "white")
        
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
        # Obtener los valores del peso y la altura
        peso = float(self.ePeso.get())
        altura = float(self.eAltura.get())
        altura_m = altura/100
        # Calcular
        imc = peso/altura_m**2
        # Modificar el resultado
        self.lIMC['text'] = str(imc)
        
# Invoque la clase prinpipal.
if __name__ == "__main__":
    appIMC = ImcGUI() # Creacion del objeto
    appIMC.mainloop() # Correr la ventana principal