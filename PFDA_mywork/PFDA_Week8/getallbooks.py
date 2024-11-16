import sqlite3

con=sqlite3.connect('pfda.db')

cur=con.cursor()

for row in cur.execute('SElect * FROM books'):
    print(f"row {row}")