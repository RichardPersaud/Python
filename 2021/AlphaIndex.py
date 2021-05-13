#importing the modules / packages
import pyttsx3
import os
import speech_recognition as sr
import requests
from gtts import gTTS
import re
import webbrowser
import smtplib
import json
import datetime
import array
import google
from bs4 import BeautifulSoup
import socket
import subprocess
import shutil
import winsound
import time
import csv
# ===========================

import json

myjson = open('2021/config.json','r')
jsondata = myjson.read()

obj = json.loads(jsondata)

list= obj['1.0']
for i in range(len(list)):
    # print(list[i].get('Name'))
    IndexName = list[i].get('Name').upper()
    Rate = list[i].get('SpeechRate')
    Volume = list[i].get('SpeechVolume')
    Voice = list[i].get('SpeechVoice')
# print(Name)

# ==========================================================================

engine = pyttsx3.init()

# VOICE SETTINGS =========================================================
rate = engine.getProperty("rate")
engine.setProperty("rate", Rate)

volume = engine.getProperty("volume")
engine.setProperty("volume", Volume)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[Voice].id)
# ==================================================================

# with open('2021/config.csv', 'r') as fd:
#     reader = csv.reader(fd)
    
#     for line in reader:
#         print(line)
# ==================================================================
import winsound
import wikipedia

try: 
    # ==========================================================
    os.system('cls')
    winsound.Beep(500,800)
    print("\n********* Booting Up! *********")

    intro = IndexName+", Powering up! "
    engine.say(intro)
    engine.runAndWait()

    def main():
        listen = True
        websites = ["Google", "YouTube", "Reddit", "Twitch", "Twitter", "Amazon", "eBay"]

        if listen == False:
            print("\nListening is 'OFF'")
            exit()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            winsound.Beep(1000,100)
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source)
            speak = r.recognize_google(audio,language='en')

            try:

                if speak.upper() == IndexName:
                    while listen == True:
                        
                        winsound.Beep(1000,100)
                        winsound.Beep(1000,500)
                    
                        # os.system('cls')
                        print("listening....")
                        
                        aud = r.listen(source)
                        r.adjust_for_ambient_noise(source)
                        spk = r.recognize_google(aud,language='en')
                        word=spk.split(" ")
                        
                        def ecc(sys):
                            winsound.Beep(1000,100)
                            engine.say(sys)
                            engine.runAndWait()

                        if word[0] == "open" or "search":
                            if word[1] in websites:
                                sys = "opening "+word[1]+"...."
                                ecc(sys)
                                url = 'https://www.'+word[1]+'.com/'
                                webbrowser.open(url)
                                print("You said " + speak)
                                main()
                            elif word[1] == 'localhost':
                                sys = "opening "+word[1]+"...."
                                ecc(sys)
                                url = 'http://'+word[1]+':8012'
                                webbrowser.open(url)
                                main()
                            elif word[1] == 'Wikipedia':
                                def searcher(question):
                                    ans = wikipedia.summary(question).split('.')
                                    for line in ans:
                                        print(line)
                                if(word[2]=='for'):
                                    continue
                                else:
                                    question = word[2]
                                    searcher(question)
                                    main()

                            else:
                                sys = "Searching for "+ word[1]
                                ecc(sys)
                                search = word[1] 
                                url = 'https://www.'+search+'.com/'
                                webbrowser.open(url)
                                print("You said " + speak)
                                main()
                                time.sleep(1)
                                
                            time.sleep(1)
                        time.sleep(1)

                    return r.recognize_sphinx(audio)
                else:
                    print("You said " + speak)
                    main()
         
            except sr.UnknownValueError:
                os.system('cls') 
                main()
               
    main()

except sr.UnknownValueError:
    print("Could not understand")
    os.system('cls') 
    main()


