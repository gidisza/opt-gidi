import numpy as np


class Parabola:
    def __init__(self, variables_num):
        self._variables_num = variables_num
        pass

    def __call__(self, input_arr: np.ndarray):
        if len(input_arr.shape) != 1:
            raise Exception("array must be 1D!")

        if input_arr.shape[0] != self._variables_num:
            raise Exception(f"number of params is not equal to function params which is {self._variables_num}")

        return (input_arr ** 2).sum()
