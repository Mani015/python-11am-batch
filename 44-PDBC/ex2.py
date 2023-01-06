import mysql.connector

x=mysql.connector.connect(host='localhost',user='root',password='root')

mydb=x.cursor()

mydb.execute('show databases')
for db in mydb:
    print(db)

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
# ('super',)
# ('sys',)