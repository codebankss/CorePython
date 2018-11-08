f = open('sample3.txt', 'a+')
n = int(input("Enter number of entries to be entered"))

for i in range(n):
    name = input('Enter name')
    f.write(name)
    f.write('\n')

f.close()

f1 = open('sample3.txt', 'r+')
li = f1.readlines()

x = input("Enter name to be searched")
x = x + '\n'

if x in li:
    print("Name found")
else:
    print("Name not found")

n = input("Ener name to be removed")
n = n+'\n'

if n in f1:
    f1.removed(n)
else:
    print("Not there")

f1.close()
