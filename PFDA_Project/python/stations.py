class Stations:
#Class to hold the metadata and weather data for the stations
#The metadata includes the county, station name, latitude, longitude, altitude and skiprows
#The weather data is stored in a pandas DataFrame
#The stations are identified by their station number
#
    def __init__(self):
        None
    
    def get_station(self, id, county):
        import pandas as pd
        self.id = id
        self.county = county
        #Create a dictionary to hold the metadata and weather data for the stations
        #The keys are the station numbers
        #The values are a dictionary with keys metadata and data
        #The metadata is a dictionary with keys county, station_name, latitude, longitude, altitude and skiprows
        #Author: Michael Curley

        station = {
            id: {
                "metadata": {
                    "station_name": None, 
                    "latitude": None, 
                    "longitude": None, 
                    "altitude": None, 
                    "skiprows": None,
                    "skiprows_hourly": None
                },
            }
        }
        return station
    