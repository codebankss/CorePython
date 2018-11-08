ans = 'y'
while (ans=='y'):
    print("1.ADD, 2.SHOW, 3.SEARCH, 4.UPDATE, 5.DELETE, 6.EXIT")
    ch = int(input("Enter choice"))
    if ch == 1:
        f = open('employee.txt', 'a+')
        name = input("Enter name")+'\n'
        f.write(name)
        f.close()
    elif ch == 2:
        f = open('employee.txt')
        print(f.read())
        f.close()
    elif ch == 3:
        f = open('employee.txt')
        n = input("Enter name to be searched")+'\n'
        li = f.readlines()
        if n in li:
            print("Name found")
        else:
            print("Name not found")
        f.close()
    elif ch == 4:
        f = open("employee.txt")
        li = f.readlines()
        f.close()
        i = input("Enter name to be replaced")+'\n'
        j = input("Enter replaced name")+'\n'
        if i in li:
            x = li.index[i]
            li[x] = j
            f = open('employee.txt', 'w')
            for x in li:
                f.write(x)
            f.close()
            print("Updated")
    elif ch == 5:
        f = open('employee.txt')
        li = f.readlines()
        x = input("Enter record to be deleted")+'\n'
        li.remove(x)
        f = open('employee.txt', 'w')
        for x in li:
            f.write(x)
        f.close()
        print("deleted")
    elif ch == 6:
        exit(0)
    ans = input('y/n')
