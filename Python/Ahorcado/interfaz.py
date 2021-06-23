from tkinter import *

def letter(letra):
    return letra

def InitWindow():
    window = Tk()
    window.title("Ahorcado")
    window.maxsize(865,600)
    window.minsize(865,600)
    a = Button(window, text="a", width=5, height=3, command=lambda: letter("a")).place(x=200,y=400)
    b = Button(window, text="b", width=5, height=3, command=lambda: letter("b")).place(x=250,y=400)
    c = Button(window, text="c", width=5, height=3, command=lambda: letter("c")).place(x=300,y=400)
    d = Button(window, text="d", width=5, height=3, command=lambda: letter("d")).place(x=350,y=400)
    e = Button(window, text="e", width=5, height=3, command=lambda: letter("e")).place(x=400,y=400)
    f = Button(window, text="f", width=5, height=3, command=lambda: letter("f")).place(x=450,y=400)
    g = Button(window, text="g", width=5, height=3, command=lambda: letter("g")).place(x=500,y=400)
    h = Button(window, text="h", width=5, height=3, command=lambda: letter("h")).place(x=550,y=400)
    i = Button(window, text="i", width=5, height=3, command=lambda: letter("i")).place(x=600,y=400)
    j = Button(window, text="j", width=5, height=3, command=lambda: letter("j")).place(x=200,y=460)
    k = Button(window, text="k", width=5, height=3, command=lambda: letter("k")).place(x=250,y=460)
    l = Button(window, text="l", width=5, height=3, command=lambda: letter("l")).place(x=300,y=460)
    m = Button(window, text="m", width=5, height=3, command=lambda: letter("m")).place(x=350,y=460)
    n = Button(window, text="n", width=5, height=3, command=lambda: letter("n")).place(x=400,y=460)
    ñ = Button(window, text="ñ", width=5, height=3, command=lambda: letter("ñ")).place(x=450,y=460)
    o = Button(window, text="o", width=5, height=3, command=lambda: letter("o")).place(x=500,y=460)
    p = Button(window, text="p", width=5, height=3, command=lambda: letter("p")).place(x=550,y=460)
    q = Button(window, text="q", width=5, height=3, command=lambda: letter("q")).place(x=600,y=460)
    r = Button(window, text="r", width=5, height=3, command=lambda: letter("r")).place(x=200,y=520)
    s = Button(window, text="s", width=5, height=3, command=lambda: letter("s")).place(x=250,y=520)
    t = Button(window, text="t", width=5, height=3, command=lambda: letter("t")).place(x=300,y=520)
    u = Button(window, text="u", width=5, height=3, command=lambda: letter("u")).place(x=350,y=520)
    v = Button(window, text="v", width=5, height=3, command=lambda: letter("v")).place(x=400,y=520)
    w = Button(window, text="w", width=5, height=3, command=lambda: letter("w")).place(x=450,y=520)
    x = Button(window, text="x", width=5, height=3, command=lambda: letter("x")).place(x=500,y=520)
    y = Button(window, text="y", width=5, height=3, command=lambda: letter("y")).place(x=550,y=520)
    z = Button(window, text="z", width=5, height=3, command=lambda: letter("z")).place(x=600,y=520)  
    
