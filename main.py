from numpy import minimum
from opt import OPT_METHODS, optimize
from target_functions import Parabola

from target_functions import himmelblaus

print(optimize(func=lambda x: Parabola(3)(x), variables_num=3, grad_direction=-1, step_size=0.1,
               method=OPT_METHODS.GRAD_DESC,graphics=True))
