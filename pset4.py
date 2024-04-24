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
# newdf = df.shift(periods = 1, freq = 'D')

# create lag_price column lagging 'Close' by 1 done
# take the difference between lag_price and 'Close'. create that as a new column called diff
# lag that column and regress diff on that column

# newdf['lag_price'] = newdf['Close'].shift(1, fill_value = 0)
# newdf['delta'] = (newdf['Close'] - newdf['lag_price'])
# newdf['lag_delta'] = newdf['delta'].shift(1, fill_value = 0)
# print(newdf.head(15))

# reg = sm.OLS(newdf['delta'], newdf['lag_delta'])
# results = reg.fit(cov_type = 'HC1', use_t = True)
# results_summary = results.summary()
# t_stat = results.tvalues
# print(results_summary)
# print(t_stat)

# if previous date - current date > 1, fill row with dates in between until next date is reached

def autoregress(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """
    newdf = df.shift(periods = 1, freq = 'D')
    newdf['lag_price'] = newdf['Close'].shift(1, fill_value = 0)
    newdf['delta'] = (newdf['Close'] - newdf['lag_price'])
    newdf['lag_delta'] = newdf['delta'].shift(1, fill_value = 0)

    reg = sm.OLS(newdf['delta'], newdf['lag_delta'])
    results = reg.fit(cov_type = 'HC1', use_t = True)
    t_stat = results.tvalues
    return t_stat

# print(autoregress(df))

# exercise 4

from sklearn.linear_model import LogisticRegression
import numpy as np



newdf = df.shift(periods = 1, freq = 'D')
newdf['lag_price'] = newdf['Close'].shift(1, fill_value = 0)
newdf['delta'] = (newdf['Close'] - newdf['lag_price'])
newdf['lag_delta'] = newdf['delta'].shift(1, fill_value = 0)
newdf['logistic'] = newdf['delta'] - newdf['lag_delta']

newdf['bool'] = (newdf['logistic'] > 0).astype(int)
# print(newdf.head(15))


# print(newdf.head(5))

model = LogisticRegression()

# print(list(newdf.columns))

# exogenous = pd.DataFrame(newdf['logistic'])
# exogenous = exogenous.flatten()
# endogenous = pd.DataFrame(newdf['bool'])

# below works for scikit learn... not statsmodels
# exogenous = np.array(newdf['logistic'])
# exogenous = exogenous.reshape(-1, 1)
# endogenous = np.array(newdf['bool'])
# print(exogenous.shape)
# print(endogenous.shape)

# log_reg = model.fit(exogenous, endogenous)


endogenous = newdf['logistic'].reshape(-1, 1)
reg = sm.Logit(newdf['logistic'], newdf['bool'])
results = reg.fit(use_t = True)
t_stat = results.tvalues

# reg = sm.Logit('delta ~ lag_delta', data = newdf)
# reg = sm.Logit(newdf['delta'], newdf['lag_delta'])
# results = reg.fit(use_t = True)
# t_stat = results.tvalues

    # return t_stat


# func throws error
def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """
    newdf = df.shift(periods = 1, freq = 'D')
    newdf['lag_price'] = newdf['Close'].shift(1, fill_value = 0)
    newdf['delta'] = (newdf['Close'] - newdf['lag_price'])
    newdf['lag_delta'] = newdf['delta'].shift(1, fill_value = 0)

    endogenous = pd.array(newdf['lag_delta'])

    # reg = sm.Logit('delta ~ lag_delta', data = newdf)
    reg = sm.Logit(newdf['delta'], newdf['lag_delta'])
    results = reg.fit(use_t = True)
    t_stat = results.tvalues

    return t_stat

# print(autoregress_logit(df))