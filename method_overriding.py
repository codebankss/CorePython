class Base:
  def __init__(self): # base class constructor, called when formed object with child class
    print("This is Base class")

    def add(self, x, y):
      k = x+y
      print("Output", k)

    def display(self):
      print("display of base class")

class Child(Base):
  def add(self, x, y):
    k = x+y
    print('Total', k)

  def show(self):
    print("show of child class")


#ob1 = Base()
ob2 = Child()
ob2.add(2,2)
#ob1.add(2,2) this will give error when executed
