class Download:  
#This class is used to download a zip file from a given URL.
#The file is saved to a specified directory, extracted, and then deleted.
#The class has a single method, downloadZip, which takes the URL of the file to download, 
# the directory to save it in, and an optional file name.
#Author: Michael Curley

    def __init__(self):
        None
        
  
    def downloadZip(self, url, download_dir, file_name=None):

        import os
        import requests
        import zipfile

        self.download_dir = download_dir
        self.url = url
        self.file_name = file_name
        
        try:
            #Check if a file name is provided. If not, use the last part of the URL as the file name
            #The last part of the URL is obtained by splitting the URL at each '/' and taking the last element
            if not self.file_name:
                self.file_name = self.url.split("/")[-1]

            #Set the file path of the downloaded files
            file_path = os.path.join(self.download_dir, self.file_name)
            
            #Send a GET request to download the file
            response = requests.get(self.url)
            
            #Check if the request was successful. Response code 200 indicates success
            if response.status_code == 200:
                # Write the content to the file
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                    print(f"Downloaded {url} to {file_path}")
                
                try:
                    #Open the ZIP file
                    #The zipfile module provides a ZipFile class that can be used to read and write ZIP files
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        # Extract all contents into the specified directory
                        zip_ref.extractall(download_dir)

                    #After extraction, delete the ZIP file
                    os.remove(file_path)
                
                except zipfile.BadZipFile:
                    print(f"Failed to extract {file_path}: Bad ZIP file")
                except Exception as e:
                    print(f"Error extracting {file_path}: {e}")
            
            else:
                print(f"Failed to download {url}: {response.status_code}")
        
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        