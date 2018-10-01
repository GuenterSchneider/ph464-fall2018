import numpy as np
import matplotlib.pyplot as plt

"""
This file loads/plots 2-column-data from /data/data.txt
then finds two polyfits x in [3,10]
"""

### Load data ###
print('hello world')
data = np.loadtxt('data.txt')
print (data)

x = data[:,0]
y = data[:,1]

### Plot data ###
plt.plot(x,y,"o",label="data")

### Fit data ###
x_fit = np.linspace(3,10,500)
### parabolic ###
z = np.polyfit(x,y,3)
fit = np.poly1d(z)
y_fit = fit(x_fit)
plt.plot(x_fit,y_fit,"-r",label="n=3 fit")
min = min(y_fit)

print('Minimum located at: ', min)

### n=4 fit ###
z = np.polyfit(x,y,4)
fit = np.poly1d(z)
y_fit = fit(x_fit)
plt.plot(x_fit,y_fit,"-b",label="n=4 fit")

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
