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

# exercise 2

import matplotlib.pyplot as plt

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Plots Tesla stock price using matplotlib from df that was passed in 
    from the problem above. It takes in string values that denotes 
    the start and end dates for the plot.
    """
    # converts start and end strings to datetime objects
    start = pd.to_datetime([start])
    end = pd.to_datetime([end])
    
    # create plotting environment
    fig = plt.figure()
    ax = fig.add_subplot()

    # create the plot
    graph = ax.plot(df['Close'], color = 'green',
                    linestyle = '-', ms = 0.25,
                    linewidth = 1, marker = 'o')
    
    # sets window
    ax.set_xlim(start, end)
    
    #set x and y axis labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Price")
    ax.set_title("Tesla Stock Prices 2010-2024")

    # plot the plot
    plt.show()

    return None

# print(plot_close(df, '2010-06-29', '2024-04-15'))

# exercise 3

import statsmodels.api as sm

def autoregress(df: pd.DataFrame) -> float:
    """
    Shifts 'Close' and creates new column called 'lag_price'. Creates new
    column called delta, taking the difference between 'Close' and 'lag_price'.
    It then lags delta and creates new column called 'lag_delta', regresses
    'delta' on 'lag_delta' using OLS and returns the t stat for beta 0 hat.
    """

    # shift 'Close' and creates shifted close column
    df['lag_price'] = df['Close'].shift(1)

    # takes difference between close and lagged price
    df['delta'] = (df['Close'] - df['lag_price'])

    # shifts the difference column and creates new column
    df['lag_delta'] = df['delta'].shift(1)

    # takes OLS reg of delta on lag_delta, omitting NAs
    reg = sm.OLS(df['delta'], df['lag_delta'], missing = 'drop')

    # fit the reg and assign it to results
    results = reg.fit(cov_type = 'HC1', use_t = True)

    # get our t stat
    t_stat = results.tvalues

    return t_stat

# print(autoregress(df))

# exercise 4

def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Shifts 'Close' and creates new column called 'lag_price'. Creates new
    column called delta, taking the difference between 'Close' and 'lag_price'.
    Create new column called bool that assigns 1 if row value in delta column > 0,
    else 1 for that column. It then lags delta and creates 
    new column called 'lag_delta', regresses 'bool' on 'lag_delta' 
    using logit reg. and returns the t stat for beta 0 hat.
    """

    # shift 'Close' and creates shifted close column
    df['lag_price'] = df['Close'].shift(1)

    # takes difference between close and lagged price
    df['delta'] = (df['Close'] - df['lag_price'])

    # shifts the difference column and creates new column
    df['lag_delta'] = df['delta'].shift(1)

    # assigns 1 if row value in delta column > 0, else 1 for new bool column
    df['bool'] = (df['delta'] > 0).astype(int)

    # takes logit reg of bool on lag_delta, omitting NAs
    reg = sm.Logit(df['bool'], df['lag_delta'], missing = 'drop')

    # fit logit model
    results = reg.fit(use_t = True)

    # obtain our t stat
    t_stat = results.tvalues
    
    return t_stat

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

    # shifts close column
    df['lag_price'] = df['Close'].shift(1, freq = "D")

    # take difference and creates delta column
    df['delta'] = (df['Close'] - df['lag_price'])

    # set up plotting environment
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(df['delta'], color = 'blue',
            linestyle = '-', ms = 0.25,
            linewidth = 1, marker = 'o')
    
    # set up x, y and title labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Price Change")
    ax.set_title("Tesla Stock Price Changes: 2010-2024")
    
    # plot the plot
    plt.show()
    
    return None

# print(plot_delta(df))