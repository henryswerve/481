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
    as data_output
    """
    dfs = []
    for year in years:
        # directory = f'C:\\Users\\danny\\Downloads\\ghgp_data_{year}.xlsx'
        # for desktop directory
        directory = f'C:\\Users\\henryswerve\\Downloads\\ghgp_data{year}.xlsx'
        data = pd.read_excel(directory, 'LDC - Direct Emissions', skiprows = 3)
        dfs.append(data)
        data_output = pd.concat(dfs, ignore_index = True)
        # create a df for each year of direct emitters tab
        # dont use any columns as the index
        # do not import first three rows

    return data_output

# print(import_yearly_data(years))

# exercise 2

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 
         2017, 2018, 2019, 2020, 2021, 2022]
# directory = f'C:\\Users\\danny\\Downloads\\ghgp_data_parent_company_09_2023.xlsb'
# print(pd.read_excel(directory))


# as dictionary, can't easily do pd.df.dropna... where where do None for our second argument
# 

# def import_parent_companies(years: list) -> pd.DataFrame:
#     """
#     Some docstrings.
#     """
#     for year in years:
#         directory = f'C:\\Users\\danny\\Downloads\\ghgp_data_parent_company_09_2023.xlsb'
#         dict_of_data = pd.read_excel(directory, None, keep_default_na= False)
#         for k, v in dict_of_data.items():
#             v['Year'] = k
#         # dict_of_data = pd.DataFrame(dict_of_data)
#         # dict_of_data.dropna()
#         data_output = pd.concat(dict_of_data, ignore_index = True)
#     return data_output

# print(import_parent_companies(years))

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    dfs = []
    for year in years:
        # directory = f'C:\\Users\\danny\\Downloads\\ghgp_data_parent_company_09_2023.xlsb'
        # for desktop directory
        directory = f'C:\\Users\\henryswerve\\Downloads\\ghgp_data_parent_company_09_2023.xlsb'
        data = pd.read_excel(directory, str(year))
        data = data.replace(r'', pd.NaT)
        data = data.dropna()
        dfs.append(data)
        data_output = pd.concat(dfs, ignore_index = True)
    return data_output

print(import_parent_companies(years))

# exercise 3