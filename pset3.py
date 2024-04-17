# Henry Tran
# Econ 481
# Pset 3


# exercise 0

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/henryswerve/481/blob/main/pset3.py"

# exercise 1 done

import pandas as pd

years = [2019, 2020, 2021, 2022]

# create year variable, evrey time you call a year, it creates a column


def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Takes excel file, skips the first three rows appends each sheet to an empty
    list called dfs in which we concatenate the then populated dfs list to return
    as data_output. Then we create year column that is in line with each year from the excel files
    """
    dfs = []
    for year in years:
        directory = f'https://lukashager.netlify.app/econ-481/data/ghgp_data_{year}.xlsx'
        data = pd.read_excel(directory, 'LDC - Direct Emissions', skiprows = 3).assign(year = year)
        dfs.append(data)
        data_output = pd.concat(dfs, ignore_index = True)
    return data_output

emissions_data = import_yearly_data(years)

# print(emissions_data)

# exercise 2 done

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 
         2017, 2018, 2019, 2020, 2021, 2022]

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    dfs = []
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 
         2017, 2018, 2019, 2020, 2021, 2022]
    for year in years:
        directory = f'https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb'
        data = pd.read_excel(directory, str(year)).assign(year = year)
        data = data.replace(r'', pd.NaT)
        data = data.dropna()
        dfs.append(data)
        data_output = pd.concat(dfs, ignore_index = True)
    return data_output

parent_data = import_parent_companies(years)
# print(parent_data)

# exercise 3 done

df = 'https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb'

def n_null(df: pd.DataFrame, col: str) -> int:
    """
    Some docstrings
    """
    # has to choose sheet and a column for given df and count # of nas in a given column
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 
         2017, 2018, 2019, 2020, 2021, 2022]
    for year in years:
        data = pd.read_excel(df, str(year))
        data = data.replace(r'', pd.NaT)
        na_count = data[col].isna().sum()
    return na_count

ex_4 = n_null(df, "FRS ID (FACILITY)")

# to be considered: FRS Id good choice to join data? sure

# exercise 4

def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Some docstrings.
    """
    joined_data = pd.merge(emissions_data, parent_data, left_on = ['year', 'FRS Id'],  
                       right_on = ['year', 'FRS ID (FACILITY)'])
    
    joined_data = joined_data.loc[
        (~pd.isna(joined_data['Facility Id'])) &
        (~pd.isna(joined_data['REPORTING YEAR'])) &
        (~pd.isna(joined_data['State where Emissions Occur'])) &
        (~pd.isna(joined_data['Industry Type (subparts)'])) &
        (~pd.isna(joined_data['Total reported direct emissions from Local Distribution Companies'])) &
        (~pd.isna(joined_data['PARENT CO. STATE'])) &
        (~pd.isna(joined_data['PARENT CO. PERCENT OWNERSHIP']))
    ]

    returned_df = joined_data[['Facility Id', 'year', 'State where Emissions Occur',
                                'Industry Type (subparts)',
                                'Total reported direct emissions from Local Distribution Companies',
                                'PARENT CO. STATE', 'PARENT CO. PERCENT OWNERSHIP']]
    
    returned_df.columns = returned_df.columns.str.lower()

    return returned_df

df = clean_data(emissions_data, parent_data)
print(df['total reported direct emissions from local distribution companies'].describe())
print(df['parent co. percent ownership'].describe())

# group_vars = [state, year...]
# given those variables, take the summary of the ones listed
# in exercise 5 online

# exercise 5

def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    # just use df.describe for min, med., mean and max.
    # sort highest to lowest mean total reported direct emissions
    # use df.groupby('blah blah')

    if group_vars['state']:
        a = b
        # look at total reported direct emissions, parent co. percent ownership
        # at the state level
    elif group_vars['facility id']:
        b = a
    elif group_vars['industry type (subparts)']:
    

    # df['total reported direct emissions from local distribution companies'].describe()
    # df['parent co. percent ownership'].describe()

    return None