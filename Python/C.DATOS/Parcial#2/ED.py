import nltk
from textblob.blob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analisisSentimientos(texto):
    texto_text = TextBlob(texto)
    print(texto_text.sentiment)

def analisisSentimientosNltk(texto):
    tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
    frases = tokenizer.tokenize(texto)
    analizador = SentimentIntensityAnalyzer()
    for sentence in frases:
        print(sentence)
        scores = analizador.polarity_scores(sentence)
        for key in scores:
            print(key, ': ', scores[key])