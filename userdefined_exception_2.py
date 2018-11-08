from userdefined_exception import myExcept

i = int(input("Enter a number"))

try:
  if(i<30):
    raise myExcept("Number can not be less than 30")
except myExcept as me:
  print(me)
