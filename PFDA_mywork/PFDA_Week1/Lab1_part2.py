# Read in a csv file and print the contents. This time, we will print the header row and all subsequent rows separately.
# Author: Michael Curley
# The csv file we are reading in is data.csv, stored in the Data_Files directory
# Seperating the header row is useful if you want to run some operations on the data, but not on the header row.

import csv

FILENAME= "data.csv"
DATADIR = "../Data_Files/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount: # first row ie header row
            print (f"{line}\n-------------------")
        else: # all subsequent rows
            print (line)
        linecount += 1
