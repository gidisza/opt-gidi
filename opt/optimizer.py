from .opt_methods import OPT_METHODS
from typing import Callable,List


def optimize(func: Callable[[float, float, float], float], boundaries: List[float], is_convex: bool, initial_guess: List[float], method: OPT_METHODS):
    if method == OPT_METHODS.GENETIC:
            
    
