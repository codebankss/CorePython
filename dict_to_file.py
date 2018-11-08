f = open('sample.txt', 'w')
di = {}
li = []

for x in range(3):
    marks = int(input('Enter marks'))
    li.append(marks)

name = input("Enter name")
di[name] = li
f.write(str(di)) # file only contains string
f.close()
