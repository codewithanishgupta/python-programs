#  pip install speechrecognition pyaudio
# pip install setuptools  
# pip install pocketsphix  

import speech_recognition as sr
import webbrowser
import pyttsx3
import muzicLybrary
import requests

recognizer = sr.Recognizer()
# engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

newsapi = "242587126bbf45ffbb17cad86d6a2008"

def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        # song = c.lower().split(" ")[1]
        song = c.lower()[5:].strip()
        link = muzicLybrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # parse the json response 
            data = r.json()
            
            # extract the article
            articles = data.get('article', [])
            
            # print the headline 
            for article in articles :
                speak(article['title'])
            
            
if __name__ == "__main__" :
    speak("Initializing jarvis...")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        
        r = sr.Recognizer()
        
        print("Recognizing...")
        
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=3, phrase_time_limit = 3)
                word= r.recognize_google(audio)
                
            
            if "jarvis" in word.lower():
                print("Jarvis Activated!")
                speak("yes anish bro...")
                engine.say("yes anish bro...")
                # listen for cammand 
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source , timeout=5, phrase_time_limit = 3)
                    command = r.recognize_google(audio)
                                
                    processcommand(command)
                
        
        except Exception as e :
            print("Error ; {0}".format(e))