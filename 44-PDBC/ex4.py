import mysql.connector

x1=mysql.connector.connect(host='localhost', user='root',password='root',database='student')

mydb=x1.cursor()
mydb.execute('show tables')

for i in mydb:
    print(i)
# mydb=x1.cursor()
# mydb.execute("create table tenth(name varchar(20),rollno int(30),address varchar(30))")

# ('tenth',)
