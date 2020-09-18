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
	
#And condition
comm.execute("select name,place from human  where name='varma' and place='bangalore'")

for n in comm:
	print(n)
	
#OR Condition
comm.execute("select Name,age from human where Name = 'kowshik' or age = 27")

for o in comm:
	print(o)


#AND Condition
comm.execute("select Name,age from human where Name = 'kowshik' and age = 27")

for a in comm:
	print(a)
	
#Not Condition
comm.execute("select name from human where not name ='kowshik'")

for n in comm:
	print(n)
print("end not")
#order by descending order for name ascending is by default present no need to explicit mention it
comm.execute("select name from human order by name desc")

for od in comm:
	print(od)
print("end order by")

comm.execute("use python")
#insert
t=comm.execute("insert into python.human(Name,age,school,place) values('thomson',37,'kidzee','florida')")

#null
comm.execute("select name,age,school from human where name is not null")

for nu in comm:
	print(nu)
	
#update
comm.execute("update human set age=33, school='chinmaya' where name='thomson'")
comm.execute("update human set place ='mumbai',school='kendriya' where age=28 and name='kowshik'")

print("end of update")
#delete
comm.execute("delete from human where name=''")

for de in comm:
	print(de)
	
comm.execute("select * from human")

for hu in comm:
	print(hu)
print("end of table delete")
#limit
comm.execute("select * from human where place='chennai' limit  1;")

for li in comm:
	print(li)

#max and min
comm.execute("select max(age) from human")


for ag in comm:
	print(ag)

