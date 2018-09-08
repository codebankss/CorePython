#inserting through list

import pymysql
import pymysql.cursors

conn = pymysql.connect(host = 'localhost', user = 'root',
                       password = 'vera', db = 'sample')

a = conn.cursor()

lst = [(1090, 'pqr'),
       (1091, 'xyz'),
       (1093, 'abc')
  ]

a.executemany(
  '''INSERT INTO Employee VALUES(%s, %s)''', lst)

conn.commit()
