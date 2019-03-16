import datetime
import os
import webbrowser

#clears console
os.system('cls')
userName = str(input('Hello My Name Is Alpha Index, whats yours?'))

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

elif userInput == "search":
    print("what do you want to search on the Web?   example( www.google.com )")
    userInput = str(input("search..>> "))

    url = userInput
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)



elif userInput == "What is":
    print("what is what?")
    userInput = str(input("what is..>> "))

elif userInput == "open":
    print("open what on desktop?")
    userInput = str(input("open..>> "))

else: print("Huh?")
