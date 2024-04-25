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
    Reads in Tesla csv from website, and denotes the dates in the csv
    to be the index for the dataframe called directory.
    """
    directory = f'https://lukashager.netlify.app/econ-481/data/TSLA.csv'
    data = pd.read_csv(directory,
                        index_col = 0,
                        parse_dates = ['Date'])
    
    return data

df = load_data()

# print(df)

# exercise 2

import matplotlib.pyplot as plt

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Plots Tesla stock price using matplotlib from df that was passed in 
    from the problem above. It takes in string values that denotes 
    the start and end dates for the plot.
    """
    start = pd.to_datetime([start])
    end = pd.to_datetime([end])
    fig = plt.figure()
    ax = fig.add_subplot()
    graph = ax.plot(df['Close'], color = 'green',
                    linestyle = '-', ms = 0.25,
                    linewidth = 1, marker = 'o')
    ax.set_xlim(start, end)
    ax.set_title("Tesla Stock Prices 2010-2024")
    plt.show()

    return None

# print(plot_close(df, '2010-06-29', '2024-04-15'))

# exercise 3
import statsmodels.api as sm

# newdf = df.shift(periods = 1, freq = 'D')
# df['lag_price'] = df['Close'].shift(1, freq = 'D')

# df['day_diff'] = df.index.to_series().diff().dt.days
# df = df[df['day_diff'] == 1.0]

# df['delta'] = (df['Close'] - df['lag_price'])
# df['lag_delta'] = df['delta'].shift(1, freq = "D")

# # print(newdf)
# reg = sm.OLS(df['delta'], df['lag_delta'], missing = 'drop')
# results = reg.fit(cov_type = 'HC1', use_t = True)
# t_stat = results.tvalues
# print(t_stat)

# logit
# newdf['bool'] = (newdf['lag_price'] > 0).astype(int)
# reg = sm.Logit(newdf['bool'], newdf['lag_price'], missing = 'drop')
# results = reg.fit(method = 'bfgs', use_t = True)
# t_stat = results.tvalues
# print(t_stat)




# print(results.summary())

import statsmodels.api as sm

def autoregress(df: pd.DataFrame) -> float:
    """
    Shifts 'Close' and creates new column called 'lag_price'. Creates new
    column called delta, taking the difference between 'Close' and 'lag_price'.
    It then lags delta and creates new column called 'lag_delta', regresses
    'delta' on 'lag_delta' using OLS and returns the t stat for beta 0 hat.
    """

    df['lag_price'] = df['Close'].shift(1, freq = "D")

    df['day_diff'] = df.index.to_series().diff().dt.days
    df = df[df['day_diff'] == 1.0]

    df['delta'] = (df['Close'] - df['lag_price'])
    df['lag_delta'] = df['delta'].shift(1, freq = "D")

    # print(newdf)
    reg = sm.OLS(df['delta'], df['lag_delta'], missing = 'drop')
    results = reg.fit(cov_type = 'HC1', use_t = True)
    t_stat = results.tvalues
    # print(t_stat)

    return t_stat

print(autoregress(df))

# def autoregress(df: pd.DataFrame) -> float:
#     """
#     Shifts 'Close' and creates new column called 'lag_price'. Creates new
#     column called delta, taking the difference between 'Close' and 'lag_price'.
#     It then lags delta and creates new column called 'lag_delta', regresses
#     'delta' on 'lag_delta' using OLS and returns the t stat for beta 0 hat.
#     """
#     newdf = df.shift(periods = 1, freq = 'D')
#     newdf['lag_price'] = newdf['Close'].shift(1)
#     newdf['delta'] = (newdf['Close'] - newdf['lag_price'])
#     newdf['lag_delta'] = newdf['delta'].shift(1)
#     reg = sm.OLS(newdf['delta'], newdf['lag_delta'], missing = 'drop')
#     results = reg.fit(cov_type = 'HC1', use_t = True)
#     t_stat = results.tvalues

#     return t_stat

# print(autoregress(df))

# exercise 4

# from sklearn.linear_model import LogisticRegression

df['lag_price'] = df['Close'].shift(1)
df['day_diff'] = df.index.to_series().diff().dt.days
df = df[df['day_diff'] == 1.0]

df['delta'] = (df['Close'] - df['lag_price'])
df['lag_delta'] = df['delta'].shift(1)

df['bool'] = (df['lag_price'] > 0).astype(int)
reg = sm.Logit(df['bool'], df['lag_price'], missing = 'drop')
results = reg.fit(method = 'bfgs', use_t = True)
t_stat = results.tvalues
print(t_stat)

    # return t_stat


def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """
    df['Date'] = df.index.to_series()
    df['Date'] = pd.to_datetime(df['Date'])
    df['lag_price'] = df['Close'].shift(1)
    df['day_diff'] = df.index.to_series().diff().dt.days
    df = df[df['day_diff'] == 1.0]

    df['delta'] = (df['Close'] - df['lag_price'])
    df['lag_delta'] = df['delta'].shift(1)

    df['bool'] = (df['lag_price'] > 0).astype(int)
    reg = sm.Logit(df['bool'], df['lag_price'], missing = 'drop')
    results = reg.fit(method = "bfgs", use_t = True)
    t_stat = results.tvalues
    # print(t_stat)

    return t_stat

# print(autoregress_logit(df))

# def autoregress_logit(df: pd.DataFrame) -> float:
#     """
#     Some docstrings.
#     """
#     newdf = df.shift(periods = 1, freq = 'D')
#     newdf['lag_price'] = newdf['Close'].shift(1)
#     newdf['bool'] = (newdf['lag_price'] > 0).astype(int)
#     reg = sm.Logit(newdf['bool'], newdf['lag_price'], missing = 'drop')
#     results = reg.fit(method = 'bfgs', use_t = True)
#     t_stat = results.tvalues

#     return t_stat

# print(autoregress_logit(df))  

# exercise 5

def plot_delta(df: pd.DataFrame) -> None:
    """
    Converts start and end date to datetime objects.
    Plots the change in stock price from Tesla's inception to present.
    Function shifts one down on 'Close and creates a new column 'lag_price'
    It then creates a new column called 'delta' that is takes the 
    difference between 'Close' and 'lag_price'. 
    It then plots 'delta' in blue.
    """
    start = '2010-06-29'
    end = '2024-04-15'
    start = pd.to_datetime([start])
    end = pd.to_datetime([end])
    df['lag_price'] = df['Close'].shift(1, freq = "D")
    df['delta'] = (df['Close'] - df['lag_price'])
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(df['delta'], color = 'blue',
            linestyle = '-', ms = 0.25,
            linewidth = 1, marker = 'o')
    ax.set_xlim(start, end)
    ax.set_title("Tesla Stock Prices Delta 2010-2024")
    plt.show()
    
    return None

# print(plot_delta(df))