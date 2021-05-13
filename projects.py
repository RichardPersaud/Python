import os
import subprocess
# Create Web Project
# Create directory
dirName = 'tempDir'
parent_dir = "D:/Desktop/xampp/htdocs/"
try:
    # Create target Directory
    path = os.path.join(parent_dir, dirName)
    os.mkdir(path)

    print("Directory ", dirName,  " Created ")
except FileExistsError:
    print("Directory ", dirName,  " already exists")


# os.startfile('C:\Program Files\Sublime Text 3\sublime_text.exe')
subprocess.Popen('C:\Program Files\Sublime Text 3\sublime_text.exe', '.'], cwd=path, shell=True)
