a = []
num = int(input("Enter the size of the list"))

for i in range(num):
  num1 = int(input("Enter the number"))
  a.append(num1)

print(a)

b=[]
c=[]

for j in a:
  if(j%2==0):
    b.append(j)
  else:
    c.append(j)
  j += 1

print("Even values are", b)
print("odd values are", c)
    
