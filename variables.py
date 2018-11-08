class Base:
  def __init__(self):
    self.X = 10 # public
    self.__X = 20 # private[encapsulation(data hiding)]
    self._X = 30 # protected

ob = Base()
print(ob.X)
print(ob._X)
print(ob.__X) # error because private variable is not availble

