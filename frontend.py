import tkinter as Tk
from tkinter import *
import backend
from backend import * # We are importing our backend.py file as a module and all the functions are imported
''' Below are the functions which provide the Functionality to our buttons created in the tkinter GUI where each button is having one of these  
functions as a command and get executed upon clicking it'''
def get_selected_row(event): # This is a function which will triger the even defined for the listbox when we are selecting any tuple displayed in the listbox
    global selected_tuple # declaring selected_tuple as a global variable
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
   










def view_command():
    list1.delete(0,END)
    for row in backend.view(): # since our function return a list of tuples we have to iterate over it and pass it through our function
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),Author_text.get(),year_text.get(),isbb_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),Author_text.get(),year_text.get(),isbb_text.get())
    ''' We are passing the whole data entered by user as tuple since 
    my sqlite database is accepting tuple as an input'''
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),Author_text.get(),year_text.get(),isbb_text.get()))

def delete_backend():
    backend.delete(selected_tuple[0])




master_1 = Tk() # master window for executing and displaying the functionality of our applications
# Setting up the initial functionaliity of our module further 
l1 = Label(master_1,text = 'Title')
l1.grid(row=0,column=0)



l2 = Label(master_1,text = 'Author')
l2.grid(row=0,column=2)


l3 = Label(master_1,text = 'Year')
l3.grid(row=1,column=0)

l4 = Label(master_1,text = 'ISBN')
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(master_1,textvariable=title_text)
e1.grid(row = 0 , column = 1)

Author_text = StringVar()
e2 = Entry(master_1,textvariable=Author_text)
e2.grid(row = 0 , column = 3)


year_text = StringVar()
e3 = Entry(master_1,textvariable=year_text)
e3.grid(row = 1, column = 1)

isbb_text = StringVar()
e4 = Entry(master_1,textvariable=isbb_text)
e4.grid(row = 1, column = 3)


list1 = Listbox(master_1,height = 6 ,width = 35)
list1.grid(row = 2, column = 0,rowspan = 6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

scroll_bar1 = Scrollbar(master_1)
scroll_bar1.grid(row = 2,column = 2)

list1.configure(yscrollcommand = scroll_bar1.set)
scroll_bar1.configure(command = list1.yview)

button1 = Button(master_1,text = "view all",command = view_command)
button1.grid(row=2,column = 3)

button2 = Button(master_1,text = "search entry",command = search_command)
button2.grid(row=3,column = 3)

button3 = Button(master_1,text = "Add entry" , command = add_command)
button3.grid(row=4,column = 3)


button4 = Button(master_1,text = "Update")
button4.grid(row=5,column = 3)

button5 = Button(master_1,text = "Delete",command = delete_backend)
button5.grid(row=6,column = 3)

button6 = Button(master_1,text = "Close")
button6.grid(row=7,column = 3)


 






mainloop() # This is our mainloop function which gets executed