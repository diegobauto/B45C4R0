from nltk import sent_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
import textblob.exceptions
from textblob import Word
from nltk.stem import SnowballStemmer

def translate(status):
    try:
        valor = TextBlob(status.text)
        texto = valor.translate(to="es")
    except textblob.exceptions.TranslatorError:
        texto = "ERROR"
    except textblob.exceptions.NotTranslated:
        texto = "ERROR"
    return texto

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