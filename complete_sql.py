from pymysql import *

ans = ''
while(ans != 'y'):
  print("1. Add, 2.Search, 3. Delete, 4. Update, 5. Show, 6. Exit ")
  print("Enter your choice")
  choice = int(input())
  if choice == 1:
    con = connect(db = 'ducat', user = 'root', passwd = 'vera', host = 'localhost')
    cur = con.cursor()
    print("Enter student id")
    sid = int(input())
    print("Enter student name")
    sname = input()
    print("Enter student class")
    sclass = input()
    print("Enter students father name")
    fname = input()
    cur.execute('''insert into student values(%d,%s,%s,%s)'''%(sid, sname, sclass, fname))
    con.commit()
    print("Record Saved")
    con.close()

  if choice ==2 :
    con = connect(db = 'ducat', user = 'root', passwd = 'vera', host = 'localhost')
    cur = con.cursor()
    print("Enter student id")
    sid = int(input())
    cur.execute('''select * from student where sid = %d'''%(sid))
    record = cur.fetchone()
    if record :
      print()
      print("Student id", sid)
      print("Student name", record[1])
      print("Student class", record[2])
      print("Students fathers name", record[3])
      print("\n Press Enter to continue \n")
      input()
    else:
      print("Record not found")
    con.close()

  if choice == 3:
    con = connect(db = 'ducat', user = 'root', passwd = 'vera', host = 'localhost')
    cur = con.cursor()
    print("Enter student id")
    sid = int(input())
    cur.execute('''delete from student where sid = %d'''%(sid))
    con.commit()
    print("Record deleted")
    con.close()

  if choice == 4:
    con = connect(db = 'ducat', user = 'root', passwd = 'vera', host = 'localhost')
    cur = con.cursor()
    print("Enter student id")
    sid = int(input())
    print("Enter new name")
    sname = input()
    print("Enter new class")
    sclass = input()
    cur.execute('''update student set sname = %s, sclass =%s where sid = %d'''%(sname, sclass, sid))
    con.commit()
    print("record updated")
    con.close()

  if choice == 5:
    con = connect(db = 'ducat', user = 'root', passwd = 'vera', host = 'localhost')
    cur = con.cursor()
    cur.execute('''select * from student''')
    record = cur.fetchall()
    x = 0
    l = len(record)
    while l>0:
      print("_"*80)
      print("Student id : ", record[x][0])
      print("Student name :", record[x][1])
      print("Student class : ", record[x][2])
      print("Student fathers name :", record[x][3])
      x+=1
      l-=1
      print("_"*80)
    con.close()
    print("Enter to continue")
    input()

  if choice == 6:
    exit(0)
    
