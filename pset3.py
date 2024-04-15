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

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Takes excel file, skips the first three rows appends each sheet to an empty
    list called dfs in which we concatenate the then populated dfs list to return
    as data_output
    """
    dfs = []
    for year in years:
        directory = f'C:\\Users\\danny\\Downloads\\ghgp_data_{year}.xlsx'
        # for desktop directory
        # directory = f'C:\\Users\\henryswerve\\Downloads\\ghgp_data{year}.xlsx'
        data = pd.read_excel(directory, 'LDC - Direct Emissions', skiprows = 3)
        dfs.append(data)
        data_output = pd.concat(dfs, ignore_index = True)
        # create a df for each year of direct emitters tab
        # dont use any columns as the index
        # do not import first three rows

    return data_output

emissions_data = import_yearly_data(years)

# exercise 2 done

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 
         2017, 2018, 2019, 2020, 2021, 2022]
# directory = f'C:\\Users\\danny\\Downloads\\ghgp_data_parent_company_09_2023.xlsb'

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    dfs = []
    for year in years:
        directory = f'C:\\Users\\danny\\Downloads\\ghgp_data_parent_company_09_2023.xlsb'
        # for desktop directory
        # directory = f'C:\\Users\\henryswerve\\Downloads\\ghgp_data_parent_company_09_2023.xlsb'
        data = pd.read_excel(directory, str(year))
        data = data.replace(r'', pd.NaT)
        data = data.dropna()
        dfs.append(data)
        data_output = pd.concat(dfs, ignore_index = True)
    return data_output

parent_data = import_parent_companies(years)

# exercise 3 done

df = f'C:\\Users\\danny\\Downloads\\ghgp_data_parent_company_09_2023.xlsb' # desktop
# df = f'C:\\Users\\henryswerve\\Downloads\\ghgp_data_parent_company_09_2023.xlsb' # laptop

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

# print(n_null(df, "FRS ID (FACILITY)"))

# to be considered: FRS Id good choice to join data? sure

# exercise 4

# what's a good visual way to check if the join is right?

# joined_data = emissions_data.join(parent_data, how = 'left')
# joined_data = pd.merge(emissions_data, parent_data, left_on = 'FRS Id', right_on = 'FRS ID (FACILITY)')
# print(sorted(emissions_data))
# print(sorted(parent_data))
print(joined_data)

def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Some docstrings.
    """

    # left join parent companies data onto the EPA data using as join keys the year and facility ID
    # variables in the emissions data and their equivalents in the parent companies data
    # left on year and facility ID

    return None

# exercise 5

def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Some docstrings.
    """

    return None