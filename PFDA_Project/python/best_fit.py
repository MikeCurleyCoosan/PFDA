class BestFit:
#Author: Michael Curley
#This class is used to create a best fit line when comparing the mean windspeed over an extended period of time
#https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy-polyfit
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy
    #Constructor. This is the code that is run when a new instance of the class is created. Here we pass in the dataframe
    def __init__(self, df): #The constructor takes in the dataframe
        self.df = df

    #Create a function to create a best fit line for the petal length and petal width variables
    def best_fit(self, placename):
        #Import the required libraries
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates

        #Set the placename variable to the placename passed in
        self.placename = placename
        #Create a variable to store the column name for the mean wind speed
        windspeed = 'Mean Wind Speed (knot)_'+self.placename #Create a variable to store the column name for the mean wind speed 
        print(windspeed)

        bestfit = self.df[['Date/Time (utc)', windspeed]]

        #Convert the Mean Wind Speed (utc) column to m/s
        bestfit['Mean Wind Speed (m/s)'] = round(bestfit[windspeed] * 0.514444, 2)

        #Resample for monthly wind speed data while keeping the mean and the index as the date
        bestfit = bestfit.resample('ME', on='Date/Time (utc)').mean()

        #Select data from 2012 onwards
        bestfit_2012 = bestfit[bestfit.index.year >= 2012].copy()

        #Convert the Date/Time (utc) column to a number so that it can be used in the polyfit function
        bestfit_2012['DateNumber'] = mdates.date2num(bestfit_2012.index)

        #Calculate the best fit parameters for the wind speed data m,c
        idx = np.isfinite(bestfit_2012['DateNumber']) & np.isfinite(bestfit_2012['Mean Wind Speed (m/s)'])

        #Calculate our values for m and c
        m, c = np.polyfit(bestfit_2012['DateNumber'][idx], bestfit_2012['Mean Wind Speed (m/s)'][idx], 1)

        #Plot the best fit line

        #Set the font for the# x and y axis labels and the title 
        font1 = {'family':'serif','color':'blue','size':20}
        font2 = {'family':'serif','color':'darkred','size':15}

        #Create a figure and axes object
        fig, ax = plt.subplots()
        #Create a scatter plot of the wind speed data from 2012 onwards
        ax.plot(bestfit_2012['Mean Wind Speed (m/s)'], 'o', label='Data', color='blue', markersize=5) #The 'o' is used to create a scatter plot

        #Create the best fit line using the coefficients returned from the polyfit function
        ax.plot(m*bestfit_2012['DateNumber'] + c, 'r-', label='Best fit line')

        #Set the x and y axis labels
        ax.set_xlabel('Year', fontdict=font2)
        ax.set_ylabel('Mean Wind Speed (m/s)', fontdict=font2)

        #Add a title to the plot
        plt.title('Best fit line for Wind Speed data from 2012', fontdict=font1)
        #Add a legend
        plt.legend(loc='upper right', fontsize=12)

        
        #Save the plot as a .png file
        plt.savefig('images/best_fit_line.png')
        #Clear the current figure
        plt.clf()
        #Close the current figure
        plt.close('all')

    