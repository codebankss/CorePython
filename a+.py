f = open('sample.txt', 'a+')
a = 'y'

while(a == 'y'):
    inp = input()
    f.write(inp+'\n')
    a = input("y or n")

f.close()
