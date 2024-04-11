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
    Simulates 1000 trials for x values under N ~ (0, 2), where y is the 
    output variable. We then create arrays for y and X, transpose them and 
    return both as a tuple
    """
    np.random.seed(481)
    x_1 = np.random.normal(0, np.sqrt(2), 1000)
    x_2 = np.random.normal(0, np.sqrt(2), 1000)
    x_3 = np.random.normal(0, np.sqrt(2), 1000)
    e_i = np.random.normal(0, 1, 1000)
    y = np.zeros([1000, 1])
    y_tobe = np.array([3 * x_1 + 2 * x_2 + 6 * x_3 + e_i + 5])
    X_tobe = np.array([x_1, x_2, x_3])
    X = np.transpose(X_tobe)
    y = np.transpose(y_tobe)
    y_and_x = (y, X)
    return y_and_x

y, X = simulate_data(481)

# exercise 2

# helper function for exercise 2
def mle_func(beta: np.array, y: np.array, X: np.array) -> tuple:
    sse = np.sum((y - X @ beta.reshape(-1, 1)) ** 2)
    log_likely = -np.sum(sse**2/2) - 500 * np.log(2 * np.pi)

    return -log_likely

def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    Adds extra column of 1s to X array for intercept term. We then run
    minimization function calling in our log_likelihood function from above
    to estimate our beta coefficients. We then output the the coefficients
    in a 4x1 array
    Wrong output for the first coefficient (not close to 5)
    """
    beta = (0, 0, 0, 0)
    X = np.c_[np.zeros(X.shape[0]).reshape(-1, 1), X]

    prob2_results = sp.optimize.minimize(
        fun = mle_func,
        args = (y, X),
        x0 = (0, 0, 0, 0),
        method = 'Nelder-Mead'
        )
    
    prob2_results = prob2_results.x
    return prob2_results.reshape(-1, 1)

print(estimate_mle(y, X))

# exercise 3

# helper function for exercise 3
def sse_function(beta: np.array, y: np.array, X: np.array) -> tuple:

    sse_use = np.sum((y - X @ beta.reshape((-1, 1))) ** 2)
    return sse_use

def estimate_ols(y: np.array, X: np.array) -> np.array:
    """
    Adds extra column of 1s to X array for intercept term, then we run
    minimization function calling in our sse function from above
    to estimate our beta coefficients. We then output the the coefficients
    in a 4x1 array
    """
    X = np.c_[np.ones(X.shape[0]).reshape(-1, 1), X]
    estimation = sp.optimize.minimize(
        fun = sse_function,
        args = (y, X),
        x0 = (0, 0, 0, 0),
        method = 'Nelder-Mead'
        )
    
    estimation_result = np.array(estimation.x)
    return estimation_result.reshape(-1, 1)

print(estimate_ols(y, X))