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

#print('Mininum point on linear regression is:', min(fitted_data))
