import datetime
import os
import re
import webbrowser
import smtplib
import socket
import csv
# from googlesearch import search
from pip._vendor import requests
import time
import subprocess
# import PyDictionary
# from pynput.keyboard import Key, Controller
from email.mime.text import MIMEText

# == clears console

try:

    #     def login():
    #         os.system('cls')

    #         print('Welcome My Name Is Alpha Index, Please sign in\n')

    #     with open('/users.csv', 'r') as csv_file:
    #         reader = csv.DictReader(csv_file)
    #         database = []

    #         for row in reader:
    #             database.append(dict(username=row['username'],
    #                                  password=row['password'],
    #                                  function=row['function']))

    #     loggedin = False
    #     while not loggedin:

    #         Username = input('Enter in your username: ')
    #         Password = input('Enter in your password: ')

    #         for row in database:
    #             Username_File = row['username']
    #             Password_File = row['password']
    #             Function_File = row['function']

    #             if (Username_File == Username and
    #                 Password_File == Password and
    #                     Function_File == 'Guest'):
    #                 loggedin = True

    #                 print('\nSuccesfully logged in as a Guest.\n')

    #             elif (Username_File == Username and
    #                   Password_File == Password and
    #                     Function_File == 'Admin'):
    #                 loggedin = True

    #                 print('\nSuccesfully logged in as a Admin.\n')

    #         if loggedin is not True:
    #             print('\nFailed to sign in, wrong username or password.\n')

    #             userin = str(input("Would you like guest access? (y or n) "))
    #             if (userin == 'y'):
    #                 print('\nThe username is temp, and the password is pass\n')
    #                 login()

    #             elif (userin == 'n'):
    #                 login()

    #             else:
    #                 print('invalid input')
    #             quit()

    # # ---- Main ---- #
    #     login()

    # def notmain():

    #     userName = True
    #     passWord = True

    #     while(userName == True and passWord == True):

    #         userName = str(
    #             input('Hello My Name Is Alpha Index, whats yours? '))
    #         passWord = str(input('Enter your password:'))

    #         if userName == "richard" and passWord == "admin":
    #             print(f"Hello {userName}. Nice to meet you.")

    #         else:
    #             print("I dont Know you")
    #             print("Try loging in again!")
    #             userName = False
    #             passWord = False
    #             break

    #     if __name__ == '__main__':
    #         notmain()

    def main():
        os.system('cls')
        os.system('cls')
        print('Welcome My Name Is Alpha Index\n')

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print("\nYour Computer Name is: " + hostname)
        print("Your Computer IP Address is: " + IPAddr)

        userInput = str(
            input("\nDo you want to know the time? ( y or n)  \n"))
        proceed = "y" "n"

        if userInput.lower() == ("y") in proceed:
            # clears console
            os.system('cls')
            currentDT = datetime.datetime.now()

            print("Your Computer Name is: " + hostname)
            print("Your Computer IP Address is: " + IPAddr)
            print(f"The Date and Time is:  {currentDT}")

        elif userInput.lower() == ("n") in proceed:
            # clears console
            os.system('cls')
            print("ok maybe next time then...")

        # else:
        #     print("ok maybe next time then...")
        #     main()

    # if __name__ == '__main__':
    main()


# ===========================================================================================================================

    def AskUser():
        var = ""
        # asks user for command
        userInput = str(input(
            "\nOPTIONS:\n--------------------------------" +
            # ==================START

            "\n|- IP ...\t|- go to ..." +
            "\n|- search ...\t|- what is ..." +
            "\n|- find ...\t|- weather ..." +
            "\n|- email ...\t|- create ...  " +

            # =================END
            "\n\n>>"))

        if userInput.lower() == "Exit" or userInput == "exit":
            exit()

        if userInput.lower() == "clear" or userInput == "clr":
            os.system('cls')
            AskUser()

        if userInput.lower() == "tree":
            os.system("tree/f")


# =================================================================================================================================

        if userInput.lower() == "go to":
            print("where do you want to go on your PC?    example>( C:\example )")
            mydir = input("go to..>> ")

            if mydir.lower() == "exit":
                AskUser()

            path = mydir
            path = os.path.realpath(path)
            os.startfile(path)

            # print("I cant find " + (mydir) +
            #       " on this PC as yet because my master has not tought me how to...")
            AskUser()

# ========================================================================================================================================

        elif userInput.lower() == "search":
            print(
                "what do you want to search on the Web?   note:(This scrapes the internet for results (10 max))")
            userInput = str(input("search..>> "))

            if userInput.lower() == "exit":
                AskUser()

            query = userInput

            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)
                url = j
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open((url))
            print('Done!')
            AskUser()

# ==============================================================================================================================================

        elif userInput.lower() == "what is":
            print("what is what? ...searches for words in Dictionary!")
            userInput = str(input("what is..>> "))
            # dictionary = PyDictionary()
            # print("\n" + userInput)

            # ans = dictionary.meaning(userInput)

            # # x = ans.split("[", 1)

            # # print("def: "+x[0])

            # print(ans)

            # print("\n")
            # print(dictionary.synonym(userInput))
            # print("\n")
            # print(dictionary.antonym(userInput))
            # print("\n")
            # AskUser()
            # # finds the definition of something:

            # # url = userInput
            # # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            # # webbrowser.get(chrome_path).open(
            # #     'www.dictionary.com/browse/'+(url))
            # # print('Done!')
            # # AskUser()

            if userInput.lower() == "exit":
                AskUser()


