import mysql.connector

mydb=mysql.connector.connect(host="localhost",username="kowshik",password="1234",database='python')


acc=mydb.cursor()

acc.execute("select * from python.human")

for i in acc:
	print(i)