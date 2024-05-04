# Henry Tran
# PSET 5
# ECON 481

import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"

link = "https://lukashager.netlify.app/teaching/#ECON-481"

r = requests.get(link)
assert r.ok

soup = BeautifulSoup(r.text, features="lxml")

links = soup.find_all('a')
# url_pattern = re.compile("https://lukashager.netlify.app/econ-481/00_intro_to_481#/title-slide")

url_pattern = re.compile("https://lukashager.netlify.app/econ-481/\d{2}_\[a-z]#/title-slide")


# match = url_pattern.match(link)

# if match:
#     print("matched")
# else:
#     print("no")


links = [x['href'] for x in soup.find_all('a', {'href': url_pattern})]
print(links[:5])



def scrape_code(url: str) -> str:
    """
    Some docstrings.
    """

    return None