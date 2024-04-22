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
# Please write a function called plot_close which takes the output of load_data() as defined above, as well as an optional start and end date 
# (strings formatted as ‘YYYY-MM-DD’) and plots the closing price of the stock between those dates as a line graph. 
# Please include the date range in the title of the graph. Note that this function needn’t return anything, just plot a graph using matplotlib

import matplotlib.pyplot as plt

# print(df)

start = '2010-06-29'
end = '2024-04-15'
data = df.reset_index()
start_date = list(df['Date'])
close_price = list(df['Close'])

plt.plot(start_date, close_price)



def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Some docstrings
    """
    start = '2010-06-29'
    end = '2024-04-15'
    data = df.reset_index()
    start_date = list(df['Date'])
    close_price = list(df['Close'])

    closed_plot = plt.plot(start_date, close_price)
    
    return closed_plot

print(plot_close(df, '2010-06-29', '2024-04-15'))