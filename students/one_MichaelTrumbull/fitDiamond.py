import numpy as np
import matplotlib.pyplot as plt

"""
This file loads/plots 2-column-data from /data/data.txt
then finds two polyfits x in [3,10]
"""

### Load data ###
print('hello world')
data = np.loadtxt('data/data.txt')
print (data)

x = data[:,0]
y = data[:,1]

### Plot data ###
plt.plot(x,y,"o",label="data")

### Fit data ###
x_fit = np.linspace(3,10,100)
### n=3 ###
z = np.polyfit(x,y,3)
fit = np.poly1d(z)
y_fit = fit(x_fit)
plt.plot(x_fit,y_fit,label="n=3 fit")
### n=4 ###
z = np.polyfit(x,y,4)
fit = np.poly1d(z)
y_fit = fit(x_fit)
plt.plot(x_fit,y_fit,label="n=4 fit")

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
