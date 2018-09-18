import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Wh1stl3r",
    database="mydb"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydb")

#mycursor.execute("SHOW DATABASES")

#for db in mycursor:
#    print(db)


mycursor.execute("CREATE TABLE students (name varchar(255) not null, age integer(10) not null)")

mycursor.execute("SHOW TABLES")

for mytable in mycursor:
 print(mytable)
