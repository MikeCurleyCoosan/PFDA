class BestFit:
#Author: Michael Curley
#This class is used to create a best fit line when comparing the mean windspeed over an extended period of time
#The class takes in a dataframe and a placename as arguments. The class contains one function called best_fit which creates a best fit line for the mean wind speed data
#The best fit line is created using the polyfit function from the numpy library
#The best fit line is then plotted using the matplotlib library
#The plot is saved as a .png file in the images folder
#https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy-polyfit
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy
    #Constructor. This is the code that is run when a new instance of the class is created. Here we pass in the dataframe
    def __init__(self, df): #The constructor takes in the dataframe
        self.df = df

    #Create a function to create a best fit line for the mean wind speed data
    def best_fit(self, placename):
        #Import the required libraries
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates

        #Set the placename variable to the placename passed in as an argument to the function
        self.placename = placename
        #Create a variable to store the column name for the mean wind speed
        windspeed = 'Mean Wind Speed (m/s)_'+self.placename #Create a variable to store the column name for the mean wind speed 
        print(windspeed)

        bestfit = self.df[['Date/Time (utc)', windspeed]].copy() 

        #Convert the Mean Wind Speed (utc) column to m/s
        bestfit['Mean Wind Speed (m/s)'] = round(bestfit[windspeed], 2)

        #Resample for monthly wind speed data while keeping the mean and the index as the date
        bestfit = bestfit.resample('ME', on='Date/Time (utc)').mean()

        #Select data from 2012 onwards
        bestfit_2012 = bestfit[bestfit.index.year >= 2012 and bestfit.index.year <=2024].copy()

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
        #Plot the best fit line
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))

        #Set up a function to format the y axis
        def windspeed_formatter(windspeed, pos):
            s = f"{windspeed} (m/s)"
            return s

        #Create a scatter plot of the wind speed data from 2012 onwards
        ax.plot(bestfit_2012['Mean Wind Speed (m/s)'], 'o', label='Data', color='blue', markersize=5) #The 'o' is used to create a scatter plot

        #Create the best fit line using the coefficients returned from the polyfit function
        ax.plot(m*bestfit_2012['DateNumber'] + c, 'r-', label='Best fit line')

        #Set the x and y axis labels
        ax.set_xlabel('Year', fontdict=font2)
        ax.set_ylabel('Mean Wind Speed (m/s)', fontdict=font2)

        title = 'Best fit line for Wind Speed for '+self.placename+' from 2012'

        #Add a title to the plot
        plt.title(title, fontdict=font1)

        #Add a legend
        ax.legend(loc='upper right', fontsize=12)

        #Set the major locator to every 2nd day, minor locator to every day.
        ax.xaxis.set_major_locator(mdates.YearLocator())  
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  
        ax.yaxis.set_major_formatter(plt.FuncFormatter(windspeed_formatter))

        #Add ticks
        plt.xticks(fontsize=12, rotation=45)
        plt.yticks(fontsize=12)

        #Add a grid
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)

        save_path = 'images/best_fit_line_'+self.placename+'.png'
        #Save the plot as a .png file
        plt.savefig(save_path)
        #Clear the current figure
        plt.clf()
        #Close the current figure
        plt.close('all')

    