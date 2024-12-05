#Run a number of queries on the shannon_airport database
# How to print out a number of different queries on the shannon_airport database
# To do this, we need to open a connection to the database, create a cursor and execute the queries.
# We can then fetch the results and print them out.
# To do it a second time, we need to create a new cursor, as the first cursor will have been used up.

import sqlite3
import pandas as pd

# Open the connection
conn = sqlite3.connect('shannon_airport.db')

# Create a cursor
c = conn.cursor()
d = conn.cursor()
e = conn.cursor()

# Execute a query to return the wind speed and date for the year 2019'
c.execute('SELECT date, wdsp FROM shannon_airport WHERE date LIKE "%2019%"')

#Find the minimum and maximum and average wind speed for the year 2019
d.execute('SELECT MIN(wdsp), MAX(wdsp), AVG(wdsp) FROM shannon_airport WHERE date LIKE "%2019%"')

#count the number of occurances of the query
e.execute('SELECT COUNT(*) FROM shannon_airport WHERE wdsp >3 and wdsp < 10')

# Fetch the results
rows = c.fetchall()

# Print the first 10 rows
for row in rows:
    print(row)


# Fetch the results
rows = d.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()