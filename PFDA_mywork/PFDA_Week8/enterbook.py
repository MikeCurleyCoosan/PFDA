import sqlite3

con = sqlite3.connect('pfda.db')

cur = con.cursor()

book = {}

book['title'] = input("Enter the title of the book: ")
book['author'] = input("Enter the author of the book: ")
book['ISBN'] = input("Enter the ISBN of the book: ")
book['year'] = int(input("Enter the year of the book: "))

data = [book]

sql = "INSERT INTO books VALUES (:title, :author, :ISBN, :year)"

cur.executemany(sql, data)

con.commit()

for row in cur.execute('SELECT * FROM books'):
    print(f'row {row}')

con.close()
