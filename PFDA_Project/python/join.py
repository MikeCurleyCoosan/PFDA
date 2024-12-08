class Join:
    #Method used to join the dataframes in the data folder into a single dataframe
    #Author: Michael Curley
    #Date: 7/12/2024

    def __init__(self):
        None

    def join_data(self, columns_to_keep):
        #Import the required libraries
        import pandas as pd
        import os

        #Our instance variables
        self.columns_to_keep = columns_to_keep

        #Define the data folder
        data_folder = 'data2'

        #Define the output file path
        output_file = 'data2/joined_data.csv'

        #Create an empty list to store the overall dataframe
        all_data = []

        #Loop through the station names and read in the data
        for file in os.listdir(data_folder):
            file_path = os.path.join(data_folder, file)
            print(file_path)

            try:
                station_name = file.split('_')[0]
                print(station_name)

                data = pd.read_csv(file_path)[columns_to_keep]
                data['station_name'] = station_name
                #Append the data to the all_data list
                all_data.append(data)

            except Exception as e:
                print('Error reading in the data:', e)

        #Concatenate the dataframes in the all_data list
        try:
            all_data = pd.concat(all_data, ignore_index=True).to_csv(output_file, index=False)
        except Exception as e:
            print('Error concatenating the dataframes:', e)
                



