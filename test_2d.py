import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def target(x, y):
    return -(x ** 2 + y ** 2) + 4


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
X,Y = np.meshgrid(x,y)


init_guess = np.random.random(2)
directions = np.array([[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]])*0.01
neighbours = init_guess+directions

Z = target(X,Y)
ax.contour3D(X, Y, Z, 50, cmap='binary')
plt.show()