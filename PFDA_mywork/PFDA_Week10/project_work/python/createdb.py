class CreateDB:
    import pandas as pd

    def __init__(self):
        import mysql.connector
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )   

        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS weather")

        self.connection.close()
        self.cursor.close()
