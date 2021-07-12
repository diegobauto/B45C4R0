from tkinter import *

# Definir la clase que contenga el frame principal
class GUIPateame(Frame):
    
    # Definir el constructor (Aca se inicializaran los elementos)
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