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
    # data.reset_index(inplace = True) plot is correct without this as code
    return data

df = load_data()
# print(df)
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
    plt.show()

    return None
# adding the index (data.reset_index(inplace = True)) shifts my graph to the 70s... removing it doesn't bring it back to normal
# however, i think i need it for problem 3 when im shifting??
# print(plot_close(df, '2010-06-29', '2024-04-15'))

# exercise 3

import statsmodels.api as sm

# need to make sure dates are consecutive
# print(df)
# print(type(df['Date']))
# df['Date'] = pd.to_datetime(df['Date'])

# df['Date'] = df['Date'].shift(periods = 3, freq = 'D')

# ???
# print(df.head(10))
newdf = df.shift(periods = 1, freq = 'D')

# create lag_price column lagging 'Close' by 1 done
# take the difference between lag_price and 'Close'. create that as a new column called diff
# lag that column and regress diff on that column

newdf['lag_price'] = newdf['Close'].shift(1, fill_value = 0)
newdf['delta'] = (newdf['lag_price'] - newdf['Close'])
print(newdf.head(15))
# newdf['lag_price_diff'] = newdf['lag_price'].shift(1, fill_value = 0)
# newdf['lag_diff'] = newdf['lag_price_diff'].shift(1, fill_value = 0)
# print(newdf.head(15))
# reg = sm.OLS(newdf['lag_price_diff'], newdf['lag_diff']) # need x array which is
# results = reg.fit()
# print(results.summary)

# if previous date - current date > 1, fill row with dates in between until next date is reached

def autoregress(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """

    reg = sm.OLS(df['Close'], df['Date'])
    tstat = 3
    return None