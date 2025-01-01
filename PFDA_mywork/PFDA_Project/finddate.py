class Finddate:
#This class is used to find the row that contains the 'date column' in the csv files we are working with
#The class has a single method, find_row, which takes the file path of the csv file and returns the row index that contains the 'date' column.
#If the 'date' column is not found, the method returns 0 to indicate that no rows should be skipped.
#Author: Michael Curley

    def _init__(self):
        None

    def find_row(self, file_path):
        #Import the regular expression module to search for the 'date' column
        import re
        #Set the instance variable
        self.file_path = file_path

        try:
            # Open the file and read its contents. Use utf-8 encoding to handle special characters
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        
        # Search for the line that contains 'date' (case-insensitive)
            for idx, line in enumerate(lines):
                if re.search(r'\bdate,\b', line, re.IGNORECASE):
                    return idx  # Return the line index where 'date' is found
            return 0  # Default to 0 if no 'date' is found, meaning skip no rows
    
        except Exception as e:
            print(f"Error reading the file for {file_path}: {e}")
            return 0  #Return 0 if something goes wrong, to avoid skipping rows