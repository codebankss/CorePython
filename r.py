f  = open('sample.txt', 'r')
print(f.read(5)) # returns only 5 characters
print(f.readline()) # reads documemnt line by readline
print(f.read()) # reads the whole document

li = f.readlines() # returns list
print(li)
