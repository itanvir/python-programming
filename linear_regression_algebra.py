import numpy as np
import matplotlib.pyplot as plt

# Data
rng = np.random.RandomState(123)
mean = np.array([100, 1000])
cov = np.array([[1, 0.9], [0.9, 1]])
sample = rng.multivariate_normal(mean, cov, size=100)
xdata, ydata = sample[:, 0], sample[:, 1]

# Linalg with ones
X = np.column_stack([np.ones(len(xdata)),xdata])
X = np.matrix(X)
y = np.matrix(ydata).T

b = np.linalg.inv(X.T*X) * (X.T*y)
ypred1 = X*b
ypred1 = np.squeeze(np.asarray(ypred1))

# Linalg without ones (this will not work)
X = np.matrix(xdata).T
y = np.matrix(ydata).T

b = np.linalg.inv(X.T*X) * (X.T*y)
ypred2 = X*b
ypred2 = np.squeeze(np.asarray(ypred2))

# Using polyfit
w = np.polyfit(xdata, ydata, deg=1)
b, w1 = w[1], w[0]
ypred3 = xdata*w1 + b

# Std errors
print (np.nanstd(ypred1 - ydata))
print (np.nanstd(ypred2 - ydata))
print (np.nanstd(ypred3 - ydata))

# Figure
plt.figure()
plt.scatter(ydata, ypred1)
plt.scatter(ydata, ypred2)
plt.scatter(ydata, ypred3)
