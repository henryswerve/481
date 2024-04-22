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
    data = pd.read_csv(directory,
                    #    index_col = 0,
                       parse_dates = True)

    return data

df = load_data()

print(list(df.columns))

# exercise 2
# Please write a function called plot_close which takes the output of load_data() as defined above, as well as an optional start and end date 
# (strings formatted as ‘YYYY-MM-DD’) and plots the closing price of the stock between those dates as a line graph. 
# Please include the date range in the title of the graph. Note that this function needn’t return anything, just plot a graph using matplotlib

import matplotlib.pyplot as plt
# df.columns()

# fig = plt.figure()
# ax = fig.add_subplot()
# graph = ax.plot(df['Close'], color = 'black',
#                 linestyle = 'dashed', marker = 'o')

# dates = df['Date']
# closing = df['Close']
# plt.plot(dates, closing)


# plt.show()

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Some docstrings
    """
    
    df = df.loc[(df['Date'] >= start) & (df['Date'] <= end)]
    fig = plt.figure()
    ax = fig.add_subplot()
    graph = ax.plot(df['Close'], color = 'black',
                    linestyle = '-', marker = '.')

    dates = df['Date']
    closing = df['Close']
    plt.plot(dates, closing)

    showing = plt.show()
    return showing

# print(plot_close(df, '2010-06-29', '2024-04-15'))