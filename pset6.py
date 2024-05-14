# Henry Tran
# PSET 6
# ECON 481

import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import Session

# exercise 0

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"

# exercise 1

# set path to auctions.db
path = "C:\\Users\\danny\\Desktop\\481\\auctions.db"

# # initialize the engine
# engine = create_engine(f'sqlite:///{path}')

# inspect the table for names
# inspector = inspect(engine)
# inspector.get_table_names()

# create the query class
class DataBase:
    def __init__(self, loc: str, db_type: str = "sqlite") -> None:
        """Initialize the class and connect to the database"""
        self.loc = loc
        self.db_type = db_type
        self.engine = create_engine(f'{self.db_type}:///{self.loc}')
    def query(self, q: str) -> pd.DataFrame:
        """Run a query against the database and return a DataFrame"""
        with Session(self.engine) as session:
            df = pd.read_sql(q, session.bind)
        return(df)

# assign the query class to auction
auctions = DataBase(path)

# exercise 1
# Please write a function called std that takes no arguments and returns
# a string containing a SQL query that can be run against the 
# auctions.db database that outputs a table that has two columns: 
# itemId and std, the standard deviation of bids for that item. 
# Include only bids for which the unbiased standard deviation 
# can be calculated (that is, those with at least two bids). 


def std() -> str:
    """
    Some docstrings.
    """
    q = 'select itemId, quantity from bids'
    
    print(auctions.query(q).head())
    sd = ''
    return None

q = """
SELECT COUNT(*) as n_bids
, itemID
FROM bids
GROUP BY itemID
ORDER by n_bids asc
"""

# print(auctions.query(q).head(10))

# exercise 2
# Please write a function called bidder_spend_frac that takes no arguments and 
# returns a string containing a SQL query that can be run against the auctions.db 
# database that outputs a table that has four columns:
# bidderName: the name of the bidder
# total_spend: the amount the bidder spent (that is, the sum of their winning bids)
# total_bids: the amount the bidder bid, regardless of the outcome. 
# NB: bidders may submit multiple bids for an item – if this is the case only count their 
# highest bid for an item for this calculation.
# spend_frac: total_spend/total_bids

# need total_bids?
# need spend_frac

# winning bids meaning only the ones they win? or all bids?
# , (total_spend / total_bids) as spend_frac???


q = """
SELECT biddername
, sum(bidAmount) as total_spend
, max(bidAmount) as total_bids
, (total_spend / total_bids) as spend_frac
FROM bids
WHERE bidAmount is not null
GROUP BY biddername
"""

# print(auctions.query(q).head())

def bidder_spend_frac() -> str:
    """
    Some docstrings.
    """

    return None