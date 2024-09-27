#Reading a csv file as a dictionary object
#Author: Michael Curley
#The csv file we are reading in is data.csv, stored in the Data_Files directory

import csv

FILENAME= "data.csv"
DATADIR = "../Data_Files/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line["age"]
        print (line)
        count += 1
    print (f"Average age: {total/count}")