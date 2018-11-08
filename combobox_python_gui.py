from tkinter import *

class Abc(Frame):
  def __init__(self, master):
    super().__init__(master)

    self.tkvar = StringVar(self)
    choices = {'Python', 'DS', 'ML', 'Django', 'Java', 'DL'} #set because no duplicates
    self.tkvar.set('----select----') #defining default option
    self.popupMenu = OptionMenu(self, self.tkvar, *choices, command = self.sel)
    self.lblx = Label(self, text = 'Choose a alanguage')
    self.lblx.grid(row = 1, column = 1)
    self.popupMenu.grid(row = 2, column = 1)
    self.pack()

  def sel(self, event):
    val = str(self.tkvar.get())
    print(val)


root = Tk()
root.title("Combo Box Example")
root.geometry("200x200")
obj = Abc(root)
