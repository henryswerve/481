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

prob_1_array = simulate_data(481)

y = prob_1_array[0]
X = prob_1_array[1]

# exercise 2

print(y)

# pass in x and y from above
# use scipy

beta = np.zeros([4, 1])

def sse_fun(beta: np.array, y: np.array, X: np.array) -> tuple:
    """
    blah blah
    """
    X = np.c_[np.zeros(X.shape[0]).reshape(-1, 1), X]
    sse = np.sum(np.square(y - X @ beta))

    return sse

print(sse_fun(beta, y, X))

# def estimate_mle(mle_fun: np.array, y: np.array, X: np.array) -> np.array:
#     """
#     Some docstrings.
#     """
#     empty_array = np.zeros([4, 1]) # empty array for returning beta coefficients
#     seed = np.random.default_rng(seed = 481)
#     e_i = seed.normal(0, 1, 1000)

    
    # estimation = sp.optimize.minimize(
    #     fun = sse_fun,
    #     args = (y, X),
    #     x0 = beta,
    #     method = 'Nelder-Mead'
    #     )
    # return estimation

# print(estimate_mle())

# exercise 3


def estimate_ols(beta: np.array, y: np.array, X: np.array) -> np.array:
    """
    Some docstrings.
    """
    beta = np.zeros([4, 1])
    beta = beta.flatten()
    estimation = sp.optimize.minimize(
        fun = sse_fun,
        args = (y, X),
        x0 = beta,
        method = 'Nelder-Mead'
        )
    estimation_result = np.array(estimation.x)
    return estimation_result.reshape(-1, 1)

print(estimate_ols(beta, y, X))