import datetime
import os
import webbrowser
import smtplib
import requests
import requests
from pprint import pprint


#clears console
os.system('cls')
userName = str(input('Hello My Name Is Alpha Index, whats yours? '))

if userName == "richard":
    print(f"Hello {userName}. Nice to meet you.")
else: 
    print("I dont Know you")
    exit()

userInput = str(input("Do you want to know the time? ( y or n)   "))
proceed = "y" "n"

if userInput == ("y") in proceed:
    #clears console
    os.system('cls')
    currentDT = datetime.datetime.now()
    print (f"The Date and Time is:  {currentDT}")
    

elif userInput == ("n") in proceed:
    #clears console
    os.system('cls')
    print("ok maybe next time then...")

else: print("What? i dont understand....")

#asks user for command
userInput = str(input("What would you like to do? ('go to ...'/'search ...'/'what is...'/'open ...')  >>"))

if userInput == "go to":
    print("where do you want to go on your PC?    example>( C:\example )")
    mydir = str(input("go to..>> "))

    print("I cant find "+ (mydir)+ " on this PC as yet because my master has not tought me how to...")

elif userInput == "search":
    print("what do you want to search on the Web?   example( www.google.com )")
    userInput = str(input("search..>> "))

    #   searches the internet for the path your entering:

    url = userInput
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    print('Done!')


elif userInput == "what is":
    print("what is what?")
    userInput = str(input("what is..>> "))

    # finds the definition of something:

    url = userInput
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('www.dictionary.com/browse/'+(url))
    print('Done!')

elif userInput == "open":
    print("open what on desktop?")
    userInput = str(input("open..>> "))

    print("I cant find "+ (userInput)+ " on this PC as yet because my master has not tought me how to...")


# Asks for the city to find the current weather temp there 

elif userInput == "weather":
    def weather_data(query):

        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        return res.json();

    def print_weather(result,city):

        print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
        print("Wind speed: {} m/s".format(result['wind']['speed']))
        print("Description: {}".format(result['weather'][0]['description']))
        print("Weather: {}".format(result['weather'][0]['main']))

    def main():

        city=input('Enter the city:')
        print()

        try:
            query='q='+city;
            w_data=weather_data(query);
            print_weather(w_data, city)
            print()

        except:
            print('City name not found...')

    if __name__=='__main__':
        main()

else: print("Huh?")
