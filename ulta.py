n = input("Enter a name")

a = n.split()
length = len(a)
nname = ''
for x in range(0, length-1):
  nname = nname+' '+a[x][0]

nname = a[length-1]+' '+nname
print(nname)
