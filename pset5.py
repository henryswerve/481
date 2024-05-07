# Henry Tran
# PSET 5
# ECON 481

import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re
import time

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"

# assign link to link
link = "https://lukashager.netlify.app/teaching/#ECON-481"

# test the link
r = requests.get(link)
assert r.ok

# initiailze beautiful soup
soup = BeautifulSoup(r.text, features="lxml")

# find all <a> elements from link
links = soup.find_all('a')

# use regex to filter by digit #, and file extension
match = re.compile('\d{2}[a-z_]+[^.]+$')

# filters hrefs based on match criteria
links = [x['href'] for x in soup.find_all('a', {'href': match})]

# list comprehension to remove the last terms in the list
# is there a better way to do this?
urls = [x for i, x in enumerate(links) if i < 7]

# print(urls)

# for each url, get the text
for url in urls:
    url = f'https://lukashager.netlify.app' + url
    r1 = requests.get(url)
    assert r1.ok
    r1_bs = BeautifulSoup(r1.text, features = 'lxml')
    time.sleep(3)


def scrape_code(url: str) -> str:
    """
    Some docstrings.
    """

    return None