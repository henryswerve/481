# Henry Tran
# 4/3/24
# ECON 481
# PSET 1

# exercise 0

def github() -> str:
    """
    Returns my github link hopefully
    """
    return "https://github.com/henryswerve/481.git"

# exercise 1

import numpy
import pandas
import scipy
import matplotlib
import seaborn

#exercise 2

def evens_and_odds(n: int) -> dict:
    """
    Takes in a variable n of type int and outputs a dictionary with empty key values
    'evens' and 'odds'. we create empty variables evensum/oddsum and an 
    empty dictionary. The for loop differentiates between evens and odds by
    whether i % 2 has a result of 0, and adds to the total evensum, else we add
    to the total oddsum. We then add these values to the dictionary depending on 
    total type (even or odd) and return that dictionary called dict_1.
    """
    
    # create empty variables and dictionary for use in function
    evensum = 0
    oddsum = 0
    dict_1 = {
    'evens': 0,
    'odds': 0,
    }
    
    # if i % 2 == 0, add to evensum total, else add to oddsum
    for i in range(n):
        if i % 2 == 0:
            evensum += i
        else:
            oddsum += i

    # assigns key values to variables added from for loop above
    dict_1['evens'] = evensum
    dict_1['odds'] = oddsum
    return dict_1

print(evens_and_odds(4))

# exercise 3

from typing import Union
import datetime


def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """
    Function takes in date_1, date_2, and out which are all type string.
    Date_1 and date_2 are changed into datetime objects. Delta takes the absolute 
    difference between date_2 and date_1. The if else statement outputs a string if
    out is "string", changing the variable delta into a string, else outputs the absolute
    difference between date_2 and date_1 if out is "float".

    """

    # converts string to datetime objects
    date_1 = datetime.datetime.strptime(date_1, '%Y-%m-%d')
    date_2 = datetime.datetime.strptime(date_2, '%Y-%m-%d')
    
    # takes absolute difference between date_1 and date_2
    delta = abs(date_2 - date_1)
        
    # if/elif outputs string or float value for printing
    if out == "string":
        return f"There are {str(delta.days)} days between the two dates"
    elif out == "float":
        delta_1 = abs(date_2 - date_1)
        return delta_1.days

print(time_diff('2020-01-03', '2020-01-01', 'float'))

# exercise 4

in_list = ['a', 'b', 'c']

def reverse(in_list: list) -> list:
    """
    Takes in a list and outputs one as well. We create an empty list
    called newlist, and we return that newlist after using the reversed 
    function.
    """
    
    # create empty list called newlist and reverse it
    newlist = []
    newlist = list(reversed(in_list))
    
    return newlist

print(reverse(in_list))

# exercise 5

n = 0
k = 0

def prob_k_heads(n: int, k: int) -> float:
    """
    Takes in variables n and k, which are both type int and outputs a 
    float value denoting the binomial probability. We determine the binomial
    coefficient using the two for loops (ty Lukas for the code), storing the value
    under n_choose_k. We create two empty variables of type int called p_val and
    q_val for the rest of the distribution equation. The for loop determines the values
    for p_val and q_val, where we raise 0.5 to the power i for the range of n to determine 
    the probability of successes, and q_val to the n - i for to determine the failures in the trials. 
    We then output binom_prob, which is the product of n_choose_k, p_val and q_val.
    """

    # binom coef (n choose k part is done, 
    # n_minus_k_fac is the value returned)
    n_minus_k_fac = 1
    for i in range(1, n-k+1):
        n_minus_k_fac *= i
    n_choose_k = 1
    for i in range(k+1, n+1):
        n_choose_k *= i
    n_choose_k /= n_minus_k_fac

    # p^x * q^n-x
    p_val = 0
    q_val = 0
    
    # we know the prob for success/failure is 0.5 for flipping coins
    for i in range(n):
        p_val = 0.5**i
        q_val = 0.5**(n - i)

    binom_prob = n_choose_k * p_val * q_val

    return binom_prob

print(prob_k_heads(1, 1))