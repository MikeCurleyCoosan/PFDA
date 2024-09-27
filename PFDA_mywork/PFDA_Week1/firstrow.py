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
