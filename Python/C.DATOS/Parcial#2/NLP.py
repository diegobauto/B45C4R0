from typing import List
import nltk
from nltk import text
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import textblob.exceptions


class NLP():

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
        #print("LISTA:",lista)
        for i in lista:
            palabras = i.split()
            for palabra in palabras:
                if palabra not in palabras_vacias:
                    texto += palabra + " "
        print(texto)