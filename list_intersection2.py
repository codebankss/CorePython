def inter(list1, list2):
  print(list(set(list1) and set(list2)))
  return

x = [1,2,2,2,3,4,4]
y = [2,2,3,3,4]
inter(x, y)
