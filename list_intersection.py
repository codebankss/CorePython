x= [1,2,3,4,4,4,7,6,4,7,8,9,4,2,3,4,6,1,3,8,0,9,1,2,3,4]
y = [4,5,42,1,1,2,2,3,4,4,5,5,6,7,7,8,9,0]

def inter(list1, list2):
  lis3 = [i for i in list1 if i in list2]
  lis4 = []
  for j in lis3:
    if j not in lis4:
      lis4.append(j)
  print(lis4)
  return
    

inter(x, y)
