import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def local_derivative(x,target,epsilon):
    der = np.array([0,0])
    for i in [0,1]:
        point_1 = x.copy()
        point_2 = x.copy()
        point_1[i]+=epsilon
        point_2[i]-=epsilon
        der[i] = (target(point_1)- target(point_2))/(2*epsilon)
    return der
import math
import copy
plt.ion()
plt.show()

def target(x):
    return -(x[0] ** 2 + x[1] ** 2) + 4

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

Z = target([X, Y])
fig, ax = plt.subplots()
ax.contour(X,Y,Z)
plt.show()
last_point = np.random.random(2)*10
last_val = target(last_point)
der_vec = np.ones(2)*np.inf
alpha = 0.5
new_point = copy.copy(last_point)
new_point = new_point + np.random.random(2)*alpha
while np.abs(der_vec).max() > .1:  
    val = target(new_point)
    last_point
    der = local_derivative(new_point, target, epsilon=0.01)
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

