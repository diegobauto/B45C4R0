from tkinter import *

# Crear y configurar la ventana raiz 
ventanaPrincipal = Tk() # Create a window

# Crear los widgets
frame = Frame(ventanaPrincipal)
lb1 = Label(frame, text = "Label 1")
lb2 = Label(frame, text = "Label 2")
lb3 = Label(frame, text = "Label 3")

# Agregar los widgets en la ventana 
frame.pack()
lb1.pack(side='left')
lb2.pack(side='left')
lb3.pack(side='left')

# Correr la ventana principal
ventanaPrincipal.mainloop()