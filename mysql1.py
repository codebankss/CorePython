# creating a database

import pymysql
#import pymysql.cursors

conn = pymysql.connect(host = 'localhost', user = 'root',
                       password = 'vera')

a = conn.cursor()

query = 'CREATE DATABASE sample'

a.execute(query)
conn.commit()
