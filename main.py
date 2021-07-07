from numpy import minimum
from opt import OPT_METHODS, optimize
from target_functions import Parabola

from target_functions import himmelblaus

print(optimize(func=lambda x: himmelblaus(x), variables_num=2, grad_direction=-1, step_size=0.005,
               method=OPT_METHODS.NEDLER_MEAD,graphics=True))
