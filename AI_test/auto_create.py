import datetime
import os
import re
import webbrowser
import smtplib
import socket
import csv
from pip._vendor import requests
import time
import subprocess
import shutil  



# == clears console

try:
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

    def database():
        import mysql.connector

        mydb = mysql.connector.connect(
        host="localhost",
        user="myusername",
        password="mypassword"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SHOW DATABASES")

        for x in mycursor:
            print(x)


# ===========================================================================================================================

    def AskUser():
        var = ""
        # asks user for command
        userInput = str(input(
            "\nOPTIONS:\n--------------------------------" +
            # ==================START

            "\n|- create ...  " +

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
# =======================================================================================================================

        elif userInput.lower() == 'create':
            def create():

                print("\n0 - HTML/CSS \n1 - ANGULAR \n2 - FLUTTER \n3 - REACT_JS \n")
                sel = input('Project Type: ')
            
                if sel.lower() == "exit":
                    AskUser()

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

                            sublimePath = "D:\\Sublime Text 3\\sublime_text.exe"
                            xamppPath = "D:\\Desktop\\xampp\\xampp-control.exe"
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
                                    "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n" +
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

                            # database()

                            db = input("Name of SQL database to use: ")

                            f = open(path+"/functions/"+"conn.php", "w")
                            f.write(
                                "<?php $host = 'localhost';\n $user = 'root'; \n$pswd = '';\n$dbName = '"+db+"';\n$conn = mysqli_connect($host, $user, $pswd, $dbName);\n" +
                                "\nif (empty($conn)){\n die('Connection failed: <br>' . mysqli_connect_error());}?>")
                            f.close()

                            sublimePath = "D:\\Sublime Text 3\\sublime_text.exe"
                            xamppPath = "D:\\Desktop\\xampp\\xampp-control.exe"
                            subprocess.Popen([xamppPath])
                            subprocess.Popen(
                                [sublimePath, path+"index.php", path+"/assets/CSS/style.css"])
                            webbrowser.open('http://localhost:8012/phpmyadmin/db_structure.php?server=1&db='+db)
                            webbrowser.open('http://localhost:8012/'+project+'/')

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
