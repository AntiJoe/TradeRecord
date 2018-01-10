# Trade Record...  January 9, 2018
# Build sqlite db for trades and stocks

import sqlite3
import datetime
import time


conn = sqlite3.connect('trade_record_v1.db')
# conn = sqlite3.connect("test3.db")
c = conn.cursor()

# Create table

# c.execute('''CREATE TABLE trades
#          (Name text,
#          ticker text,
#          BatchID int,
#          EntryDate text,
#          long int,
#          price real,
#          shares real)''')

# c.execute('''
#
# ''')

# Insert a row of data
# c.execute("INSERT INTO pulpeye VALUES ('Line 1', 1, 12, '2018-01-04 8:00:01', 124,1.56, 412)")
# c.execute("INSERT INTO pulpeye VALUES ('Line 2', 2, 13, '2018-01-04 8:07:02', 134,1.66, 367)")
# c.execute("CREATE UNIQUE INDEX batchindex ON pulpeye (BatchID)")


conn.commit()