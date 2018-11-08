class Base:
  def __init__(self):
    self.student = []
    self.name = []
    self.marks = []

  def get(self):
    self.name.append(input("Enter name"))
    for x in range(3):
      m = int(input("Enter marks"))
      self.marks.append(m)
    self.student.append([self.name, self.marks])
    print(self.student)

ob = Base()
ob.get()
