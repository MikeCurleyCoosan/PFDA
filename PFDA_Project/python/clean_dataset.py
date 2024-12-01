class CleanDataset:

    #Import the libraries you need
    import pandas as pd

    #Set the instance variables
    filename = ""
    skiprows = 0

    #Set an empty dataset variable to store the imported dataset
    dataset = pd.DataFrame()


    #Constructor. This is the code that is run when a new instance of the class is created.
    def __init__(self, filename, skiprows):
        import pandas as pd
        file_path = './data/'
        self.filename = filename
        self.skiprows = skiprows
        url = file_path + filename
        self.dataset = pd.read_csv(url, 
                                   skiprows=skiprows, 
                                   skipinitialspace=True,   
                                    )
        self.dataset.columns = ['Date/Time (utc)', 'Indicator', 'Precipitation Amount (mm)', 'Indicator', 'Temperature (°C)', 'Indicator', 'Wet Bulb Temperature (°C)', 'Dew Point Temp (°C)', 'Vapour Pressure (hPa)','Relative Humidity (%)', 'Mean Sea Level Pressure (hPa)','Indicator', 'Mean Wind Speed (knot)', 'Indicator', 'Predominant Wind Direction (deg)', 'Present Weather', 'Past Weather', 'Sunshine duration (hours)', 'Visibility', 'Cloud Height (ft * 100s)', 'Cloud amount']
        print('Dataset imported')
        
    #Create a function to remove the NA values from the dataset
    def remove_na_values(self):
        import pandas as pd
        print('Removing NA values')
        self.dataset.drop(columns=['Indicator'])
        self.dataset.dropna(inplace=True)
        print('NA values removed')

    #Create a function to clean the datetime column and add a month and year column
    def clean_datetime(self):
        import pandas as pd
        import datetime as dt
        self.dataset['Date/Time (utc)'] = pd.to_datetime(self.dataset['Date/Time (utc)'], format='%d-%b-%Y %H:%M')
        self.dataset['Month'] = self.dataset['Date/Time (utc)'].dt.month
        self.dataset['Year'] = self.dataset['Date/Time (utc)'].dt.year
        print('Datetime cleaned')

    #Create a function to rename the wind column and reduce the dataset to only the columns we need
    def rename_windcolumn(self):
        import re
        station_name = re.findall(r'_(.*?)_', self.filename)
        name = str(station_name[0]) + '_Wind_Speed'
        name = self.dataset[['Date/Time (utc)', 'Mean Wind Speed (knot)', 'Month', 'Year']].copy()
        name.rename(columns={'Mean Wind Speed (knot)': 'Mean Wind Speed (knot)_' + str(station_name[0])}, inplace=True)
        self.dataset = name
        print('Wind column renamed')
        print(self.dataset.head())

    def clean_dataset(self):
        self.remove_na_values()
        self.clean_datetime()
        self.rename_windcolumn()
        return 