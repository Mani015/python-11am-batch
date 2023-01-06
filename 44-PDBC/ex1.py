import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root')

if db:
    print('connceted successfully')
else:
    print('connceted unsuccessfully')