import sqlite3 as lite
import sys

con = lite.connect("test.db")

with con:

  cur = con.cursor()
  
  cur.execute('''CREATE TABLE Cars(Id INT, Name TEXT, Price INT)''')
  cur.execute('''INSERT INTO Cars VALUES(1, 'car1', 10)''')
  cur.execute('''INSERT INTO Cars VALUES(2, 'car2', 20)''')
  cur.execute('''INSERT INTO Cars VALUES(3, 'car3', 30)''')



  
