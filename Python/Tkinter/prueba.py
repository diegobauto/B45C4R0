from tkinter import *
from PIL import ImageTk, Image

def click(event):
    text = event.widget.cget("text")
    
    #Segunda opcion, cambiarle el texto
    #event.widget["text"] = " "
    # print(event.widget.config(COMMAND=print(" ")))
        
    print(text)
    #Eventos para ocultar el boton
    #event.widget.destroy()
    #event.widget.grid_forget()
    #event.widget.grid_remove()
    
ventana = Tk()
botones = "abcdefghijklmnñopqrstuvwxyz"

# Imagenes
img = ImageTk.PhotoImage(Image.open("Python\Tkinter\jaja.png"))
panel = Label(ventana, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

#Frame para añadir el teclado
frame = Frame(ventana, bg="gray", padx=30, pady=30)
frame.pack()

x = 0
y = 0
#Ubicar los botones de a 9 por fila
for i in botones:   
    b = Button(frame, text=i, padx=10, pady=10, font="lucida 20 bold")
    b.grid(row=x, column=y, padx=5, pady=5)
    y += 1
    b.bind("<Button-1>", click)
    if y % 9 == 0:
        x += 1
        y = 0

# Correr
ventana.mainloop()