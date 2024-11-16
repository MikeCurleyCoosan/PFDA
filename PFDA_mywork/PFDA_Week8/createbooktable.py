import sqlite3

con = sqlite3.connect('pfda.db')

cur = con.cursor()

sql = "DROP TABLE IF EXISTS books"
cur.execute(sql)

# Create a table called books
cur.execute("CREATE TABLE books (title, author, ISBN, year)")

result = cur.execute("SELECT * FROM books")
print("Books Table contents")
print(result.fetchone())
print("End of Books Table contents")

