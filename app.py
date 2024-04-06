import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "appdbproj"
)

cursor = db.cursor()

cursor.execute("select * from city")
results= cursor.fetchall() 
print(results)


db.close()
cursor.close()