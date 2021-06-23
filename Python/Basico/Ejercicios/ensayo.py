texto = ""
ensayo = ""
conespacio = ""

while ( texto != "-1"):
    texto = input()
    if (texto != "-1"):
        ensayo += texto + " "
        conespacio += texto
longitud = len(ensayo)

def sinEspacio():
    letras = 0
    for i in range(longitud):
        if(ensayo[i] != " "):
            letras += 1
    return letras

def parrafos():
    parrafos = 0
    for i in ensayo:
        if(i == "."):
            parrafos += 1
    return parrafos

def ensayoValido():
    valido = (longitud >= 10)
    return valido

print("Palabras:"+str(len(ensayo.split())))
print("Caracteres con espacio:"+str(len(conespacio)))
print("Caracteres sin espacio:"+str(sinEspacio()))
print("Parrafos:"+str(parrafos()))
print("Ensayo Valido:"+str(ensayoValido()))