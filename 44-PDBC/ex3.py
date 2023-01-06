import mysql.connector

x=mysql.connector.connect(host='localhost',user='root',password='root')

mydb=x.cursor()

# mydb.execute('create database student')

# print(mydb)
mydb.execute('show databases')


for k in mydb:
    print(k)

# ('batch',)
# ('cat',)
# ('cbv',)
# ('dell',)
# ('employee',)
# ('grk',)
# ('gun',)
# ('information_schema',)
# ('lap',)
# ('man',)
# ('mysql',)
# ('performance_schema',)
# ('saw',)
# ('student',)
# ('super',)
# ('sys',)