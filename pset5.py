# Henry Tran
# Pset 5
# Econ 481

# execise 0

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"

# exericse 1

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

r = requests.get('https://lukashager.netlify.app/teaching/#ECON-481')
# assert r.ok
# print(r.ok)
1

def scrape_code(url: str) -> str:
    """
    Some docstrings.
    """

    return None


