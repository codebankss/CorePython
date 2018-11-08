from tkinter import *
from tkinter import messagebox as tm

class Demo(Frame):            # calling base class frame
  def __init__(self, other):      #defining constructor
    super().__init__(other)   #calling 'other' from base class

    self.l1 = Label(self, text = "User name")
    self.l2 = Label(self, text = "Password")
    self.t1 = Entry(self)
    self.t2 = Entry(self, show = '*')
    self.b1 = Button(self, text = 'Login', command = self.show)

    self.l1.grid(row = 0, column = 0)
    self.t1.grid(row = 0, column =1)

    self.l2.grid(row = 2, column = 0)
    self.t2.grid(row = 2, column = 1)

    self.b1.grid(columnspan = 2)
    self.pack()

  def show(self):     
    uid = self.t1.get()  #getting username
    pwd = self.t2.get()  #getting password

    tm.showinfo('Information', 'Thanks' +uid+ 'your password is' +pwd )  #displaying information after clicking
    self.t1.delete(0, 'end') #event handling(deleting textbox values after showing)
    self.t2.delete(0, 'end')
    
    


root = Tk()                           #creating object of tkinter
ob = Demo(root)                   #creating object of  our class
root.title("Employee")        #giving title
root.geometry('200X200')    #defining size
root.mainloop()                     # displaying form
