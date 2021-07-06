import numpy as np


def himmelblaus(input_arr: np.ndarray):
        return (input_arr[0]**2+input_arr[1]-11) ** 2 + (input_arr[0]+input_arr[1]**2-7)**2
