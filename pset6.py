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

# reexplain renaming columns
# join by left, right, inner??
# questions from each exercise specifically

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"

# exercise 1

# set path to auctions.db
path = "C:\\Users\\danny\\Desktop\\481\\auctions.db"
# path = "C:\\Users\\henryswerve\\Desktop\\481\\auctions.db"

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

# we want all std for all itemids?
# misuse of avg function
# not summing across all items...

q = """
SELECT SQRT((n_bids - AVG(n_bids) * (n_bids - AVG(n_bids))) / (COUNT(n_bids) - 1)) AS std
, itemID
FROM (
    SELECT itemID
    , COUNT(itemID) AS n_bids
    FROM bids
    GROUP BY itemID
    HAVING n_bids > 2
    ORDER BY itemID desc
) AS bids;
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

# winning bids meaning only the ones they win? or all bids?
# how to count only their highest bid for an item?
# , (total_spend / total_bids) as spend_frac???

q = """
SELECT biddername
, sum(bidAmount) as total_spend
, max(bidAmount) as total_bids
, (sum(bidAmount) / max(bidAmount)) as spend_frac
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

# exercise 3

# Please write a function called min_increment_freq that takes no arguments and 
# returns a string containing a SQL query that can be run against the auctions.db 
# database that outputs a table that has one column (freq) which represents the 
# fraction of bids in the database that are exactly the minimum bid increment 
# (items.bidIncrement) above the previous high bid. For this exercise, 
# exclude items where isBuyNowUsed = 1.

# q = """
# SELECT *
# FROM items
# WHERE 1 = 2
# """

# shrug
# q = """
# SELECT (b.bidAmount == b.itemPrice) AS freq
# FROM bids as b
# LEFT JOIN items as i
# WHERE isBuyNowUsed != 1
# ORDER BY i.itemID desc
# """

q = """
SELECT COUNT((b.bidAmount == b.itemPrice)) / COUNT(b.itemID) AS freq
, b.itemID
FROM bids as b
LEFT JOIN items as i
WHERE i.isBuyNowUsed != 1
"""
# print(auctions.query(q).head())

def min_increment_freq() -> str:
    """
    Some docstrings.
    """

    return None




# exercise 4
# Please write a function called win_perc_by_timestamp that takes no arguments 
# and returns a string containing a SQL query that can be run against the auctions.db database that outputs a table that has two columns:

# timestamp_bin: Using the same methodology as in the slides to normalize the 
# percentage of time remaining in the auction when a bid is placed, 
# normalize the bid timestamp and classify it as one of ten bins: 
# 1 corresponds to 0-.1, 2 corresponds to .1-.2, etc.
# win_perc: the frequency with which a bid placed with this timestamp
#  bin won the auction.


# how to create new column for timestamp_bin? has to be better way to iterate this over all the end and start times


# q = """
# select b.itemid, b.bidtime, a.starttime, a.endtime,
# (julianday(endtime)-julianday(bidtime)) / a.length as time_norm,
# timestamp_bin
# from bids as b
# inner join (
#     select itemid, starttime, endtime, 
#     julianday(endtime) - julianday(starttime) as length,
#     case when (julianday(endtime) - julianday(starttime)) <= 1 then 1
#     when (julianday(endtime) - julianday(starttime)) <= 2 and (julianday(endtime) - julianday(starttime)) > 1 then 2
#     else 0 end as timestamp_bin
#     from items
# ) as a
# on b.itemid=a.itemid
# """

# idk man

q = """
select b.itemid, b.bidtime, a.starttime, a.endtime,
(julianday(a.endtime)-julianday(b.bidtime)) / a.length as time_norm,
case when (julianday(a.endtime) - julianday(a.starttime)) < 1 AND (julianday(a.endtime) - julianday(a.starttime)) >= 0 then 1 
when (julianday(a.endtime) - julianday(a.starttime)) < 2 AND (julianday(a.endtime) - julianday(a.starttime)) >= 1 then 2
when (julianday(a.endtime) - julianday(a.starttime)) < 3 AND (julianday(a.endtime) - julianday(a.starttime)) >= 2 then 3 else 0 end as timestamp_bin
from bids as b
inner join (
    select itemid, starttime, endtime, 
    julianday(endtime) - julianday(starttime) as length
    from items
) as a
on b.itemid=a.itemid;
"""



print(auctions.query(q).head())

def win_perc_by_timestamp() -> str:
    """
    Some docstrings.
    """

    return None