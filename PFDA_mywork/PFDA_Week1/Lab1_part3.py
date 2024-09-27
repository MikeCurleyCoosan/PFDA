#Modify the program in part 2 to calculate the average age of the people in the list.
#Print the result to the console.
#Author: Michael Curley

import csv

FILENAME= "data.csv"
DATADIR = "../Data_Files/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total_age = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
        else: # all subsequent rows
            total_age += int(line[1])
            print (line)
        linecount += 1
    print (f"Average age: {total_age/(linecount-1)}")