#updating values

import pymysql
import pymysql.cursors

conn = pymysql.connect(host = 'localhost', user = 'root',
                       password = 'vera', db = 'sample')

a = conn.cursor()

en = input("Enter employees name: ")
en = " ' " +en+ " ' "
print(en)

sql = '''
UPDATE Employee SET ename = '" +en +"'WHERE eid = 1090
'''

a.execute(sql)
conn.commit()
