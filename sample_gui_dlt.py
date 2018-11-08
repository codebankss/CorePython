'''from tkinter import *
from tkinter import messagebox

top = Tk()
L1 = Label(top, text = 'name1')
L1.pack()
L2 = Label(top, text = 'name2')
L2.pack()
L3 = Label(top, text = 'name3')
L3.pack()


E1 = Button(top, text = 'Display together')
E1.pack()

def output():
  msg = messagebox.showinfo('name 1'+L1+'name2'+L2+'name3'+L3)

top.mainloop()
'''
from tkinter import *

from tkinter import messagebox

def login():
    if(E1<6):
        msg = messagebox.showinfo("LogIn", "success")
    else:
        msg = messagebox.showinfo("LogIn", "failed")

top = Tk()
L1 = Label(top, text = "User name")
L1.pack(side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

E1 = Button(top, text = "LogIn", command = login)
E1.place(x = 50, y = 50)

top.mainloop()
