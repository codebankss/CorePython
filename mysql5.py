#printing output

import pymysql
import pymysql.cursors

conn = pymysql.connect(host = 'localhost', user = 'root',
                       password = 'vera', db = 'sample')

a = conn.cursor()

query = '''
SELECT * FROM Employee;
'''
a.execute(query)
lst = a.fetchall()
#print(lst)

for x in lst:
  print(x)
