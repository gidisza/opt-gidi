from typing import Callable
import numpy as np


class GradientDescent:
    def __init__(self, variables_num,step_size,epsilon = 0.001, eps_grad = 0.000001):
        self._variables_num = variables_num

    def __call__(self, target: Callable, initial_guess=None):
        if initial_guess is None:
            initial_guess = np.random.random(3) * 10
        

