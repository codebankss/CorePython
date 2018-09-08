import sqlite3 as lite
import sys

con = lite.connect("test.db")

with con:

  cur = con.cursor() # cursor is a temp memory
  cur.execute("SELECT SQLITE_VERSION()")

  data = cur.fetchone()

  print("SQLite version is %s" % data)


  
