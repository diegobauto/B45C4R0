from tkinter import *

# Crear y configurar la ventana raiz 
root = Tk()

# Crear los widgets
frame1 = Frame(root, bg = '#46BDBD')
b1_1 = Button(frame1, text="One", fg='red')
b1_2 = Button(frame1, text="Two")
b1_3 = Button(frame1, text="Three")
frame2 = Frame(root, bg='cyan')
b2_1 = Button(frame2, text="Big Fat Four")
b2_2 = Button(frame2, text="Five")
b2_3 = Button(frame2, text="Six")

# Agregar los widgets en la ventana 
frame1.pack(side = LEFT)
b1_1.grid(row = 0,column = 0, padx = 20)
b1_2.grid(row = 0, column = 1, pady=10)
b1_3.grid(row=0, column=2)
frame2.pack(side = 'right')
b2_1.pack(side=TOP)
b2_2.pack(side='top')
b2_3.pack(side='top')

# Correr la ventana principal
root.mainloop()