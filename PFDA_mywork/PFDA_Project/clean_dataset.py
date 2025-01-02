class CleanDataset:

    #Import the libraries you need
    import pandas as pd

    #Set the instance variables
    filename = ""
    skiprows = 0

    #Set an empty dataset variable to store the imported dataset
    dataset = pd.DataFrame()


    #Constructor. This is the code that is run when a new instance of the class is created.
    def __init__(self, id, skiprows):
        import pandas as pd
        file_path = 'data/hourly_data/hly'
        self.skiprows = skiprows
        self.id = id
        location = ('{}' + '{}'+'.csv').format(file_path, self.id)
        #print(location)
        try:
            self.dataset = pd.read_csv(location, 
                                   skiprows=skiprows, 
                                   skipinitialspace=True,
                                   na_values = ['-', 'N/A', 'NA', 'nan', 'NaN', 'NAN', 'Nan', 'N/a', 'n/a', 'na', ''] 
                                    )
        except FileNotFoundError: 
            print('File not found. Please check the file path and name')


        #Create a function to import the dataset
        if self.skiprows == 23:
            try:
                self.dataset.columns = ['Date/Time (utc)', 'Indicator', 'Precipitation Amount (mm)', 'Indicator', 'Temperature (°C)', 'Indicator', 'Wet Bulb Temperature (°C)', 'Dew Point Temp (°C)', 'Vapour Pressure (hPa)','Relative Humidity (%)', 'Mean Sea Level Pressure (hPa)','Indicator', 'Mean Wind Speed (knot)', 'Indicator', 'Predominant Wind Direction (deg)', 'Present Weather', 'Past Weather', 'Sunshine duration (hours)', 'Visibility', 'Cloud Height (ft * 100s)', 'Cloud amount']
                #print('Dataset imported')
            except KeyError:
                print('Columns not found. Please check the column names')
        else:
            try:
                self.dataset.columns = ['Date/Time (utc)', 'Indicator', 'Precipitation Amount (mm)', 'Indicator', 'Temperature (°C)', 'Indicator', 'Wet Bulb Temperature (°C)', 'Dew Point Temp (°C)', 'Vapour Pressure (hPa)','Relative Humidity (%)', 'Mean Sea Level Pressure (hPa)','Indicator', 'Mean Wind Speed (knot)', 'Indicator', 'Predominant Wind Direction (deg)']
                #print('Dataset imported')
            except KeyError:
                print('Columns not found. Please check the column names')
        
    
        
    #Create a function to remove the NA values from the dataset
    def remove_na_values(self):
        import pandas as pd
        #print('Removing NA values')
        #Remove the indicator columns
        self.dataset.drop(columns=['Indicator'], inplace=True)
        #print('Indicator columns removed')
        #Remove the rows with NA values
        self.dataset.dropna(inplace=True, ignore_index=True)


    #Create a function to clean the datetime column and add a month and year column
    def clean_datetime(self):
        import pandas as pd
        import datetime as dt
        self.dataset['Date/Time (utc)'] = pd.to_datetime(self.dataset['Date/Time (utc)'], format='%d-%b-%Y %H:%M')
        self.dataset['Month'] = self.dataset['Date/Time (utc)'].dt.month
        self.dataset['Year'] = self.dataset['Date/Time (utc)'].dt.year
        #print('Datetime cleaned')

    #Create a function to rename the wind column and reduce the dataset to only the columns we need
    def rename_windcolumn(self):
        import re
        station_name = self.filename.split('_')
        #print(station_name)
        name = str(station_name[0]) + '_Wind_Speed'
        name = self.dataset[['Date/Time (utc)', 'Precipitation Amount (mm)','Temperature (°C)','Mean Wind Speed (knot)','Predominant Wind Direction (deg)', 'Month', 'Year']].copy()
        name.rename(columns={'Mean Wind Speed (knot)': 'Mean Wind Speed (knot)_' + str(station_name[0])}, inplace=True)
        self.dataset = name
        #print('Wind column renamed')
        #print(self.dataset.head())

    def clean_dataset(self):
        self.remove_na_values()
        self.clean_datetime()
        self.rename_windcolumn()
        
        return self.dataset