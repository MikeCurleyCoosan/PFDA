class Join:
    #Method used to join the dataframes in the data folder into a single dataframe.
    #The columns to keep are passed in as an argument
    #The station data is passed in as an argument. This is a dictionary with the station id as the key
    #The value is a dictionary with the metadata and the data
    #The metadata includes the station name and the skiprows. The data is a pandas dataframe
    #The data is saved to a csv file called joined_data.csv. This file is saved in the data folder
    

    #Author: Michael Curley
    #Date: 7/12/2024

    def __init__(self):
        None

    def join_data(self, columns_to_keep, stations_data):
        #Import the required libraries
        import pandas as pd
        import os

        #Our instance variables
        self.columns_to_keep = columns_to_keep
        self.stations_data = stations_data


        #Define the data folder
        data_folder = 'data/daily_data'

        #Define the output file path
        output_file = 'data/joined_data.csv'

        #Create an empty list to store the overall dataframe
        all_data = []

        #Loop through the station names and read in the data
        for file in os.listdir(data_folder):
            if not file.endswith('.csv'):
                continue
            else:
                file_path = os.path.join(data_folder, file)
                #print(file_path)
                #Split the last four digits before the file extension to get the station id
                id = file.split('/dly')[-1].split('.')[0]
                id = int(id[3:])
                #print(id)

            try:
                station_name = self.stations_data[id]['metadata']['station_name']
                skiprows = self.stations_data[id]['metadata']['skiprows']
                #print(station_name)
                #print(skiprows)

                weather_data = pd.read_csv(file_path, skiprows=skiprows, skipinitialspace=True)
                len = weather_data.columns.size
            
                if len == 24:
                    weather_data.columns = [ 'Date/Time (utc)', 'Indicator', 'Maximum Air Temperature (C)', 'Indicator2', 'Minimum Air Temperature (C)', 'igmin', 'Minimum  Air Temperature (C)', 'Indicator3', 'Precipitation Amount (mm)', 'Mean CBL Pressure (hpa)', 'Mean Wind Speed (knot)', 'Indicator4', 'Highest ten minute mean wind speed (knot)', 'Indicator5', 'Wind Direction at max 10 min. mean (deg)', 'Indicator6', 'Highest Gust (knot)', 'Mean 10cm Soil Temperature (C)', 'Potential Evapotranspiration (mm)', 'Evaporation (mm)', 'InSoil Moisture Deficits(mm) well drained', 'Soil Moisture Deficits(mm) moderately drained', 'Soil Moisture Deficits(mm) poorly drained', 'Global Radiation (J/cm sq.)']
                elif len == 25:
                    weather_data.columns = [ 'Date/Time (utc)', 'Indicator', 'Maximum Air Temperature (C)', 'Indicator2', 'Minimum Air Temperature (C)', 'igmin', 'Minimum  Air Temperature (C)', 'Indicator3', 'Precipitation Amount (mm)', 'Mean CBL Pressure (hpa)', 'Mean Wind Speed (knot)', 'Indicator4', 'Highest ten minute mean wind speed (knot)', 'Indicator5', 'Wind Direction at max 10 min. mean (deg)', 'Indicator6', 'Highest Gust (knot)', 'Sunshine duration (hours)', 'dos', 'Mean 10cm Soil Temperature (C)', 'Potential Evapotranspiration (mm)', 'Evaporation (mm)', 'InSoil Moisture Deficits(mm) well drained', 'Soil Moisture Deficits(mm) moderately drained', 'Soil Moisture Deficits(mm) poorly drained']
                else:
                    weather_data.columns = [ 'Date/Time (utc)', 'Indicator', 'Maximum Air Temperature (C)', 'Indicator2', 'Minimum Air Temperature (C)', 'igmin', 'Minimum  Air Temperature (C)', 'Indicator3', 'Precipitation Amount (mm)', 'Mean CBL Pressure (hpa)', 'Mean Wind Speed (knot)', 'Indicator4', 'Highest ten minute mean wind speed (knot)', 'Indicator5', 'Wind Direction at max 10 min. mean (deg)', 'Indicator6', 'Highest Gust (knot)', 'Sunshine duration (hours)', 'dos','Global Radiation (J/cm sq.)', 'Mean 10cm Soil Temperature (C)', 'Potential Evapotranspiration (mm)', 'Evaporation (mm)', 'InSoil Moisture Deficits(mm) well drained', 'Soil Moisture Deficits(mm) moderately drained', 'Soil Moisture Deficits(mm) poorly drained']                                 


                data = weather_data[columns_to_keep].copy()
                data['Station Name'] = station_name
                #Append the data to the all_data list
                all_data.append(data)

            except Exception as e:
                print('Error reading in the data:', e)

        #Concatenate the dataframes in the all_data list
        try:
            all_data = pd.concat(all_data, ignore_index=True).to_csv(output_file, index=False)
            print(f'Joined data saved to {output_file}')
        except Exception as e:
            print('Error concatenating the dataframes:', e)
                



