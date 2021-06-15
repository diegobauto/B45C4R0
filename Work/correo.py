import string

n = int(input())
listaAprobados = []

def listAlphabet():
  return list(string.ascii_lowercase)

numeros = ["1","2","3","4","5","6","7","8","9"]
letras = listAlphabet()

def nombreUsuario(correo):
    nombre = correo[0:correo.index("@")]
    nombre = nombre.lower()
    conteo = 0
    for j in nombre:
        if j == "_" or j == "-" or j in letras or j in numeros:
            conteo += 1
    if nombre[0] in letras and conteo == len(nombre):
        return True

def websiteName(correo):
    cantnumeros = 0
    texto = 0
    website = correo[correo.index("@")+1:correo.index(".")]
    for w in website:
        if w in numeros: 
            cantnumeros += 1
        if(w in letras or w in numeros):
            texto += 1
    if(texto==len(website) or cantnumeros>=1):
        return True

def extension(correo):
    conteoLetras = 0
    extension = correo[correo.index(".")+1:]
    longitud = len(extension)
    for e in extension:
        if e in letras:
            conteoLetras += 1
    if(conteoLetras == longitud) and (3>=longitud>=2):
        return True
            
def ordenar(lista):
    for x in range(len(lista)-1,0,-1):
        for i in range(x):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista

def verificarArroba(correo):
    if (correo.count("@") == 1):
        return True


i = 0
while i<n:
    correo = input()
    if (verificarArroba(correo)):
        if(nombreUsuario(correo) and websiteName(correo) and  extension(correo)):
            listaAprobados.append(correo)
    i += 1

print(ordenar(listaAprobados))
print("Validos:"+str(len(listaAprobados)))
print("Invalidos:"+str(n-len(listaAprobados)))