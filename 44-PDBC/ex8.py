import mysql.connector

x1=mysql.connector.connect(host='localhost',user='root',password='root',database='student')

mydb=x1.cursor()


mydb=x1.cursor()
sql='delete from tenth  where rollno=103'
mydb.execute(sql)
x1.commit()

