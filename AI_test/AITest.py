import datetime
import os
import re
import webbrowser
import smtplib 
# smtp is for mail sending
import requests

import csv
#clears console



def login():
    os.system('cls')

    print('Welcome My Name Is Alpha Index, Please sign in\n')

    with open('users.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        database = []
        for row in reader:
            database.append(dict(username=row['username'],
                                 password=row['password'],
                                 function=row['function']))

    loggedin = False

    while not loggedin:

        Username = input('Enter in your username: ')
        Password = input('Enter in your password: ')

        for row in database:
            Username_File = row['username']
            Password_File = row['password']
            Function_File = row['function']

            if (Username_File == Username and
                Password_File == Password and
                    Function_File == 'Guest'):
                loggedin = True

                print('\nSuccesfully logged in as a Guest.\n')

            elif (Username_File == Username and
                  Password_File == Password and
                    Function_File == 'Admin'):
                loggedin = True

                print('\nSuccesfully logged in as a Admin.\n')

        if loggedin is not True:
            print ('\nFailed to sign in, wrong username or password.\n')

            userin = str(input("Would you like guest access? (y or n) ")) 
            if (userin == 'y'):
                print('\nThe username is temp, and the password is pass\n')
                login()

            elif (userin == 'n'):
                login()

            else: print('invalid input')
            quit()

# ---- Main ---- #
login()


# def main():

#     userName = True
#     passWord = True

#     while(userName == True and passWord == True):   

#         userName = str(input('Hello My Name Is Alpha Index, whats yours? '))
#         passWord = str(input('Enter your password:'))

#         if userName == "richard" and passWord == "admin":
#             print(f"Hello {userName}. Nice to meet you.")
            
#         else: 
#             print("I dont Know you")
#             print("Try loging in again!")
#             userName = False
#             passWord = False
#             break

# if __name__=='__main__':
#     main()




def main():
    userInput = str(input("Do you want to know the time? ( y or n)  \n "))
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

if __name__=='__main__':
        main()



def AskUser():
    #asks user for command
    userInput = str(input("\nWhat would you like to do? \n1. go to ...\n2. search ...\n3. what is ...\n4. open ...\n5. weather ...\n  \n>>"))

    if userInput == "go to":
        print("where do you want to go on your PC?    example>( C:\example )")
        mydir = str(input("go to..>> "))

        print("I cant find "+ (mydir)+ " on this PC as yet because my master has not tought me how to...")
        AskUser()

    elif userInput == "search":
        print("what do you want to search on the Web?   example( www.google.com )")
        userInput = str(input("search..>> "))

        #   searches the internet for the path your entering

        url = userInput
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('https://'+(url))
        print('Done!')
        AskUser()


    elif userInput == "what is":
        print("what is what?")
        userInput = str(input("what is..>> "))

        # finds the definition of something:

        url = userInput
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('www.dictionary.com/browse/'+(url))
        print('Done!')
        AskUser()

    elif userInput == "open":
        print("open what on desktop?")
        userInput = str(input("open..>> "))

        print("I cant find "+ (userInput)+ " on this PC as yet because my master has not tought me how to...")
        AskUser()


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

            city=input('\nEnter the city:')
            print()

            try:
                query='q='+city;
                w_data=weather_data(query);
                print_weather(w_data, city)
                print()

            except:
                print('City name not found...')
                main()

        if __name__=='__main__':
            main()

    else: print("\nHuh?\n")
    AskUser()

AskUser()
