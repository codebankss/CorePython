import sqlite3 as lite
import sys

cars = (
  (1, 'car1', 100),
  (2, 'car2', 200),
  (3, 'car3', 300)
  )

con = lite.connect("test.db")

with con:
  cur = con.cursor()
  cur.execute('''DROP TABLE IF EXISTS Cars''' )
  cur.execute('''CREATE TABLE Cars(Id INT, Name TEXT, Price INT)''')
  cur.executemany('''INSERT INTO Cars VALUES(?,?,?)''', cars)



  
