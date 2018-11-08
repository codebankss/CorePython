# overriding __str__

class Abc:
  def __init__(se, name):
    se.name = name
    print("Hello")

  def __str__(se):
    print(se.name)

ob = Abc('what')
print(ob)
    
