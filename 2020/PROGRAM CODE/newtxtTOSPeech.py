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
# ===========================

engine = pyttsx3.init()

# VOICE SETTINGS =========================================================
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)

volume = engine.getProperty("volume")
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
# ==================================================================





# DEFINITIONS ======================================================

# LOGS ===========
def system_log(sys):
    with open('log.txt', 'a') as f:
        now = datetime.datetime.now()
        data = (sys)
        f.write("Log:"+str(now)+": System: "+data+ " \n")
def user_log(speak):
    with open('log.txt', 'a') as f:
        now = datetime.datetime.now()
        data = (speak)
        f.write("Log:"+str(now)+": User: "+data+ " \n")
def show_logs():
    print("Logs:")
# =================

# CREATE CODING PROJECTS ============
def create_project():
    print("Creating Coding Project....")
    engine.say("what type of project would you like to work on today?")
    engine.runAndWait()

    print("\n0 - HTML/CSS \n1 - ANGULAR \n2 - FLUTTER \n3 - REACT_JS \n")
    sel = input("Project Type")

    if sel.lower() == "exit":
        main()

    project = input('Enter name of Project: ')

    if project.lower() == "exit":
        main()

    if sel == '0':
        choice = input(
            "\nEnter Project type:\n" +
            "\n0 - Basic HTML/CSS/JS" +
            "\n1 - Advance PHP/HTML/CSS/JS" +
            "\n-: ")

            
        if choice == "0":
            print("\nCreating Basic Html/Css/JS Project...\n")
            # CODE HERE! D:\Desktop\Python\AI_test

            path = "D:/Desktop/xampp/htdocs/"+project+"/"

            try:
                os.makedirs(path)
                os.makedirs(path+"/assets/CSS")
                os.makedirs(path+"/assets/JS")
                os.makedirs(path+"/assets/IMG")

                f = open(path+"index.html", "w")

                f.write(
                    "<!DOCTYPE html>\n<html>\n<head>\n\t<title>"+project+"</title>\n\t" +
                    "<link rel='stylesheet' type='text/css' href='assets/CSS/style.css'>\n" +
                    "</head>\n<body>\n\t<h1>Project "+project+" Created Successfully!</h1>\n</body>\n</html>")
                f.close()

                f = open(path+"/assets/CSS/"+"style.css", "w")
                f.write(
                    "*{margin:0;padding:0;}\n\nhtml{font-family:sans-serif;}")
                f.close()

                sublimePath = "D:\\Sublime Text 3\\sublime_text.exe"
                xamppPath = "D:\\Desktop\\xampp\\xampp_start.exe"
                subprocess.Popen([xamppPath])
                subprocess.Popen([sublimePath, path+"index.html", path+"/assets/CSS/style.css"])

                webbrowser.open('http://localhost/'+project+'/')

                os.startfile(path)

            except OSError:
                print("\nCreation of the directory %s failed" % path)
            else:
                print("\nSuccessfully created the directory %s " % path)

        # =============================

        elif choice == "1":
            print("\nCreating Advance PHP/Html/Css/JS Project...\n")
            # CODE HERE! D:\Desktop\Python\AI_test

            path = "D:/Desktop/xampp/htdocs/"+project+"/"

            try:
                os.makedirs(path)
                os.makedirs(path+"/functions")
                os.makedirs(path+"/assets/CSS")
                os.makedirs(path+"/assets/JS")
                os.makedirs(path+"/assets/IMG")

                f = open(path+"header.php", "w")
                f.write("<?php include 'functions/conn.php'; ?>\n" +
                        "<!DOCTYPE html>\n<html>\n<head>\n\t<title>"+project+"</title>\n\t" +
                        "<link rel='stylesheet' type='text/css' href='assets/CSS/style.css'>\n" +
                        "</head>\n<body>")
                f.close()

                f = open(path+"index.php", "w")
                f.write("\n<?php include 'header.php'?>\n\t<h1>Project " +
                        project+" Created Successfully!</h1>\n<?php include 'footer.php'?>")
                f.close()

                f = open(path+"footer.php", "w")
                f.write(
                    "\n</body>\n</html>")
                f.close()

                f = open(path+"/assets/CSS/"+"style.css", "w")
                f.write(
                    "*{margin:0;padding:0;}\n\nhtml{font-family:sans-serif;}")
                f.close()

                db = input("Name of SQL database to use: ")

                f = open(path+"/functions/"+"conn.php", "w")
                f.write(
                    "<?php $host = 'localhost';\n $user = 'root'; \n$pswd = '';\n$dbName = '"+db+"';\n$conn = mysqli_connect($host, $user, $pswd, $dbName);\n" +
                    "\nif (empty($conn)){\n die('Connection failed: <br>' . mysqli_connect_error());}?>")
                f.close()

                sublimePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                xamppPath = "D:\\Desktop\\xampp\\xampp_start.exe"
                subprocess.Popen([xamppPath])
                subprocess.Popen(
                    [sublimePath, path+"index.php", path+"/assets/CSS/style.css"])
                webbrowser.open('http://localhost/phpmyadmin/')
                webbrowser.open('http://localhost/'+project+'/')

                os.startfile(path)

            except OSError:
                print("\nCreation of the directory %s failed" % path)
            else:
                print(
                    "\nSuccessfully created the project directory %s " % path)

        main()

    elif sel == '1':
        print("\nCreating Angular Project...\n")
        # CODE HERE! D:\Desktop\Python\AI_test
        projectfolder = "D:/Desktop/Angular Projects/"
        angularPath = "D:/Desktop/Angular Projects/"+project+"/"
        os.chdir(projectfolder)
        os.system("ng new "+project)
        os.chdir(angularPath)
        os.system("dir")
        vscodePath = "D:\\Program Files\\Microsoft VS Code\\Microsoft VS Code\\Code.exe"
        path = "D:\\Desktop\\Angular Projects\\myFirst"
        subprocess.Popen([vscodePath, path])
        os.system("ng serve --open")
        os.startfile(angularPath)
        # subprocess.Popen([angularPath])

        main()
    elif sel == '2':
        print("\nCreating Flutter App Project...\n")
        # CODE HERE! D:\Desktop\Python\AI_test

        projectfolder = "D:/Desktop/Flutter Projects/"
        flutterPath = "D:/Desktop/Flutter Projects/"+project+"/"
        os.chdir(projectfolder)
        os.system("flutter create "+project)
        os.chdir(flutterPath)
        os.system("dir")
        vscodePath = "D:\\Program Files\\Microsoft VS Code\\Microsoft VS Code\\Code.exe"
        path = "D:\\Desktop\\Flutter Projects\\"+project

        subprocess.Popen(
            [vscodePath,
                path+"\\",
                path+"\\lib\\main.dart"
                ])

        # os.chdir("cd "+path)
        # os.system("flutter run")
        os.startfile(flutterPath)

        main()

    elif sel == '3':
        print("Creating React JS Application....")
        os.system("npx create-react-app "+project)
        # Source path  
        source = "D:/Desktop/Python/"+project
        # Destination path  
        destination = "D:/Desktop/ReactJS/"+project
        
        # Move the content of  
        # source to destination  
        dest = shutil.move(source, destination)  
    
        print("Destination path: "+dest)  
        os.system("start cmd /K cd D:/Desktop/ReactJS/"+project)
        
        main();
    else:
        create_project()


