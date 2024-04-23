# Henry Tran
# Pset 4
# Econ 481

# exercise 0 
def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/henryswerve/481/blob/main/pset4.py"

# exercise 1 ok

import pandas as pd

def load_data() -> pd.DataFrame:
    """
    Some docstrings.
    """
    directory = f'https://lukashager.netlify.app/econ-481/data/TSLA.csv'
    data = pd.read_csv(directory,
                       index_col = 0,
                       parse_dates = ['Date'])
    return data

df = load_data()
# exercise 2 ok

import matplotlib.pyplot as plt

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Some docstrings
    """
    
    start = pd.to_datetime([start])
    end = pd.to_datetime([end])
    fig = plt.figure()
    ax = fig.add_subplot()
    graph = ax.plot(df['Close'], color = 'blue',
                    linestyle = '-', marker = 'o')
    ax.set_xlim(start, end)
    closing = df['Close']
    plt.plot(closing)
    plt.show()

    return None

# print(plot_close(df, '2010-06-29', '2024-04-15'))

# exercise 3

import statsmodels.api as sm

# need to make sure dates are consecutive
df['Date'] = pd.to_datetime(df['Date'])
reg = sm.OLS(df['Close'], df['Date'])
results = reg.fit()
results.params

def autoregress(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """

    reg = sm.OLS(df['Close'], df['Date'])
    tstat = 3
    return None