class Base:
  def __init__(self):
    self.student = []
    self.name = []
    self.marks = []

  def get(self):
    for z in range(2):
      self.name = []
      self.marks = []
      self.name.append(input("Enter name"))
      for x in range(3):
        m = int(input("Enter marks"))
        self.marks.append(m)
      self.student.append([self.name, self.marks])
    #print(self.student)

  def show(self):
    for x in range(2):
      j = 1
      i = 0
      print("Student name", self.student[x][i])
      print("Total marks", sum(self.student[x][j]))
      i += 1

ob = Base()
ob.get()
ob.show()
