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
    new lines after omitting for % to be returned at the end of the function.
    """

    # check for connection to url
    r1 = requests.get(url)
    assert r1.ok

    #initialize beautifulsoup
    bs = BeautifulSoup(r1.text, features = 'lxml')

    # find the code lines under div using the criteria
    find_div = bs.body.find_all('code', attrs = {"class": "sourceCode python"})

    # obtain the code under tag elements
    code_tobe = [tag.get_text() for tag in find_div]

    # add each line of code on each new line
    joined_string = "\n".join(code_tobe)  

    # omit % using regex
    cleaned_string = re.sub(r'^\s*%.*$', '', joined_string, flags=re.MULTILINE)

    time.sleep(3)

    return cleaned_string

print(scrape_code("https://lukashager.netlify.app/econ-481/01_intro_to_python#/title-slide"))