class BestFit:
#Author: Michael Curley
#This class is used to create a best fit line when comparing the mean windspeed over an extended period of time
#https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy-polyfit
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy


    #Constructor. This is the code that is run when a new instance of the class is created. Here we pass in the dataframe
    def __init__(self, df): #The constructor takes in the dataframe
        self.df = df

    #Create a function to create a best fit line for the petal length and petal width variables
    def best_fit(self):
        #Import the required libraries
        import numpy as np
        import matplotlib.pyplot as plt

        #Create local variables for the petal length and petal width variables
        mean_wind= self.df['Mean Wind Speed (knot)']
        #Convert the petal length variable to a numpy array
        plen = plen.to_numpy()
        #Create a local variable for the petal width variable
        pwdith = self.df['petal_width']
        #Convert the petal width variable to a numpy array
        pwdith = pwdith.to_numpy()

        #Set the font for the x and y axis labels and the title 
        font1 = {'family':'serif','color':'blue','size':20}
        font2 = {'family':'serif','color':'darkred','size':15}

        #Create a figure and axes object
        fig, ax = plt.subplots()
        #Create a scatter plot of the petal length and petal width variables
        ax.plot(plen, pwdith, 'o', label='Original data', markersize=5) #The 'o' is used to create a scatter plot
                                                                        #The markersize is used to set the size of the markers

        #We are using the numpy polyfit function to create a best fit line for the petal length and petal width variables
        #This function returns the coefficients of the best fit line (m and c)
        #The 1 in the function is used to specify that we want a linear best fit line
        m, c = np.polyfit(plen, pwdith, 1)

        #Create the best fit line using the coefficients returned from the polyfit function
        #plen is the x-axis variable
        #m*plen + c is the equation of the line
        #The 'r' is used to set the colour of the line to red
        ax.plot(plen, m*plen + c, 'r', label='Best fit line')

        #Set the x and y axis labels
        ax.set_xlabel('Petal Length (cm)', fontdict=font2)
        ax.set_ylabel('Petal Width (cm)', fontdict=font2)

        #Add a title to the plot
        plt.title('Best fit line for Petal Length and Petal Width', fontdict=font1)
        #Add a legend
        plt.legend()
        #Save the plot as a .png file
        plt.savefig('Plots/best_fit_line.png')
        #Clear the current figure
        plt.clf()
        #Close the current figure
        plt.close('all')

    