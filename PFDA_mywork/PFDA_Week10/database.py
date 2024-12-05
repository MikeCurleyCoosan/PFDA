#Looking at creating a database of a csv file for the project

import pandas as pd
import sqlite3

# Read the csv file
df = pd.read_csv('./data/hly518_shannon_airport_hourly.csv', skipinitialspace=True, skiprows=23)

# Create a connection to a new database, if it exists, it will be overwritten

conn = sqlite3.connect('shannon_airport.db')

# Write the data to a sqlite table
df.to_sql('shannon_airport', conn)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

# Open the connection
conn = sqlite3.connect('shannon_airport.db')

# Create a cursor
c = conn.cursor()

# Execute a query
c.execute('SELECT * FROM shannon_airport')

# Fetch the results
rows = c.fetchall()

# Print the first 10 rows
for row in rows[:10]:
    print(row)


# Close the connection
conn.close()

