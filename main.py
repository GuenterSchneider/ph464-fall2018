## LIBRARY IMPORTS ##

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


## DATA IMPORTS ##

# Data filename
ifname = "data.txt"

# Import the data
# dtype is float64 for the whole array
# omitting delimiter option lets genfromtxt find data on each line automatically
data = np.genfromtxt(ifname, usecols=(0, 1))

# Use subarray to grab x and y data into their own arrays
x = data[:, 0]
y = data[:, 1]


## PLOTTING ##

# Looks like an xy-plot. Visualize
plt.figure(1)
plt.title("Unknown Data")
plt.plot(x, y, '.', label="Data")
plt.xlabel('x')
plt.ylabel('y')
# plt.show()


## QUADRATIC FITTING ##

# The minimum of the data looks vaguely parabolic, try to fit a function
# Be selective about the data to fit
r = 4
roi = [np.argmin(y) - r, np.argmin(y) + r]

qdfit = np.polyfit(x[roi[0]:roi[1]], y[roi[0]:roi[1]], 2)
xp = np.linspace(x[roi[0]], x[roi[1]])
yp = (qdfit[0] * xp**2) + (qdfit[1] * xp) + qdfit[2]

# Plot the fit data
plt.plot(xp, yp, label="Quadratic Fit")


## NONLINEAR FITTING ##
# Trying to fit a given nonlinear model

# Define the function to fit to
def fitFunction(V, V0, E0, B0, BP):
    t1 = E0
    t2a = ((1 / (BP - 1)) * (V0 / V)**BP) + 1
    t2 = B0 * (V / BP) * (t2a)
    t3 = -1 * B0 * V0 / (BP - 1)

    return (t1 + t2 + t3)

# X region to plot over
xpp = np.linspace(min(x), max(x))

# Guess values for the model to feed to the nonlinear fit
guess = (5, -8, 1, 2.7)
plt.plot(xpp, fitFunction(xpp, *guess), label="Nonlinear guess: V0=%2.1f, E0=%2.1f, B0=%2.1f, BP=%2.1f" % tuple(guess))

# Fit the data to the fit function
popt, pcov = optimize.curve_fit(fitFunction, x, y, p0=guess)

# Plot the nonlinear fit
plt.plot(xpp, fitFunction(xpp, *popt), label="Nonlinear fit: V0=%2.1f, E0=%2.1f, B0=%2.1f, BP=%2.1f" % tuple(popt))

# Plot another nonlinear fit over only the roi
popt2, pcov2 = optimize.curve_fit(fitFunction, x[roi[0]:roi[1]], y[roi[0]:roi[1]], p0=guess)
plt.plot(xp, fitFunction(xp, *popt2), label="Nonlinear fit: V0=%2.1f, E0=%2.1f, B0=%2.1f, BP=%2.1f" % tuple(popt2))

# Show plots
plt.legend()
plt.show()
