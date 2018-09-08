# Creating tables

import pymysql
import pymysql.cursors

conn = pymysql.connect(host = 'localhost', user = 'root',
                       password = 'vera', db = 'sample')

a = conn.cursor()

sql = '''
CREATE TABLE Employee(
eid int(4) NOT NULL,
ENAME VARCHAR(20));
'''

a.execute(sql)
conn.commit()
