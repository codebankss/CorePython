from pymysql import *
ans=''
while ans!='y':
	print('1. Add Record')
	print('2. Search Record')
	print('3. Delete Record')
	print('4. Update Record')
	print('5. Show All')
	print('6. Exit')
	print('Enter Your  Choice 1 to 6')
	choice=(int)(input())
	if choice==1:
		con=connect(db='ducat',user='root',passwd='vera',host='localhost')
		cur=con.cursor()
		print('Enter Student id')
		sid=(int)(input())
		print('Enter Student Name')
		sname=input()
		print('Enter Student Class')
		sclass=input()
		print('Enter Student Father\'s name')
		fname=input()
		cur.execute("insert into student values(%d,'%s','%s','%s')"%(sid,sname,sclass,fname))
		con.commit()
		print('Record Saved')
		con.close()
	if choice==2:
		con=connect(db='ducat',user='root',passwd='vera',host='localhost')
		cur=con.cursor()
		print('Enter Student id')
		sid=(int)(input())
		cur.execute("select * from student where sid=%d"%(sid))
		record=cur.fetchone()
		if record:
			print()
			print('Student Id ',sid)
			print('Student Name',record[1])
			print('Student Class',record[2])
			print('Father\'s Name',record[3])
			print('\nPress Enter to continue...\n')
			input()
		else:
			print('Record Not Found')
		con.close()
	if choice==3:
		con=connect(db='ducat',user='root',passwd='vera',host='localhost')
		cur=con.cursor()
		print('Enter Student id')
		sid=(int)(input())
		cur.execute("delete from student where sid=%d"%(sid))
		con.commit()
		print('Record Deleted')
		print('\nPress Enter to continue...\n')
		input()
	if choice==4:
		con=connect(db='ducat',user='root',passwd='vera',host='localhost')
		cur=con.cursor()
		print('Enter Student id Which you want to change')
		sid=(int)(input())
		print('Enter New Name')
		sname=input()
		print('Enter New Class')
		sclass=input()
		cur.execute("update student set sname='%s',sclass='%s' where sid=%d"%(sname,sclass,sid))
		con.commit()
		print('Record Updated')
		print('\nPress Enter to continue...\n')
		input()
		
	if choice==5:
		con=connect(db='ducat',user='root',passwd='vera',host='localhost')
		cur=con.cursor()
		cur.execute("select * from student")		
		record=cur.fetchall()
		for i in range(len(record)):
                                                    i = 2
                                                    r = cur.fetchmany(i)
                                                    i = i+2
                                                    print(r)
		x=0
		l=len(record)
		while l>0:
			print('---------------------------------------------------------')
			print('Student Id        : ',record[x][0])
			print('Student Name      : ',record[x][1])
			print('Student Class     : ',record[x][2])
			print('Father\'s Name     : ',record[x][3])
			x+=1
			l-=1
			print('---------------------------------------------------------')
		con.close()
		print('\nPress Enter to continue...\n')
		input()
	if choice==6:
		exit(0)