# create_project()

# ==========================================================================================================
    # else:
    #     var = userInput.lower()
    #     os.system(var)
    #     AskUser()

# main()
# ==============================================




# ===================================================================



# Program always starts here!
try: 
    # ===========================================================

    os.system('cls')
    print("\n********* Booting Up! *********")
    system_log("\nSystem booting.....\n")

    intro = "Alpha Index, Powering up! "
    engine.say(intro)
    engine.runAndWait()

    def main():
        # ==================
        prog = True

        greetings = ["hello","hi","what's up", "hey"]
        say = ["say something", "say", "read this"]
        listening_off = ["stop listening", "switch to command", "command"]
        listening_on = ["listen", "switch to listen"]
        weather = ["what's the weather", "weather"]
        exit = ["exit", "close", "goodbye", "bye", "shutdown", "end"]
        websites = ["Google", "YouTube", "Reddit", "twitch", "Twitter", "Amazon", "eBay"]
        # showlogs = ["logs"]
    

        # res = input("Listen? 'n/y'")
        # if res == "n":
        #     listen = False
        # else:
        #     listen = True


        # *********************************************************
        listen = True #Change when your working with voice
        # *********************************************************

        while (prog == True):
            os.system('cls')

            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Computer Name is: " + hostname)
            print("Your Computer IP Address is: " + IPAddr)

            if listen == False:
                print("\nListening is 'OFF'")
                system_log("Listening is 'OFF'")
            else:
                print("\nListening is 'ON'")
                system_log("Listening is 'ON'")
            
            r = sr.Recognizer()

            arr = [] # array of words from 'word'
            def word_count(speak):
                for i in word:
                    arr.append(i)

                # Prints the new array
                # for a in arr:
                #     print(a)

                # input("") #debugging

            if listen == False:
                    command = input("Command >>: ")
                    speak = command
                    word= speak.split(" ") #spliting for websites
                    word_count(speak)

                    user_log(command)

            else:
                with sr.Microphone() as source:
                    
                    print("Speak:")
                    audio = r.listen(source)
                    speak = r.recognize_google(audio)
                    # spoken = True
                    word= speak.split(" ") #spliting for websites

                    # for i in range(len(word)):
                    #     print(word[i])
                    #     # words = ["'"+word[i]+"',"]
                    #     # words = words.append(word[i])
                    #     arr = []
                    #     arr.append(i)
                    # print(arr)

                    word_count(speak)

                    try: 
                        # print("Word count: "+str(len(arr)))

                        print("You said " + speak)
                        user_log(speak)

                        
                    except sr.UnknownValueError:
                        print("Could not understand")
                    except sr.RequestError as e:
                        print("errpr: {0}".format(e))

            if speak in greetings:
                sys = engine.say(speak+"!?, really?, is there nothing to ask?")
                engine.runAndWait()

                system_log(str(sys))

            # spoken is True and 
            # and arr[2] in websites
            elif arr[0] == "open" and arr[1] == "website" :

                if arr[2] in websites:
                     # web = speak.split(" ")
                    sys = "opening "+arr[2]+"...."
                    engine.say(sys)
                    engine.runAndWait()
                    url = 'https://www.'+arr[2]+'.com/'
                    webbrowser.open(url)
                    print('Done!')
                    system_log(sys)

                else:
                    sys = "Searching for "+ arr[2]
                    engine.say(sys)
                    engine.runAndWait()

                    search = arr[2] 

                    url = 'https://www.'+search+'.com/'
                    webbrowser.open(url)
                    print('Done!')
                    # sys = "opening "+arr[2]+"...."
                    # engine.say(sys)
                    # engine.runAndWait()
                    # url = 'https://www.'+arr[2]+'.com/'
                    # webbrowser.open(url)
                    # print('Done!')
                    system_log(sys)

            elif arr[0] == "search" and arr[1] == "website":
                # web = speak.split(" ")
                sys = "searching for "+arr[2]
                engine.say(sys)
                engine.runAndWait()
                url = 'https://www.'+arr[2]+'.com/'
                webbrowser.open(url)
                print('Done!')

                system_log(sys)

            elif arr[0] == "google" and arr[1] == "search":
                try: 
                    from googlesearch import search 
                except ImportError:  
                    print("No module named 'google' found") 
                
                # # to search 
                # con = ''
                # for i in arr:
                #     con += str(i)+" "
                #     print(con)

                sys = "searching for "+arr[2]+" "+arr[3]
                engine.say(sys)
                engine.runAndWait()

                se = arr[2]+" "+arr[3]

                for j in search(se, tld="co.in", num=10, stop=10, pause=2): 
                    url = j
                    webbrowser.open(url)
                    print(j)
                input("Press Enter....")
                system_log(sys)
            

            elif speak in say:
                sys = "what would you like me to say?"
                engine.say(sys)
                engine.runAndWait()

                ask_say = input("say: ")
                sys = engine.say(ask_say)
                engine.runAndWait()

                system_log(str(ask_say))
            
            elif(speak in listening_off):
                sys = "Listening is off...."
                engine.say(sys)
                engine.runAndWait()
                listen = False

                system_log(sys)

            # ============================================
            # elif arr[0] in showlogs or arr[1] in showlogs :
            #     sys = "opening logs.."
            #     engine.say(sys)
            #     engine.runAndWait()
                
            #     with open("D:/Desktop/Python/log.txt") as file:
            #         for line in (file.readlines() [-20:]): 
            #             print(line, end ='') 

            #     input("Press Enter.....")

            #     system_log(sys)
            
             # ===================================

            elif arr[0] == "show" and arr[1] == "logs":
                # now = datetime.datetime.now()
                if arr[3] == "today":
                    now = datetime.datetime.now()
                    # print(now)
                    DT = str(now).split(" ")
                    date = DT[0]
                    t_ime = DT[1]

                    

                    print("Date: "+str(date))
                    print("Time: "+str(t_ime))

                    input("today.......")
                else:
                    input("logs for: "+ arr[3])
 
            # ===================================

            # =======================================

            elif(speak in listening_on):
                listen = True
                print("Im Listening....")
                sys = "Speak, im listening..."
                engine.say(sys)
                engine.runAndWait()

                system_log(sys)

            # ====================================

            elif arr[0] == "create" and arr[1] == "project":
                sys = "ok"
                engine.say(sys)
                engine.runAndWait()

                create_project()

                system_log(sys)
            # ===================================

          
            

            elif speak in weather:
                def weather_data(query):
                    res = requests.get('http://api.openweathermap.org/data/2.5/weather?' +
                                        query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
                    return res.json()
                def print_weather(result, city):
                    # Printing the temperature
                    temp = "{}'s temperature: {}°C ".format(city, result['main']['temp'])
                    print(temp)
                    #printing wind speed
                    speed = "Wind speed: {} m/s".format(result['wind']['speed'])
                    print(speed)
                    #printing weather description
                    desc = "Description: {}".format(result['weather'][0]['description'])
                    print(desc)
                    cond = "Weather: {}".format(result['weather'][0]['main'])
                    print(cond)
                def mainW():
                    city = input('\nEnter the city: ')
                    
                    try:
                        query = 'q='+city
                        w_data = weather_data(query)
                        print_weather(w_data, city)
                        # print()

                        sys = "This is the weather in "+city+ " today"
                        engine.say(sys)
                        engine.runAndWait()

                        system_log(sys)

                        input("\nPress Enter....")

                    except:
                        print('City name not found...')
                        sys = "City not found.."
                        engine.say(sys)
                        engine.runAndWait()

                        system_log(sys)
               

                mainW()
            # ------------------
            elif(speak in exit):
                prog = False

            else:
                sys = "Sorry, i didn't get that, please try again."
                engine.say(sys)
                engine.runAndWait()

                system_log(sys + " Error:100")

        if prog == False:

            sys = "Good Bye User!"
            engine.say(sys)
            engine.runAndWait()

            system_log(sys)
    main()
    
except sr.UnknownValueError:
    print("Could not understand")
    sys = "Sorry, i could not understand"
    engine.say(sys)
    engine.runAndWait()
    system_log(sys + " Error:101")
    main()
    
except:
    sys = "Sorry, i dont understand that!"
    engine.say(sys)
    engine.runAndWait()
    system_log(sys + " Error:102")
    main()



