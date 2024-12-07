class CreateTable:

    import pandas as pd
    host = "localhost"
    user = "root"
    password = ""
    database = "weather"

    def __init__(self):
        None

    def create_table(self, table_name, skiprows):
        import mysql.connector
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='weather'
        )   

        self.table_name = table_name
        self.skiprows = skiprows

        if skiprows == 17:
            self.cursor = self.connection.cursor()
            sql = f"CREATE TABLE IF NOT EXISTS {table_name} (date DATE, ind INTEGER, rain FLOAT, ind2 INTEGER, temp FLOAT, ind3 INTEGER, wetb FLOAT, dewpt FLOAT, vappr FLOAT, rhum INTEGER, msl INTEGER, ind4 INTEGER, wdsp FLOAT, ind5 INTEGER, wddir INTEGER)"

            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
            self.cursor.close()
        else:
            self.cursor = self.connection.cursor()
            sql = f"CREATE TABLE IF NOT EXISTS {table_name} (date DATE, ind INTEGER, rain FLOAT, ind2 INTEGER, temp FLOAT, ind3 INTEGER, wetb FLOAT, dewpt FLOAT, vappr FLOAT, rhum INTEGER, msl INTEGER, ind4 INTEGER, wdsp FLOAT, ind5 INTEGER, wddir INTEGER, ww FLOAT, w INTEGER, sun FLOAT, vis INTEGER, clht INTEGER, clamt INTEGER)"
            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
            self.cursor.close()

