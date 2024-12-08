class Import_Data:
    #This class will be used to import the hourly csv files from the web into the data folder
    #Author: Michael Curley
    #Date: 06/12/2024


    def __init__(self):
        None

    #Method to import the csv files from the web into the data folder and return the data
    def import_data(self, station_name, station_id, skiprows):
        #Import the required libraries
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
        data_folder = 'data/hourly_data'

        # Create the data folder if it does not exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder, exist_ok=True)

        # Read the csv file
        try:
            # Download the data from the url. The response object contains the data
            # The raise_for_status() method will raise an exception if the response is not
            # a successful response
            response = requests.get(url)
            response.raise_for_status()
            # Read the data into a pandas dataframe called weather_data
            weather_data = pd.read_csv(StringIO(response.text), skiprows=self.skiprows, skipinitialspace=True)
            
            if self.skiprows == 17:
                weather_data.columns = ['Date/Time (utc)', 'Indicator', 'Precipitation Amount (mm)', 'Indicator', 'Temperature (°C)', 'Indicator', 'Wet Bulb Temperature (°C)', 'Dew Point Temp (°C)', 'Vapour Pressure (hPa)','Relative Humidity (%)', 'Mean Sea Level Pressure (hPa)','Indicator', 'Mean Wind Speed (knot)', 'Indicator', 'Predominant Wind Direction (deg)']
            else:
                weather_data.columns = ['Date/Time (utc)', 'Indicator', 'Precipitation Amount (mm)', 'Indicator', 'Temperature (°C)', 'Indicator', 'Wet Bulb Temperature (°C)', 'Dew Point Temp (°C)', 'Vapour Pressure (hPa)','Relative Humidity (%)', 'Mean Sea Level Pressure (hPa)','Indicator', 'Mean Wind Speed (knot)', 'Indicator', 'Predominant Wind Direction (deg)', 'Present Weather', 'Past Weather', 'Sunshine duration (hours)', 'Visibility', 'Cloud Height (ft * 100s)', 'Cloud amount']


        except requests.exceptions.RequestException as e:
            print('Error downloading the file:', e)

        
        # Save the data to a csv file
        self.path = os.path.join(data_folder, f'{self.station_name}_{self.station_id}.csv')
        weather_data.to_csv(self.path, index=False)


    
   