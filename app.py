import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "appdbproj",
  autocommit=True
)

cursor = db.cursor()

#cursor.execute("select * from city where id = 245")
cursor.execute("UPDATE citycopy SET population = population + 100 where id =123")
results= cursor.fetchall() 
print(results)


db.close()
cursor.close()