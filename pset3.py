# Henry Tran
# Econ 481
# Pset 3

# exercise 0

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/henryswerve/481/blob/main/pset3.py"

# exercise 1

import pandas as pd

years = [2019, 2020, 2021, 2022]

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Takes excel file, skips the first three rows appends each sheet to an empty
    list called dfs in which we concatenate the then populated dfs list to return
    as data_output. Then we create year column that matches each year from the excel files
    """
    dfs = []
    for year in years:
        directory = f'https://lukashager.netlify.app/econ-481/data/ghgp_data_{year}.xlsx'
        data = pd.read_excel(directory, 'Direct Emitters', skiprows = 3).assign(year = year)
        dfs.append(data)
        data_output = pd.concat(dfs, ignore_index = True)
    return data_output

emissions_data = import_yearly_data(years)

# exercise 2

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 
         2017, 2018, 2019, 2020, 2021, 2022]

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Passes through years, a list of all the years on each of the sheets in the parent 
    company excel file. For each of those years, read in the file and create a new column
    called year that tracks which year a row is from. We then replace all blanks with an NA,
    and drop those Nas in which we append the dataframe to an empty list called dfs.
    We then use pd.concat to combine the dataframes and return the overall combined dataframe 
    from the pd.concat.
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

df = 'https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb'

# exercise 3

def n_null(df: pd.DataFrame, col: str) -> int:
    """
    Passes through df (excel file) and the column name to determine
    how many NAs are present for that column.
    For all the years in the years list, read the excel file,
    replace every blank with an NA value and count the number of nas for each column
    and then return that na count. 
    """
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 
         2017, 2018, 2019, 2020, 2021, 2022]
    for year in years:
        data = pd.read_excel(df, str(year))
        data = data.replace(r'', pd.NaT)
        na_count = data[col].isna().sum()
    return na_count

# print(n_null(df, 'FRS ID (FACILITY)'))

# to be considered: FRS Id good choice to join data? perchance

# exercise 4

def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Passes through dataframes from exercise 1 and 2 to then be merged by year and 
    facility ID. The function then subsets the data based on the requirments from the
    exercise, and finally decapitalizes the column names and returns the dataframe.
    """
    joined_data = pd.merge(emissions_data, parent_data, left_on = ['year', 'FRS Id'],  
                       right_on = ['year', 'FRS ID (FACILITY)'])
    joined_data = joined_data.loc[
        (~pd.isna(joined_data['Facility Id'])) &
        (~pd.isna(joined_data['year'])) &
        (~pd.isna(joined_data['State'])) &
        (~pd.isna(joined_data['Industry Type (sectors)'])) &
        (~pd.isna(joined_data['Total reported direct emissions'])) &
        (~pd.isna(joined_data['PARENT CO. STATE'])) &
        (~pd.isna(joined_data['PARENT CO. PERCENT OWNERSHIP']))
    ]
    returned_df = joined_data[['Facility Id', 'year', 'State',
                                'Industry Type (sectors)',
                                'Total reported direct emissions',
                                'PARENT CO. STATE', 'PARENT CO. PERCENT OWNERSHIP']]
    returned_df.columns = returned_df.columns.str.lower()

    return returned_df

df = clean_data(emissions_data, parent_data)

# print(df)

group_vars = ['state', 'year']

# exercise 5

def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Passes through df from exercise four and group_vars, a list that specifies
    which columns to take the mean for. stats groups based on the elements
    from group_vars, takes the mean of the columns required from the exercise,
    sorts the values from highest to lowest mean and returns a dataframe of these values
    """
    stats = df.groupby(group_vars, as_index = True).mean(['total reported direct emissions from local distribution companies',
                                                          'parent co. percent ownership'])
    stats = stats.sort_values(by = group_vars, ascending = False)

    return stats

# print(aggregate_emissions(df, group_vars).head(5))