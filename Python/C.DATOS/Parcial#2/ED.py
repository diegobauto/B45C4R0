from textblob.blob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv

data = []

def analisisSentimientos(texto):
    analizador = SentimentIntensityAnalyzer()
    scores = analizador.polarity_scores(texto)
    texto_text = TextBlob(texto)
    datos = texto_text.sentiment
    print("Frase: ",  texto)
    print("Polaridad: ",  datos[0])
    print("Subjetividad: ", datos[1])
    print("Negativo: ",  scores["neu"])
    print("Neutro: ",  scores["neg"])
    print("Positivo: ",  scores["pos"])
    print("Compuesto: ",  scores["compound"])
    data.append([texto, datos[0], datos[1], scores["neu"], scores["neg"],scores["pos"], scores["compound"]])
    dataFrame(data)
    
def dataFrame(data):
    with open("Python\\C.Datos\\Parcial#2\\dataframe.csv", "w", newline="", encoding="utf-8") as file:
        file = csv.writer(file, delimiter=",")
        file.writerows([["Frase", "Polaridad", "Subjetividad", "Negativo", "Neutro", "Positivo", "Compuesto"]])
        file.writerows(data)