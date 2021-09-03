from nltk import sent_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
import textblob.exceptions
from textblob import Word
from nltk.stem import SnowballStemmer
from ED import *

def main(status):
    try:
        valor = TextBlob(status.text)
        texto = valor.translate(to="es")
        lista = tokenizar(texto)
        texto = stopWords(lista)
        texto = eliminarAcentos(texto)
        texto = eliminarCaracteres(texto)
        texto = manejoUrl(texto)
        texto = steamming(lematizar(texto))
        #texto = lematizar(steamming(texto))
        print("\n")
        analisisSentimientosNltk(texto)
        analisisSentimientos(texto)
    except textblob.exceptions.TranslatorError:
        print("ERROR")
    except textblob.exceptions.NotTranslated:
        print("ERROR")

def tokenizar(text):
    texto = sent_tokenize(str(text))
    return texto

def stopWords(lista):
    texto = ""
    palabras_vacias = set(stopwords.words('spanish'))
    palabras_vacias.add("RT")
    for i in lista:
        palabras = i.split()
        for palabra in palabras:
            if palabra not in palabras_vacias:
                texto += palabra.lower() + " "
    return texto

def eliminarAcentos(texto):
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for acen in acentos:
        if acen in texto:
            texto = texto.replace(acen, acentos[acen])
    return texto

def eliminarCaracteres(texto):
    text = ""
    for i in texto:
        if (i.isalnum() or i==" "):
            text += i + ""
    return text

def steamming(texto):
    text = ""
    for i in texto.split():
        text += SnowballStemmer('spanish').stem(i) + " "
    return text

def lematizar(texto):
    text = ""
    for i in texto.split():
        text += Word(i).lemmatize() + " "
    return text

def manejoUrl(texto):
    lista = texto.split()
    text = ""
    for i in range(len(lista)):
        if len(lista[i])>3 and lista[i][0:4] == "http":
            lista[i] = "*"
    for j in lista:
        if j != "*":
            text += j + " "   
    return text
