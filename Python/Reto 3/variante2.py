from pruebas import pruebas_codigo_estudiante

dic = {
"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", 
"G": "--.", "H": "....", "I": "..", "J": "·---", "K": "-.-", "L": ".-..", 
"M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
"R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
"X": "-..-", "Y": "-.--", "Z": "--.."," ": "/"}

def obtenerClave(valor):
    for key,value in dic.items():
        if valor == value:
            return key

def traductor_a_espanol(mensaje_a_traducir):
    mensaje_traducido = ""
    lista = mensaje_a_traducir.split()
    for i in lista:
        mensaje_traducido += obtenerClave(i)
    return mensaje_traducido


pruebas_codigo_estudiante(traductor_a_espanol)