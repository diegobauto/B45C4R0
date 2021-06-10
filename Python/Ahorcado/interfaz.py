import tkinter

abecedario = "abcdefghijklmnñopqrstuvwxyz"


def obtenerTextoBoton(lista,indice):
    print(lista[indice].config("text")[-1])

def InitWindow():
    window = tkinter.Tk()
    window.maxsize(900,600)
    window.minsize(900,600)

    row = 0
    column = 0
    lista = []
    for i in abecedario: 
        lista.append(tkinter.Button(window, text=i, width=5, height=3))
    
    for j in range(27):
        print(lista[j].config("text")[-1])
        column += 1
        lista[j].grid(row = row, column = column)
    lista[j].config(command=lambda:print(j))
    #print(lista[1].grid(row = row, column = column))
    #print(lista[1].config(command=lambda:print(lista[1].config("text"))))
    
    """
    for j in range(27):
        for i in abecedario:
            boton = tkinter.Button(window, text=i, width=5, height=3, command=lambda: print(boton[j].config("text")[-1]))
            if column%9 == 0:
                row += 1
                column = 0
                boton.grid(row = row, column = column)
            else:
                boton.grid(row = row, column = column)
            column += 1
    """

    """
    btnlista = []
   
    for i in range(3):
        btnlista.append([])
        for j in range(9):
            btnlista[i].append(tkinter.Button(window))
            btnlista[i][j].config(bg="white", borderwidth=1, activebackground = "black", relief = "solid")
            btnlista[i][j].place(relx=0.1 + 0.1*j, rely=0.1 + 0.1*i, relwidth = 0.1, relheight=0.1)
            for x in range(27):
                btnlista[i][j].config(text = abecedario[x])
    """
    
    window.mainloop()
    window.pack()
