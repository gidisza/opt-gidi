from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from .plot_target import plot_target


def calculate_local_derivative(target, x, epsilon):
    der = np.zeros_like(x)
    for i in range(x.shape[0]):
        point_1 = x.copy()
        point_2 = x.copy()
        point_1[i] += epsilon
        point_2[i] -= epsilon
        der[i] = (target(point_1) - target(point_2)) / (2 * epsilon)
    return der


class GradientDescent:
    def __init__(self, variables_num, epsilon=0.001, graphics=False, **kwargs):
        self._variables_num = variables_num

        self.epsilon = epsilon
        self._grad_dir = 1
        self._graphics = graphics
        if "grad_direction" in kwargs:
            self._grad_dir = kwargs["grad_direction"]
        if "step_size" in kwargs:
            self._step_size = kwargs["step_size"]
        else:
            self._step_size = 0.01

    def __call__(self, target: Callable, initial_guess=None):
        if self._graphics:
            ax = plot_target(target)

        if initial_guess is None:
            last_point = np.random.random(self._variables_num) * 10
        else:
            last_point = initial_guess
        last_val = target(last_point)
        der_vec = np.ones(2) * np.inf
        alpha = 0.1
        new_point = last_point.copy()
        new_point = new_point + np.random.random(self._variables_num) * alpha
        while np.abs(der_vec).max() > .1:
            val = target(new_point)
            der = self._grad_dir * calculate_local_derivative(
                target, new_point, self.epsilon)
            last_val = val
            der_vec = der

            last_point = new_point.copy()
            new_point = new_point + der_vec * self._step_size
            if self._graphics:
                ax.scatter(*new_point)
                plt.pause(0.08)
        return last_point, last_val