# ========================================================================================================================================

        elif userInput.lower() == "find":

            def find():
                print("Searching (D:/) for a file: ....exmaple:( test.html )")
                name = input("File Name and .ext: ")

                if name.lower() == "exit":
                    AskUser()

                try:

                    drivename = input("Which Drive to Search ( C or D )?:  ")

                    # ext = input("Enter File Type: ")
                    count = 0
                    for root, dirs, files, in os.walk(drivename+':\\'):
                        if name in files:
                            print('\n' + root + "\ ->", name)
                            count += 1

                    print('\n'+"results found:" + str(count)+"\n")
                    find()

                # find(userInput)

                except:
                    print("Error")
                    find()
            find()

# ========================================================================================================================================

        elif userInput.lower() == "weather":
            def weather_data(query):

                res = requests.get('http://api.openweathermap.org/data/2.5/weather?' +
                                   query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
                return res.json()

            def print_weather(result, city):

                print("{}'s temperature: {}°C ".format(
                    city, result['main']['temp']))
                print("Wind speed: {} m/s".format(result['wind']['speed']))
                print("Description: {}".format(
                    result['weather'][0]['description']))
                print("Weather: {}".format(result['weather'][0]['main']))

            def mainW():

                city = input('\nEnter the city: ')
                print()

                if city.lower() == "exit":
                    AskUser()

                try:
                    query = 'q='+city
                    w_data = weather_data(query)
                    print_weather(w_data, city)
                    print()
                    mainW()

                except:
                    print('City name not found...')
                    mainW()

            mainW()

    # ==============================================================================================================
        elif userInput.lower() == 'ip':
            print("YOUR IP ADDRESS:::")
            print(socket.gethostbyname(socket.gethostname()))
            AskUser()

            # host = input('Enter HOST: ')
            # print(socket.gethostname(socket.gethostname(host)))
            # import netifaces as ni
            # ni.ifaddresses('eth0')
            # ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
            # print(ip)  # should print "192.168.100.37"

        # ==========================================================================================================

        elif userInput.lower() == 'email':
            def email():
                try:

                    # ------------------------------------------------------
                    resip = input('Enter Email of Recipient: ')
                    subject = input('Enter the Subject: ')
                    content = input('Enter Message: ')

                    # init gmail SMTP
                    mail = smtplib.SMTP('smtp.gmail.com', 587)

                    # identify to server
                    mail.ehlo()

                    # encrypt session
                    mail.starttls()

                    # defining the password for test gmail account
                    sender = "persaudpro2010@gmail.com"
                    password = "swordart123"

                    x = sender.split("@", 1)

                    body = "(To: "+x[0]+")\n\n"+"' "+content+" '"

                    msg = MIMEText(body)
                    msg['Subject'] = subject
                    msg['From'] = sender
                    msg['To'] = resip
                    # login
                    mail.login(sender, password)

                    # send message
                    mail.sendmail(sender, resip, msg.as_string() +
                                  "\n\n\n-----------------------------------------------------------------------\n - SENT FROM PYTHON ->( Project: 'ALPHA INDEX')\n@RichardPersaud\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

                    # end mail connection
                    mail.close()

                    print('Email Succesfully Sent to ' + resip + "!!")
                    AskUser()
                    # else:
                    # print('I don\'t know what you mean!')
                except:
                    print("*Failed to send Email*\n")
                    tryagain = input("Try sending again? (y/n): ")

                    if tryagain.lower() == "y":
                        email()
                    else:
                        AskUser()
            email()

# =======================================================================================================================

        elif userInput.lower() == 'create':
            def create():

                print("\n0 - HTML/CSS \n1 - ANGULAR \n2 - FLUTTER \n")
                sel = input('Project Type: ')
                project = input('Enter name of Project: ')

                if project.lower() == "exit":
                    AskUser()

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

                            sublimePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                            xamppPath = "D:\\Desktop\\xampp\\xampp_start.exe"
                            subprocess.Popen([xamppPath])
                            subprocess.Popen(
                                [sublimePath, path+"index.html", path+"/assets/CSS/style.css"])

                            webbrowser.open('http://localhost/'+project+'/')

                            os.startfile(path)

                        except OSError:
                            print("\nCreation of the directory %s failed" % path)
                        else:
                            print("\nSuccessfully created the directory %s " % path)

    # ========================================================================================
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

                    AskUser()

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

                    AskUser()
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

                    AskUser()
                else:
                    create()
            create()

# ==========================================================================================================
        else:
            var = userInput.lower()
            os.system(var)
            AskUser()

    AskUser()

except:
    import sys
    os.system('cls')
    print("\n\nSomething went wrong and almost crashed the program---Check your code..\n")
    AskUser()
    # exc_type, exc_obj, exc_tb = sys.exc_info()
    # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    # print(exc_type, fname, exc_tb.tb_lineno)
    # AskUser()
