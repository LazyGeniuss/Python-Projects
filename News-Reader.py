import requests
import json
from win32com.client import Dispatch

x = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=122ff683cc0b4ff4a48a8c8718b11919").text
y = json.loads(x)
z = y.get("articles")

speak = Dispatch("SAPI.SpVoice")
for i in range(0,5):
    speak.Speak(z[i].get("description"))