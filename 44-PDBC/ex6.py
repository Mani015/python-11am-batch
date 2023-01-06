import mysql.connector

x1=mysql.connector.connect(host='localhost',user='root',password='root',database='student')

mydb=x1.cursor()
mydb.execute('select name from tenth bharath where rollno=101')
y=mydb.fetchall()
for i in y:
    print(i)

# ('bharath',)
# ('sravani',)
# ('kishore',)
# ('praveen',)




