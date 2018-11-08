from pymysql import *

con = connect(host = 'localhost', user = 'root',
                       password = 'vera', db = 'ducat')

a = con.cursor()

sql1 = '''
CREATE TABLE dept(
deptno int,
foreign key (deptno) refrences employee(deptno),
deptname varchar(20));
'''

a.execute(sql1)

sql2 = '''
CREATE TABLE employee(
empid int(4) primary key,
ename varchar(20)
deptno int
);
'''

a.execute(sql2)
con.commit()
