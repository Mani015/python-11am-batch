import mysql.connector

x1=mysql.connector.connect(host='localhost',user='root',password='root',database='student')

mydb=x1.cursor()

mydb1='update tenth set name="xyz" where  address="pune"'
mydb.execute(mydb1)
x1.commit()