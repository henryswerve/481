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

def scrape_code(url: str) -> str:
    """
    Some docstrings.
    """
    # assign link to link
    link = "https://lukashager.netlify.app/teaching/#ECON-481"

    # test the link
    r = requests.get(link)
    assert r.ok

    # initiailze beautiful soup
    soup = BeautifulSoup(r.text, features="lxml")

    # # find all <a> elements from link
    # dont think we need this
    # links = soup.find_all('a')

    # use regex to filter by digit #, and file extension
    match = re.compile('\d{2}[a-z_]+[^.]+$')

    # filters hrefs based on match criteria
    links = [x['href'] for x in soup.find_all('a', {'href': match})]

    # list comprehension to remove the last terms in the list
    # is there a better way to do this?
    tobe_urls = [x for i, x in enumerate(links) if i < 7]

    # print(urls)

    # for each url, get the links and create urls_list
    # and obtain the html text using BeautifulSoup
    urls_list = []
    for url in tobe_urls:
            tobe_list = f'https://lukashager.netlify.app{url}'
            r1 = requests.get(tobe_list)
            assert r1.ok
            r1_bs = BeautifulSoup(r1.text, features = 'lxml')
            urls_list.append(tobe_list)
            time.sleep(3)

    testbs = BeautifulSoup(r1.text, features = 'lxml')
    search_criteria = ["sourceCode cell-code"]
    test_soup = testbs.body.find_all("div", search_criteria)

    tobe_string = ""
    for urls in urls_list:
        r_test = requests.get(urls)
        assert r_test.ok
        testbs = BeautifulSoup(r1.text, features = 'lxml')
        search_criteria = ["sourceCode"]
        test_soup = testbs.body.find_all('div', search_criteria)
        code_strings = [tag.get_text() for tag in test_soup]
        joined_string = "\n".join(code_strings)
        tobe_string += joined_string    
        time.sleep(3)

    return tobe_string

print(scrape_code("https://lukashager.netlify.app/econ-481/01_intro_to_python#"))