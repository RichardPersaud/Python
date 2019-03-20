import tkinter as tk 
from tkinter import *


#top header menu 
root = Tk()
root.geometry("1080x720")
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')
filemenu.add_command(label='Exit', command=root.quit)

ourMessage ='This is our Message'
messageVar = Message(root, text = ourMessage) 
messageVar.config(bg='lightgreen') 
messageVar.pack( )







root.mainloop() 

