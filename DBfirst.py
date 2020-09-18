import mysql.connector

mydb=mysql.connector.connect(host="localhost",username="kowshik",password="1234",database='python')


acc=mydb.cursor()

acc.execute("select * from python.human")

for i in acc:
	print(i)
	
	
#output:

#('kowshik', 28, 'st.johns', '')
#('', 27, 'mount', '')
#('Default', 28, 'st.johns', 'chennai')
#('varma', 29, 'rmk', 'bangalore')
#('kowshik', 27, 'st.johns', 'chennai')

