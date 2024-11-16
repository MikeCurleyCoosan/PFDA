import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()

sql = "INSERT INTO student (name, age) VALUES (%s, %s)"

values = ("John", 21)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

cursor.close()
db.close()
