class CreateDB:
    #This class will be used to create the database that will store the weather data
    #Author: Michael Curley
    #Date: 06/12/2024

    #Import the required libraries
    import pandas as pd

    def __init__(self):
        #The constructor method will be used to create the database
        import mysql.connector
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )   

        #Create a cursor object to allow us to interact with the database
        self.cursor = self.connection.cursor()
        #Create the database if it does not exist
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS weather")

        self.connection.close()
        self.cursor.close()
