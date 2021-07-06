from .opt_methods import OPT_METHODS
from typing import Callable, List
import numpy as np


def optimize(func: Callable[[np.ndarray], float], boundaries: List[float] = None, is_convex: bool = True,
             initial_guess: List[float] = None, method: OPT_METHODS = OPT_METHODS.GRAD_DESC, variables_num=3,
             graphics=False, **kwargs):
    if method == OPT_METHODS.GENETIC:
        # TODO: implement
        raise NotImplementedError

    if method == OPT_METHODS.GRAD_DESC:
        from .gradient_descent import GradientDescent
        return GradientDescent(variables_num=variables_num, graphics=graphics, **kwargs)(target=func)

    if method == OPT_METHODS.NEDLER_MEAD:
        from .nedler_mead import nedler_mead_optimize
        return nedler_mead_optimize(target=func, variables_num=3, termination_dist=0.001, initial_guess=initial_guess,
                                    graphics=graphics)
