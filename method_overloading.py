class Base:
  def add(self, x):
    print("Total", x)

  def add(self, x, y):
    k = x + y
    print("Output", k)


ob = Base()
#ob.add(27) ''' This will give an error when executed beacuse method overloading is not supported'''
ob.add(27,27)
