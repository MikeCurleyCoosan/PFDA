class CreateTable:
    #This class will be used to create the tables in the database that will store the weather data
    #Suthor: Michael Curley
    #Date: 06/12/2024


    def __init__(self):
        None

    #Method to create the tables in the database. This method will take in the table name and the number of rows to skip
    #The number of rows to skip will determine how many columns the table will have
    def create_table(self, table_name, skiprows):
        import mysql.connector

        #Set up the connection to the database. This data should really be read in from a config file
        #This is something that could be done time permitting
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='weather'
        )   
        #Create our instance variables
        self.table_name = table_name
        self.skiprows = skiprows

        #We know that the metadata for the tables is in two different formats, we need to create the tables accordingly
        #We will use an if statement to determine which format the metadata is in
        if skiprows == 17:
            #Create a cursor object to allow us to interact with the database
            self.cursor = self.connection.cursor()
            #Create the sql query to create the table
            sql = f"CREATE TABLE IF NOT EXISTS {table_name} (date DATE, ind INTEGER, rain FLOAT, ind2 INTEGER, temp FLOAT, ind3 INTEGER, wetb FLOAT, dewpt FLOAT, vappr FLOAT, rhum INTEGER, msl INTEGER, ind4 INTEGER, wdsp FLOAT, ind5 INTEGER, wddir INTEGER)"
            #Execute the query
            self.cursor.execute(sql)
            #Commit the changes
            self.connection.commit()
            #Close the connection and the cursor
            self.connection.close()
            self.cursor.close()
        else:
            #Create a cursor object to allow us to interact with the database
            self.cursor = self.connection.cursor()
            #Create the sql query to create the table
            sql = f"CREATE TABLE IF NOT EXISTS {table_name} (date DATE, ind INTEGER, rain FLOAT, ind2 INTEGER, temp FLOAT, ind3 INTEGER, wetb FLOAT, dewpt FLOAT, vappr FLOAT, rhum INTEGER, msl INTEGER, ind4 INTEGER, wdsp FLOAT, ind5 INTEGER, wddir INTEGER, ww FLOAT, w INTEGER, sun FLOAT, vis INTEGER, clht INTEGER, clamt INTEGER)"
            #Execute the query
            self.cursor.execute(sql)
            #Commit the changes
            self.connection.commit()
            #Close the connection and the cursor
            self.connection.close()
            self.cursor.close()

