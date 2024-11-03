import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

#Breakout number 3
# #Create an arbitary date time object and add 5 weekd to it

def datetime():
    import datetime as dt
    date = dt.date.today()
    print(date)
    new_date = date + dt.timedelta(weeks=5)
    print(new_date)

    date1 = dt.datetime(2021, 2, 1)
    print(date1)
    new_date1 = date1 + pd.tseries.offsets.BDay(5)
    print(new_date1)
    return date, new_date, date1, new_date1

datetime()

#Breakout number 4

#Create a function number_days_between that - Takes two arguments that are 8-digit integers of the form YYYYMMDD (actually a date), and
#Returns the number of days between the two dates.

#For instance:

#number_days_between(20200617, 20200619) = 2
#number_days_between(20200619, 20100219) = 3773

def number_days_between(date1, date2):
    date1 = pd.to_datetime(str(date1), format='%Y%m%d')
    date2 = pd.to_datetime(str(date2), format='%Y%m%d')
    days = date2 - date1
    return days

print(number_days_between(20200617, 20200619))
print(number_days_between(20200619, 20100219))

