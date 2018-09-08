# inserting values

import pymysql
import pymysql.cursors

conn = pymysql.connect(host = 'localhost', user = 'root',
                       password = 'vera', db = 'sample')

a = conn.cursor()

sql = '''
INSERT INTO Employee(eid, ENAME) VALUES(1101, 'Mr ABC')
'''

a.execute(sql)
conn.commit()
