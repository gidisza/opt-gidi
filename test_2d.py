import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import approx_fprime
# def approx_fprime(x,target,epsilon):
#     return (target(x+epsilon) - target(x))/epsilon
import math
import copy
plt.ion()
plt.show()

def target(x):
    return -(x[0] ** 2 + x[1] ** 2) + 4


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

Z = target([X, Y])
fig, ax = plt.subplots()
# ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.contour(X,Y,Z)
plt.show()
last_point = np.random.random(2)*10
last_val = target(last_point)
der_vec = np.ones(2)*np.inf
alpha = 0.1
new_point = copy.copy(last_point)
new_point = new_point + np.random.random(2)*alpha
while np.abs(der_vec).max() > .1:  
    val = target(new_point)
    last_point
    # der = 1/ ((val - last_val) /new_point - last_point)
    der = approx_fprime(new_point,target,epsilon=0.01)
    last_val = val
    der_vec = der
    
    last_point = copy.copy(new_point)
    new_point = new_point + der_vec*alpha
    ax.scatter(last_point[0], last_point[1])
    print(f"location: {last_point}, value: {val}, der: {der_vec}")
    print(last_point)
    plt.pause(0.04)
    if math.isnan(val):
        break


