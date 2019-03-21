import tkinter

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
 
window = Tk()
window.geometry("1080x720")
window.title("Welcome to LikeGeeks app")


menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item) 
window.config(menu=menu)


tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(window, text="Hello page 1", font=("Arial Bold", 50))
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Hello page 2", font=("Arial Bold", 50))
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')


  
#essagebox.showinfo('Message title', 'Message content')
 
#btn = Button(window,text='Click here', command=clicked)
 
#btn.grid(column=0,row=0)



window.mainloop()