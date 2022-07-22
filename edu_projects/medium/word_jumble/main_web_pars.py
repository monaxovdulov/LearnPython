import requests
import pickle


r = requests.get('https://random-word-api.herokuapp.com/word')
print(r.content.decode())
