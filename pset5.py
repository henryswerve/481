# Henry Tran
# PSET 5
# ECON 481

import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re
import time

#exercise 0

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/henryswerve/481/blob/main/pset5.py"

# exercise 1

def scrape_code(url: str) -> str:
    """
    Scrapes code from 481 slides using beautiful soup.
    Obtains code from div elements and adds each line of code as 
    new lines to be returned at the end of the function.
    """

    # check for connection to url
    r1 = requests.get(url)
    assert r1.ok

    #initialize beautifulsoup
    bs = BeautifulSoup(r1.text, features = 'lxml')

    # create search criteria 
    search_criteria = ["sourceCode"]

    # find the code lines under div using the criteria
    find_div = bs.body.find_all('div', search_criteria)

    # obtain the code under tag elements
    code_tobe = [tag.get_text() for tag in find_div]

    # add each line of code on each new line
    joined_string = "\n".join(code_tobe)   

    return joined_string