from pymysql import *
from tkinter import *;
from tkinter import messagebox as tm

from Abc import *   # This is the next form to switch using call method 

class Employee(Frame):
  def __init__(self, master):
    super().__init__(master)

    self.l1 = Label(self, text = "Employee Number")
    self.l2 = Label(self, text ="Employee Name")
    self.l3 = Label(self, text ="Salary")
    self.l4 = Label(self, text ="Department Number")

    self.t1 = Entry(self)
    self.t2 = Entry(self)
    self.t3 = Entry(self)
    self.t4 = Entry(self)

    self.b1 = Button(self, text = "Add", command = self.add)
    self.b2 = Button(self, text = "Delete")
    self.b3 = Button(self, text = "Search", command = self.find)
    self.b4 = Button(self, text = "Update")
    self.b5 = Button(self, text = "Show")
    self.b6 = Button(self, text = "Exit", command = self.exitprg)
    self.b7 = Button(self, text = "Next", command = self.call)

    self.l1.grid(row = 0, column = 0)
    self.l1.grid(row = 0, column = 1)

    self.l2.grid(row = 1, column = 0)
    self.l2.grid(row = 1, column = 1)

    self.l3.grid(row = 2, column = 0)
    self.l3.grid(row = 2, column = 1)

    self.l4.grid(row = 3, column = 0)
    self.l4.grid(row = 3, column = 1)


    self.b1.grid(row = 4, column = 0)
    self.b2.grid(row = 4, column = 1)
    self.b3.grid(row = 5, column = 0)
    self.b4.grid(row = 5, column = 1)
    self.b5.grid(row = 6, column = 0)
    self.b6.grid(row = 6, column = 1)
    self.b7.grid(row = 7, column = 1)

    self.pack()

  def add(self):
    eno = int(self.t1.get())
    ename = self.t2.get()
    sal = int(self.t3.get())
    dno = int(self.t4.get())

    con = connect(db = 'test', user = 'root', passwd = 'vera', host = 'localhost')
    cur = con.cursor()

    cur.execute("insert into emp values(%d, '%s', %d, %d )%"(eno, ename, sal, dno))
    con.commit()
    self.t1.delete(0, 'end')
    self.t2.delete(0, 'end')
    self.t3.delete(0, 'end')
    self.t4.delete(0, 'end')
    con.close()

  def exitprg(self):
    exit(0)

  def find(self):
    eno = int(self.t1.get())
    con = connect(db = 'test', user = 'root', passwd = 'vera', host = 'localhost')
    cur = con.cursor()

    cur.execute("select e.name, d.name, e.salary from emp e.dept d where e.empno = %d and e.deptno = d.deptno"%(empno))
    record = cur.fetchone()
    tm.showinfo("Search Record", record)
    con.close()

  def call(self):
    rot = Tk()
    obj = Abc(rot)
    rot.title("Second page")
    rot.geometry("250x200")
    rot.mainloop()

root = Tk()
ob = Employee(root)
root.title("Employee Dets")
root.geometry('600x400')
root.mainloop()


    


  

    

    

    
    
