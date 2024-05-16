# Henry Tran
# PSET 6
# ECON 481

import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# exercise 0

def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/<user>/<repo>/blob/main/<filename.py>"

# exercise 1

# set path to auctions.db
path = "C:\\Users\\danny\\Desktop\\481\\auctions.db" # pc
# path = "C:\\Users\\henryswerve\\Desktop\\481\\auctions.db" #laptop

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

def std() -> str:
    """
    Returns standard deviation of bidAmount
    """
    q = """
    SELECT itemID
    , SQRT(SUM(POWER(bidAmount - avg_bid, 2)) / (COUNT(bidAmount) - 1)) AS std
    FROM (
        SELECT itemID, bidAmount
        , AVG(bidAmount) OVER (PARTITION by itemID) AS avg_bid
        FROM bids
        WHERE itemID IN (
            SELECT itemID
            FROM bids
            GROUP BY itemID
            HAVING COUNT(*) >= 2
        ) AND bidAmount IS NOT NULL 
    ) AS bids
    GROUP BY itemID
    """
        
    return q

# exercise 2

def bidder_spend_frac() -> str:
    """
    Returns sql query for bidderName, total_spend,
    total_bids, and spend_frac
    """
    q = """
    SELECT bidderName
    , SUM(CASE WHEN highBidderName = bidderName THEN bidamount ELSE 0 END) AS total_spend
    , SUM(bidAmount) AS total_bids
    , SUM(CASE WHEN highBidderName = bidderName THEN bidamount ELSE 0 END) * 1.0 / SUM(bidAmount) * 1.0 AS spend_frac
    FROM (
        SELECT highBidderName
        , bidderName
        , itemPrice
        , itemID
        , bidAmount
        FROM bids AS b1
        WHERE bidAmount = (
            SELECT MAX(b2.bidAmount)
            FROm bids AS b2
            WHERE b1.itemID = b2.itemID
            AND b1.bidderName =  b2.bidderName
        )
    ) AS bids
    GROUP BY bidderName
    """
    return q

# exercise 3

def min_increment_freq() -> str:
    """
    Returns sql query for the fraction of bids in the database that are
    exactly the minimum bid increment
    """
    q = """
    SELECT SUM(CASE WHEN b2.bidAmount = b.bidAmount + i.bidIncrement THEN 1 ELSE 0 END) * 1.0 / COUNT(b2.bidAmount) AS freq
    FROM bids AS b
    JOIN bids AS b2 ON b.itemID = b2.itemID AND b.bidAmount < b2.bidAmount
    JOIN items AS i on i.itemID = b.itemID
    WHERE i.isBuyNowUsed != 1
    GROUP BY b.itemID
    """

    return q

# exercise 4

def win_perc_by_timestamp() -> str:
    """
    Returns  a sql query for timestamp_bin. Win_perc was omitted
    """
    q = """

    SELECT
    CASE 
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.1 THEN 1
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.2 THEN 2
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.3 THEN 3
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.4 THEN 4
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.5 THEN 5 
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.6 THEN 6
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.7 THEN 7 
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.8 THEN 8
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 0.9 THEN 9
        WHEN (julianday(b.bidTime) - julianday(a.auctionStart)) /
            (julianday(a.auctionEnd) - julianday(a.auctionStart)) <= 1.0 THEN 10 
    END AS timestamp_bin 
    from bids as b
    inner join (
        select itemid, starttime AS auctionStart, endtime AS auctionEnd, 
        julianday(endtime) - julianday(starttime) as length
        from items
    ) as a
    on b.itemid=a.itemid
    """

    return q