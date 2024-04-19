# Henry Tran
# Pset 4
# Econ 481

# exercise 0 
def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/henryswerve/481/blob/main/pset4.py"

# exercise 1

import pandas as pd

def load_data() -> pd.DataFrame:
    """
    Some docstrings.
    """
    directory = f'https://lukashager.netlify.app/econ-481/data/TSLA.csv'
    data = pd.read_csv(directory)

    return data

df = load_data()

# exercise 2

import matplotlib.pyplot as plt

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Some docstrings
    """
    fig = plt.figure()
    ax = fig.add_subplot()

    # ax.plot(df, color = "black",
    #         linestyle = "dashed", marker = "o")