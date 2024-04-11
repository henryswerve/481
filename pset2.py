# Henry Tran
# ECON 481
# Pset 2

import numpy as np
import scipy as sp

# exercise 0 

def github() -> str:
    """
    some docstrings.
    """

    return "https://github.com/henryswerve/481/blob/main/pset2.py"

# exercise 1 done

seed = 481

def simulate_data(seed: int) -> tuple:
    """
    Some docstrings.
    """
    np.random.seed(481)
    x_1 = np.random.normal(0, np.sqrt(2), 1000)
    x_2 = np.random.normal(0, np.sqrt(2), 1000)
    x_3 = np.random.normal(0, np.sqrt(2), 1000)
    e_i = np.random.normal(0, 1, 1000)
    y = np.zeros([1000, 1])
    y_tobe = np.array([3 * x_1 + 2 * x_2 + 6 * x_3 + e_i + 5])
    X_tobe = np.array([3 * x_1, 2 * x_2, 6 * x_3])
    X = np.transpose(X_tobe)
    y = np.transpose(y_tobe)

    y_and_x = (y, X)
    return y_and_x

# prob_1_array = simulate_data(481)

y = simulate_data(481)[0]
X = simulate_data(481)[1]

# print(y)
# print(X.shape)


# y = prob_1_array[0]
# X = prob_1_array[1]

# exercise 2

# print(y)

# pass in x and y from above
# use scipy

# beta = (0, 0, 0, 0)

# def sse_fun(beta: np.array, y: np.array, X: np.array) -> tuple:
#     """
#     blah blah
#     """
#     X = np.c_[np.zeros(X.shape[0]).reshape(-1, 1), X]
#     sse = np.sum(np.square(y - X @ beta))

#     return sse

# print(sse_fun(beta, y, X))

# def sse_function(y: np.array, X: np.array) -> tuple:

#     beta = (0, 0, 0)
#     sse_use = np.sum(np.square(y - X @ beta))

#     return sse_use

def sse_function_1(y: np.array, X: np.array) -> tuple:

    sse_use = np.sum(np.square(y - X @ (0, 0, 0)))

    return sse_use

# print(sse_function(y, X))

# def estimate_mle(y: np.array, X: np.array) -> np.array:
#     """
#     Some docstrings.
#     """
#     X = np.c_[np.zeros(X.shape[0]).reshape(-1, 1), X]
#     empty_array = np.zeros([4, 1]) # empty array for returning beta coefficients
#     beta = (0, 0, 0, 0)
#     sse = np.sum(np.square(y - X @ beta))
#     log_likely = -np.sum(sse**2/2) - 1000 / 2 * np.log(2 * np.pi * 1)
    
#     estimation = sp.optimize.minimize(
#         fun = log_likely,
#         args = (y, X),
#         x0 = (0, 0, 0, 0),
#         method = 'Nelder-Mead'
#         )
    
#     return estimation

# print(estimate_mle(y, X))

# exercise 3


def estimate_ols(y: np.array, X: np.array) -> np.array:
    """
    Some docstrings.
    """
    beta = (0, 0, 0, 0)
    X = np.c_[np.zeros(X.shape[0]).reshape(-1, 1), X]
    
    estimation = sp.optimize.minimize(
        fun = sse_function,
        args = (y, X),
        x0 = (0, 0, 0, 0),
        method = 'Nelder-Mead'
        )
    
    estimation_result = np.array(estimation.x)
    return estimation_result.reshape(-1, 1)

print(estimate_ols(y, X))