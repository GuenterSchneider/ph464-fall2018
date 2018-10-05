import numpy as np
import matplotlib.pyplot as plt

"""
This file loads/plots 2-column-data from /data/data.txt
then finds two polyfits x in [3,10]
"""

def mindata(file):
    ### Load data ###
    data = np.loadtxt(file)
    print (data)
    x = data[:,0]
    y = data[:,1]

    ### Plot data ###
    plt.plot(x,y,"o",label="data")

    ### Fit data ###
    x_fit = np.linspace(x[0],x[-1],1000)

    ### parabolic fit ###
    z = np.polyfit(x,y,2)
    fit = np.poly1d(z)
    y_fit = fit(x_fit)

    ### Plot the fit ###
    print( 'Figure 1 is fit to all the data' )
    plt.plot(x_fit,y_fit,"-r",label="Parabolic fit")

    ### Find minimum ###
    minimum = min(y_fit)
    index = np.argmin(y_fit)
    plt.plot(x_fit[index],minimum,'x',label='minimum')
    print('New minimum located at: (', minimum,',',x_fit[index],')')


    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.figure()

    ### * Use minimum 3 values ###
    x_new = [x[np.argmin(y)-1],x[np.argmin(y)],x[np.argmin(y)+1]]
    y_new = [y[np.argmin(y)-1],y[np.argmin(y)],y[np.argmin(y)+1]]

    ### parabolic fit (New) ###
    z = np.polyfit(x_new,y_new,2)
    fit = np.poly1d(z)
    y_fit = fit(x_fit)

    ### Plot the fit (New)###

    plt.plot(x,y,"o",label="data")

    print( 'Figure 2 is fit to the 3 lowest data points' )
    plt.plot(x_fit,y_fit,"-r",label="Parabolic fit (of lowest 3)")

    ### Find minimum (New)###
    minimum = min(y_fit)
    index = np.argmin(y_fit)

    plt.plot(x_fit[index],minimum,'x',label='New min')
    print('New minimum located at: (', minimum,',',x_fit[index],')')


    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()




if __name__=='__main__':
    print( '1 - Fit all data' )
    print( '2 - Find minimum' )
    print( '3 - Fit 3 data points near lowest point' )
    print( '4 - Find better minimum' )
    print( 'This is a test using diamond data: Data.txt' )
    mindata('Data.txt')
