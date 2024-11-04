# We want to write a function that increments a date by adding a number of years, months, days to it.
# We break the task into small ones by writing three functions that add days, months and years respectively.
# We then use the three functions to accomplish the task.

# Function to add years to a date

def add_years(date, years):
    import datetime as dt
    try:
        return date.replace(year = date.year + years)
    except ValueError:
        return date + (dt.date(date.year + years, 1, 1) - dt.date(date.year, 1, 1))
    
# Function to add months to a date

def add_months(date, months):
    import datetime as dt
    month = date.month - 1 + months
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, [31, 29 if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return dt.date(year, month, day)

# Function to add days to a date

def add_days(date, days):
    import datetime as dt
    return date + dt.timedelta(days)

# Function to increment a date by adding a number of years, months, days to it

def increment_date(date, years, months, days):