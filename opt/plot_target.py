import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

def plot_target(target):
    plt.ion()
    plt.show()

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)

    Z = target([X, Y])
    fig, ax = plt.subplots()
    ax.contour(X, Y, Z, levels=30, locator=ticker.LogLocator())
    plt.show()
    return ax

