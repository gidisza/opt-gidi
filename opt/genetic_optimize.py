from typing import Callable
import numpy as np
from typing import Callable


def genetic_optimize_3(target: Callable[[float, float, float], float],mating_pool_size,mating_num,initial_guess,number_of_generations=5):
    pop_shape = (mating_pool_size,3)
    population = np.random.random(size = pop_shape)+initial_guess
    for gen in range(number_of_generations):
        print("Generation : ", gen)
        fit = target()
    
    
