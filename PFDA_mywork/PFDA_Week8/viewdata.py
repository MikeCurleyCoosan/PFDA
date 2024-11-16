import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()

sql = "SELECT * FROM student WHERE id = %s"
values = (1,)

cursor.execute(sql, values)

result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()

db.close()
