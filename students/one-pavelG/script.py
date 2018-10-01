import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data/data.txt')

X = data[:,0]
Y = data[:, 1]

coef = np.polyfit(X, Y, 2)

fit = np.poly1d(coef)
fitted_data = fit(X)


f, ax = plt.subplots()
ax.scatter(X, Y, label = 'Real Data')
ax.plot(X, fitted_data, label = 'Quadratic Fit')
ax.set_title('Example Plot')
ax.legend()
plt.show()


crit = fit.deriv().r



print('If we complete the square on the equation we get the following formula:')
print('0.226729 * (x − 6.74078)^2 − 9.14145')
print('Which means the minimum point of the fitted parabola is at X =', crit)
print('and the curvature is 0.226729')
