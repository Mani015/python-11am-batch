import mysql.connector

x1=mysql.connector.connect(host='localhost', user='root',password='root',database='student')

mydb=x1.cursor()

data="Insert into tenth(name,rollno,address) values (%s, %s,%s)"
emp=[('bharath',101,'hyd'),('sravani',102,'bng'),('kishore',103,'chennai'),('praveen',104,'pune')]

mydb.executemany(data,emp)

x1.commit()