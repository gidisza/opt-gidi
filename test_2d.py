import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
plt.ion()
plt.show()

def target(x, y):
    return -(x ** 2 + y ** 2) + 4


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

Z = target(X, Y)
fig, ax = plt.subplots()
# ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.contour(X,Y,Z)
plt.show()
# plt.show()
init_guess = np.random.random(2)*10
# directions = np.array([[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]])*0.01
init_val = target(*init_guess)
new_target = init_guess + np.random.random(2)
der = np.array([1,1])*np.inf
while np.abs(der).max()>.001:
    val = target(*new_target)
    der = (new_target - init_guess) / (val - init_val)
    ax.scatter (new_target[0],new_target[1])
    print(f"location: {new_target}, value: {val}, der: {der}")
    init_guess = new_target
    init_val = val
    new_target = init_guess + 2 * der
    print(new_target)
    plt.waitforbuttonpress()
    if math.isnan(val):
        break


