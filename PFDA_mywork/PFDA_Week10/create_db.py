












    def insert_table(self, df):
        import mysql.connector
        import pandas as pd
        df = pd.DataFrame(df)
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='weather'
        )

        df.to_sql('weather', self.connection)
        self.connection.commit()

        self.connection.close()
        self.cursor.close()

    
create = create_db()
import pandas as pd
df = pd.read_csv('./data/hly518_shannon_airport_hourly.csv', skipinitialspace=True, skiprows=23)
create.insert_table(df)

