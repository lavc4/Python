import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="saurav123"
)

print(mydb)