import mysql.connector

db=mysql.connector.connect(host="localhost",username="kowshik",password="1234",database="python")

comm=db.cursor()


#distinct is used to select any specific column
comm.execute("select distinct name,place from human")

for i in comm:
	print(i)

#count is used to count the numbers of items in column
comm.execute("select count(distinct name,place) from human")
t=[]
for j in comm:
	print(j)
	t.append(j)
	print(t)

#where condition
comm.execute("select * from human where Name = 'varma'")

for l in comm:
	print(l)





