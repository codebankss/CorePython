x= [1,2,5,4,2,7,5,7,4,8,1,1,1,1,4,2,6,3,8,3]
i = 0
while i < len(x):
  j = i + 1
  while j <  len(x):
    if(x[i] == x[j]):
      del(x[j])
    else:
      j = j+1
  i = i+1  
    
print(x)


