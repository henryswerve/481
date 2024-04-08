# Henry Tran
# ECON 481
# Pset 2

import numpy as np
import scipy.optimize

# exercise 0 

def github() -> str:
    """
    some docstrings.
    """

    return "https://github.com/henryswerve/481/blob/main/pset2.py"

# exercise 1

# please write a function that returns 1000 simulated observations via the
# following data generating process:
# y_i = 5 + 3 * x_i1 + 2 * x_i2 + 6 * x_i3 + e_i
# x_i1, x_i2, x_i3 ~ N(0,2) and e_i ~ N(0,1)
# N(mu, sigma). mu is 0 for x_i1 -> x_i3, variance is 2. 
# mu is 0 for e_i, variance is 1

seed = 481

# x_1 = np.random.normal(0, 2, 1000)
# x_2 = np.random.normal(0, 2, 1000)
# x_3 = np.random.normal(0, 2, 1000)
# e_i = np.random.normal(0, 1)
# y = np.random.normal(0, 2, 1000)

# newx_1 = 3 * x_1
# newx_2 = 2 * x_2
# newx_3 = 6 * x_3

# y = np.array([y])
# y_T = np.transpose(y)
# print(y_T.shape)
# print(y_T)
# print(y)

# X = np.array([x_1, x_2, x_3])

# empty = (0 , 0)

# np.asarray(empty)

# print(empty)

# fits 1000 x 3 per the problem

# X_T = np.transpose(X)

# print(X_T)

# empty_tuple = np.asarray((y_T, X_T), dtype = tuple)

# empty_tuple = (y_T.flatten(), X_T)

# print(empty_tuple)

# print(len(empty_tuple))

def simulate_data(seed: int) -> tuple:
    """
    Some docstrings.
    """
    seed = np.random.default_rng(seed = 481)
    plus_5 = 5 * np.ones((1000, 1))
    x_1 = seed.normal(0, 2, 1000)
    x_2 = seed.normal(0, 2, 1000)
    x_3 = seed.normal(0, 2, 1000)
    e_i = seed.normal(0, 1)
    y = seed.normal(0, 2, 1000)

    newx_1 = 3 * x_1 + plus_5
    newx_2 = 2 * x_2 + plus_5
    newx_3 = 6 * x_3 + plus_5
    X_tobe = np.array([x_1, x_2, x_3])
    X = np.transpose(X_tobe)

    y_tobe = np.array([y])
    y = np.transpose(y_tobe)

    y_and_x = (y, X)
    return y_and_x

print(simulate_data(481))

# exercise 2

# print(y_and_x)

def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    Some docstrings.
    """


    return None

# print(estimate_mle())

# exercise 3

def estimate_ols(y: np.array, X: np.array) -> np.array:
    """
    Some docstrings.
    """

    return None