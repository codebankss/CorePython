import sqlite3 as lite
import sys

con = lite.connect("test.db")

with con:

  cur = con.cursor()

  cur.execute('''SELECT * FROM Cars''')
  rows = cur.fetchall()
'''  print(rows)

  for row in rows:
    print(row)


#li = list(rows)

#print(li)'''

print(rows)

for i in rows:
  print("S No"+str(i[0])+ "model"+i[1]+"price"+str(i[2]))


  
