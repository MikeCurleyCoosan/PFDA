import sqlite3

con = sqlite3.connect('pfda.db')

cur = con.cursor()

#See the contents of the books table
result = cur.execute("SELECT * FROM books")
print("Books Table contents")
print(result.fetchall())
print("End of Books Table contents")

#Insert a book into the books table

#This is not a good way to insert data into the table. It may lead to SQL injection attacks.
#SQL injection is a code injection technique, used to attack data-driven applications,
#in which malicious SQL statements are inserted into an entry field for execution 
# (e.g. to dump the database contents to the attacker).
sql = "INSERT INTO books (title, author, ISBN, year) VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925), ('To Kill a Mockingbird', 'Harper Lee', '9780061120084', 1960), ('1984', 'George Orwell', '9780451524935', 1949)"

cur.execute(sql)

#See the contents of the books table
result = cur.execute("SELECT * FROM books")
print("Books Table contents")
print(result.fetchall())
print("End of Books Table contents")

con.commit()

con.close()

