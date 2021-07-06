import numpy as np
from typing import Callable
from dataclasses import dataclass
import matplotlib.pyplot as plt

from .plot_target import plot_target
from target_functions import himmelblaus


def update_simplex_graph_callback(simplex, center, ax):
    a = ax.plot([s.loc[0] for s in simplex + [simplex[0]]], [s.loc[1] for s in simplex + [simplex[0]]])

    b = ax.scatter(center[0], center[1])
    plt.pause(0.1)
    if a is not None:
        a.pop().remove()


@dataclass
class SimplexHead:
    loc: np.ndarray
    val: float

    @classmethod
    def new_simplex_head(cls, func, x):
        return cls(loc=x, val=func(x))


# TODO: implement boundaries
# TODO: non-convex handling
def nedler_mead_optimize(target: Callable[[np.ndarray], float], variables_num, termination_dist=0.00001,
                         initial_guess=None, alpha=1., gamma=2.,
                         rho=-0.5, sigma=0.5, graphics=False):
    """
    implementation of the nedler-mead method for numeric optimization with no known jacobian
    based on Wikipedia
    :param graphics: show animation plot of optimization
    :param termination_dist: termination criteria for distance between solutions
    :param target: function to minimize
    :param variables_num: target function input dimension
    :param initial_guess: suggested initial guess for optimization
    :param alpha: reflection coefficient
    :param gamma: expansion coefficient
    :param rho: contraction coefficient
    :param sigma: shrink coefficient
    :return: location and value of found minima
    """
    # random start simplex
    simplex = [SimplexHead.new_simplex_head(func=target, x=np.random.random(variables_num) * 30 - 15) for i in
               range(variables_num + 1)]
    if graphics:
        ax = plot_target(target)
    last_best = SimplexHead(np.array([0, 0, 0]), np.inf)
    while True:

        # 1. Sorting
        simplex = sorted(simplex, key=lambda x: x.val)
        if abs(simplex[1].val - simplex[0].val) < termination_dist:
            return simplex[0]
        last_best = simplex[0]
        print(simplex)
        # -------------------------------
        # 2. Centroid Calculation
        # -------------------------------
        center = (1 / variables_num) * sum((i.loc for i in simplex[:-1]))
        print(f"center: {center}")

        if graphics:
            update_simplex_graph_callback(simplex, center, ax)

        # -------------------------------
        # 3. Reflection
        # -------------------------------
        reflection_head = SimplexHead.new_simplex_head(x=center + alpha * (center - simplex[-1].loc), func=target)

        if simplex[0].val <= reflection_head.val < simplex[-2].val:
            simplex[-1] = reflection_head
            continue

        # -------------------------------
        # 4. Expansion
        # -------------------------------
        if reflection_head.val < simplex[0].val:
            expand_simplex = SimplexHead.new_simplex_head(func=target,
                                                          x=center + gamma * (reflection_head.loc - center))
            if expand_simplex.val < reflection_head.val:
                simplex[-1] = expand_simplex
            else:
                simplex[-1] = reflection_head
            continue
        # -------------------------------
        # 5. Contraction
        # -------------------------------
        contracted_point = center + rho * (simplex[-1].loc - center)
        contracted_head = SimplexHead.new_simplex_head(func=target, x=contracted_point)
        if contracted_head.val < simplex[-1].val:
            simplex[-1] = contracted_head
            continue
        # -------------------------------
        # 5. Shrink
        # -------------------------------
        simplex[1:] = [SimplexHead.new_simplex_head(func=target, x=simplex[0].loc + sigma * (head.loc - simplex[0].loc))
                       for head in simplex[1:]]


if __name__ == '__main__':
    print(nedler_mead_optimize(target=himmelblaus, variables_num=2, graphics=True, termination_dist=0.001))
