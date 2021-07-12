from tkinter import *

# Crear y configurar la ventana raiz 
ventana = Tk() # Create a window

# Crear los widgets
fMain = Frame(ventana)
f1 = Frame(fMain)
f2 = Frame(fMain)
lb1 = Label(f1, text = "Label 1")
lb2 = Label(f1, text = "Label 2")
lb3 = Label(f1, text = "Label 3")
lb4 = Label(f2, text = "Label 4")
lb5 = Label(f2, text = "Label 5")
lb6 = Label(f2, text = "Label 6")

# Agregar los widgets en la ventana 
fMain.pack()
f1.pack()
f2.pack()
lb1.pack(side='left')
lb2.pack(side='left')
lb3.pack(side='left')
lb4.pack(side='right')
lb5.pack(side='right')
lb6.pack(side='right')

# Correr la ventana principal
ventana.mainloop()