class TestDB:


    def __init__(self):
        None

    #Method to import the csv files from the web into the data folder and return the data
    def test_db(self, station_name):
        import mysql.connector
       
    
        # Define the station name, station ID and skiprows variables for this instance of the class
        self.station_name = station_name


        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="weather"
        )

        cursor = db.cursor()

        sql = "SELECT * FROM cork_airport LIMIT 20;"
        values = (self.station_name)

        cursor.execute(sql, values)

        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()

        db.close()