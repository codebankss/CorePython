class Base:
  def __init__(self):
    print('Base constructor')

  def show(self):
    print('base method')

class Child(Base):
  def __init__(self):
    print("Child constructor")

  def show2(self):
    print("Child method")

#ob1 = Base()
ob2 = Child()
#ob2.show2()


