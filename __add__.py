#adding two numbers by overriding function and hence adding by object

class Over:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "{0},{1}".format(self.x, self.y) # index 0 for x, 1 for y

  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return(x, y)

ob = Over(1,2)
print(ob)
ob1 = Over(4,5)
print(ob1)
print(ob + ob1)
