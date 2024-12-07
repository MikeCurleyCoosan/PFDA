class TestDB:
    #This class will be used to test that we can retrieve data from the database after we have populated it with the weather data
    #The class will have a method that will connect to the database and retrieve the first 20 rows of data from the database
    #Author: Michael Curley
    #Date: 06/12/2024


    def __init__(self):
        None

    #Method to import the csv files from the web into the data folder and return the data
    def test_db(self, station_name):
        import mysql.connector
       
    
        # Define the station name, station ID and skiprows variables for this instance of the class
        self.station_name = station_name

        #Set up the connection to the database. This data should really be read in from a config file
        #This is something that could be done time permitting
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="weather"
        )
        #Create a cursor object to allow us to interact with the database
        cursor = db.cursor()
        #Define the SQL query that we want to execute
        sql = "SELECT * FROM cork_airport LIMIT 20;"
        values = (self.station_name)
        #Execute the query
        cursor.execute(sql, values)
        #Get the results of the query
        result = cursor.fetchall()
        #Print the results of the query
        for row in result:
            print(row)
        #Close the cursor and the database connection
        cursor.close()
        db.close()