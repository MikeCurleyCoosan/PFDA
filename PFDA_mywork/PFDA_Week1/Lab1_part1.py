# Read a csv file and print the contents
# Author: Michael Curley
# The csv file we are reading in is data.csv, stored in the Data_Files directory

import csv

FILENAME= "data.csv"
DATADIR = "../Data_Files/"


with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)