class Metadata:
#This class is used to extract the metadata (station name, latitude, longitude, altitude) from the header of a CSV file.
#The class has a single method, extract_metadata, which takes the file path of the CSV file and returns the extracted metadata.
#The method uses regular expressions to search for specific patterns in the header of the CSV file.
#Author: Michael Curley

    def __init__(self):
        None
    
    def extract_metadata(self, file_path):
        #Import the regular expression module to search for the metadata
        import re
        #Set the instance variable
        self.file_path = file_path
        
        try:
            # Open the file and read its contents. Use utf-8 encoding to handle special characters
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        
            # Initialize variables to store extracted values
            station_name, latitude, longitude, altitude = None, None, None, None

            # Define regex patterns for extracting metadata
            station_name_pattern = r"Station Name\s*[:=]?\s*([A-Za-z\s\(\)\-]+)"
            latitude_pattern = r"Latitude\s*[:=]?\s*([\d\.-]+)"
            longitude_pattern = r"Longitude\s*[:=]?\s*([\d\.-]+)"
            altitude_pattern = r"Station Height\s*[:=]?\s*([\d\.-]+)"
        
            # Loop through each line to search for these patterns
            for line in lines:
                station_name_match = re.search(station_name_pattern, line, re.IGNORECASE)
                if station_name_match:
                    station_name = str(station_name_match.group(1).strip())

                latitude_match = re.search(latitude_pattern, line, re.IGNORECASE)
                if latitude_match:
                    latitude = float(latitude_match.group(1))
            
                longitude_match = re.search(longitude_pattern, line, re.IGNORECASE)
                if longitude_match:
                    longitude = float(longitude_match.group(1))
            
                altitude_match = re.search(altitude_pattern, line, re.IGNORECASE)
                if altitude_match:
                    altitude = float(altitude_match.group(1))

            return station_name, latitude, longitude, altitude
    
        except Exception as e:
            print(f"Error extracting metadata from header: {e}")
            return None, None, None, None