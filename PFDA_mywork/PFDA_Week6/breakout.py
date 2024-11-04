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

#Breakout number 5

#On july 16th, the huge  363-feet Saturn V rocket was launched on the Apollo 11 mission form Pad 39A at the Kennedy Space
#center in Florida. The rocket was launched at 9:32am EDT. Write a function that computes (from now) the number of 

#years
#months
#days
#hours
#minutes
#seconds

#since the launch of the rocket.

def time_since_launch():
    import datetime as dt
    current_date = dt.datetime.now()
    launch_date = dt.datetime(1969, 7, 16, 9, 32)
    duration = current_date - launch_date

    duration_in_s = duration.total_seconds()
    years = divmod(duration_in_s, 31536000 )[0] # Seconds in a year = 365*24*60*60
    months = divmod(duration_in_s, 2628000 )[0] # Seconds in a month = 30*24*60*60
    days = divmod(duration_in_s, 86400 )[0] # Seconds in a day = 24*60*60
    hours = divmod(duration_in_s, 3600 )[0] # Seconds in an hour = 60*60
    minutes = divmod(duration_in_s, 60 )[0] # Seconds in a minute = 60

    return years, months, days, hours, minutes, duration_in_s

print(time_since_launch())
