class WriteDB:
    #This class will write the data from the csv files into a database.
    #Author: Michael Curley
    #Date: 06/12/2024


    def __init__(self):
        None

    #Method to import the csv files from the web into the data folder and return the data
    def write_db(self, station_name, station_id, skiprows):
        #Import the required libraries 
        import pandas as pd
        import requests
        from io import StringIO
        import os
        import mysql.connector
        import sqlalchemy as sa
        from sqlalchemy import create_engine
        import pymysql as pymysql
       
    
        # Define the station name, station ID and skiprows variables for this instance of the class
        self.station_name = station_name
        self.station_id = station_id
        self.skiprows = skiprows

        # Define the url and the data folder variables
        base_url = 'https://cli.fusio.net/cli/climate_data/webdata/hly{}.csv'
        url = base_url.format(self.station_id)
        data_folder = 'data'

        # Create the data folder if it does not exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder, exist_ok=True)

        # Read the csv file
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = pd.read_csv(StringIO(response.text), skiprows=self.skiprows, skipinitialspace=True)
        except requests.exceptions.RequestException as e:
            print('Error downloading the file:', e)
            
  
        # The database URL must be in a specific format. This format is as follows:
        db_url = "mysql+pymysql://{USER}:{PWD}@{HOST}/{DBNAME}"

        # Replace the values below with your own
        # DB username, password, host and database name
        # These should be read in by a config file. Look at this time permitting
        db_url = db_url.format(
            USER = "root",    
            PWD = "",
            HOST = "localhost",
            DBNAME = "weather"
        )
        # Create the DB engine instance. We'll use
        # this engine to connect to the database
        engine = create_engine(db_url, echo=False)
        #Test that the engine has being created
        print("Engine created")
        # Import the create_engine method from the sqlalchemy module
        with engine.begin() as conn:
        # Invoke DataFrame method to_sql() to
        # create the table based on where the weather data is coming from and
        # insert all the DataFrame rows into it
            weather_data.to_sql(
                name=self.station_name, # database table
                con=conn,
                if_exists='replace', # database connection
                index=False # Don't save index
            )
        # Close the connection
        conn.close()
        # Close the engine
        engine.dispose()
