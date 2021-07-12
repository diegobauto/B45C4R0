from tkinter import *

# Crear y configurar la ventana raiz 
ventana = Tk()

# Crear los widgets
fMain = Frame(ventana)
lb1 = Label(fMain , text = "Label 1")
lb2 = Label(fMain , text = "Label 2")
lb3 = Label(fMain , text = "Label 3")
lb4 = Label(fMain , text = "Label 4")
lb5 = Label(fMain , text = "Label 5")
lb6 = Label(fMain , text = "Label 6")

# Agregar los widgets en la ventana 
fMain.pack()
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)
lb3.grid(row=0, column=2)
lb4.grid(row=1, column=2)
lb5.grid(row=1, column=1)
lb6.grid(row=1, column=0)

# Correr la ventana principal
ventana.mainloop()