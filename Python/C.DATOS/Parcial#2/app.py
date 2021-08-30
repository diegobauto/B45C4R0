import tweepy
from NLP import *

class TweetsListener(tweepy.StreamListener):

    def on_connect(self):
        print("Estoy conectado!")

    def on_status(self, status):
        text = NLP.translate(status)
        lista = NLP.tokenizar(text)
        NLP.stopWords(lista)
        
    def on_error(self, status_code):
        print("Error", status_code)

consumer_key = "d45eL2nYhcpeZErDutksjGalp"
consumer_secret = "97ZIS2emajzzvxDpIe4MnlhJev1W35gJPplrlceXZb17VYDGHy"
access_token = "1023626141704306689-UNFsDNQP6e458kNm7X4JXIdBEUo1rK"
access_token_secret = "yKFJdY9cBym1HPEA0lMQyeguFAGFEkCzM1RlwmHMEIsqt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
streamingApi.filter(
    # follow=["151179935"],
    track=["Coronavirus", "Covid"]
)