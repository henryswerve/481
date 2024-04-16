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

# print(n_null(df, "FRS ID (FACILITY)"))

# to be considered: FRS Id good choice to join data? sure

# exercise 4

# joined_data = emissions_data.join(parent_data, how = 'left')
# joined_data = pd.merge(emissions_data, parent_data, left_on = 'FRS Id', right_on = 'FRS ID (FACILITY)')
# print(sorted(emissions_data))
# print(sorted(parent_data))
# print(joined_data)

# joined_data = emissions_data.join(parent_data, how = 'left')

# how am i supopsed to merge by year and frs id? create new column called year?
# what is meant by subset? I tried doing it and i end up with the same amount of columns as before I subsetted

# joined_data = pd.merge(emissions_data, parent_data, left_on = ['FRS Id'],  right_on = ['FRS ID (FACILITY)'])

# ????????
# joined_data = pd.merge(emissions_data, parent_data, left_on = ['year', 'FRS Id'],  right_on = ['REPORTING YEAR', 'FRS ID (FACILITY)'])

# print(emissions_data.columns)
# print(parent_data.columns)
# print(joined_data.head(10))
# print(joined_data.columns)

# joined_data = joined_data.loc[joined_data[['Facility Id', 'REPORTING YEAR', 'State where Emissions Occur', 
#                                                     'Industry Type (subparts)', 'Total reported direct emissions from Local Distribution Companies',
#                                                     'PARENT CO. STATE', 'PARENT CO. PERCENT OWNERSHIP']]]

#     raise ValueError("Cannot index with multidimensional key")
# ValueError: Cannot index with multidimensional key

# joined_data = joined_data.loc[
#     (~pd.isna(joined_data['Facility Id'])) &
#     (~pd.isna(joined_data['REPORTING YEAR'])) &
#     (~pd.isna(joined_data['State where Emissions Occur'])) &
#     (~pd.isna(joined_data['Industry Type (subparts)'])) &
#     (~pd.isna(joined_data['Total reported direct emissions from Local Distribution Companies'])) &
#     (~pd.isna(joined_data['PARENT CO. STATE'])) &
#     (~pd.isna(joined_data['PARENT CO. PERCENT OWNERSHIP']))
# ]

# print(joined_data.columns)
# print(joined_data.head(15))


# profs = ['Melissa Knox', 'Yael Jacobs', 'Fahad Khalil']
# data_subset = data_2023.loc[
#     data_2023['Instructor'].isin(profs) & 
#     (data_2023['Course'].str.get(5) == '4')
# ]

# subset ex. from notes

# subset_names = ['Facility Id', 'year', 'Reported State', 'Industry Type (subsets)', 
#                 'Total reported direct emissions from Local Distribution Companies', 
#                 'PARENT CO. STATE', 'PARENT CO. PERCENT OWNERSHIP']

# data_subset = joined_data.loc[
#     joined_data['']
# ]

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

# print(clean_data(emissions_data, parent_data))
df = clean_data(emissions_data, parent_data)
group_vars = ['TX'] # can also be blank, meaning take mean over whole df
# exercise 5

def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    # just use df.describe for min, med., mean and max.
    # sort highest to lowest mean total reported direct emissions
    # use df.groupby('blah blah')

    if group_vars.str.match('[A-ZA-Z]'):
        # look at total reported direct emissions, parent co. percent ownership
        # at the state level
        else:
        

    return None