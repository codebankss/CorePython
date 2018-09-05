def add():
  x,y=no()
  print(x+y)
  return


def mul():
  x,y=no()
  print(x*y)
  return

def sub():
  x,y = no()
  print(x-y)
  return

def choice():
  print("1 for add, 2 for mul and 3 for sub")

def no():
  a = int(input("Enter first number"))
  b = int(input("Enter second number"))
  return(a,b)


counter = 0

dic = {1 : add, 2 : mul, 3 : sub}

while(counter != 4):
  choice() 
  counter = int(input("Enter a choice of calculation"))
  if(counter>0 and counter < 4):
    dic[counter]()
