import pandas as pd
import numpy as np

#Create a list

listData = [
    ['John', 'math', 23],
    ['John', 'english', 25],
    ['John', 'science', 24],
    ['Jane', 'math', 22],
    ['Jane', 'english', 21],
    ['Jane', 'science', 26],
    ['Tom', 'math', 25],
    ['Tom', 'english', 24],
    ['Tom', 'science', 25]
]   

#Create a DataFrame object

df = pd.DataFrame(listData, columns=['Name', 'Subject', 'Grade'])

#Print the DataFrame
print(df.head())

#Write this dataframe to a csv file
path = './data/'
FILENAME = path + 'grades.csv'
df.to_csv(FILENAME)

#Write this dataframe to an excel file

EXCEL_FILE = path + 'grades.xlsx'
df.to_excel(EXCEL_FILE, index=False, sheet_name='grades')


