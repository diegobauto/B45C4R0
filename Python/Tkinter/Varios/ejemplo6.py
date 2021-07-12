from tkinter import *

# Crear y configurar la ventana raiz 
ventana = Tk() # Create una ventana
ventana['bg'] = 'white'

# Crear los widgets y Agregar los widgets en la ventana 
Button(ventana, text="Left 1").pack(side='left')
Button(ventana, text="Left 2").pack(side='left')
Button(ventana, text="Right 1").pack(side='right')
Button(ventana, text="Right 2").pack(side='right', padx=10)
Button(ventana, text="ventana 1").pack(side='ventana')
Button(ventana, text="ventana 2").pack(side='ventana')
Button(ventana, text="Bottom 1").pack(side='bottom')
Button(ventana, text="Bottom 2").pack(side='bottom', pady=10)

# Correr la ventana principal
ventana.mainloop()