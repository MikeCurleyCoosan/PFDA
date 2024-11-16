import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()

sql = "UPDATE student SET name = %s, age = %s WHERE id = %s"
values = ("Joe", 33, 1)

cursor.execute(sql, values)

db.commit()
print(cursor.rowcount, "record(s) affected")

cursor.close()

db.close()
