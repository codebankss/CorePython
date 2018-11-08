di = {'a':1, 'b':2, 'c':3}
li1=[]
li2=[]

'''i=0
j=0

for i,j in di.items():
  li1.append(i)
  li2.append(j)
  i +=1
  j += 1  '''

for x in di:
  li1.append(x)
  li2.append(di[x])

print(li1)
print(li2)

