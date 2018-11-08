class Base:
  def __init__(self):
    print("Taking names and age")

  def dets(self):
    global name, age
    name = input("Enter name")
    age = int(input("Enter age"))
    return name, age

class Child(Base):
  def __init__(self):
    print("Comparing ages")

    def compare(self):
      if (age<18):
        print(name, "is not eligible")
      else:
        print(name, 'is eligible')



#q = input("Input name")
#w = int(input("Input age"))

ob = Child()
ob.dets()
ob.compare()

