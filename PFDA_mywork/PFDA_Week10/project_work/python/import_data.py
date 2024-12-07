class Import_Data:


    def __init__(self):
        None

    #Method to import the csv files from the web into the data folder and return the data
    def import_data(self, station_name, station_id, skiprows):
        import pandas as pd
        import requests
        from io import StringIO
        import os
       
    
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

        
        # Save the data to a csv file
        self.path = os.path.join(data_folder, f'{self.station_name}_{self.station_id}.csv')
        weather_data.to_csv(self.path, index=False)


    
   