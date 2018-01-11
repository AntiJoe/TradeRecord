# Trade Record...  January 9, 2018
# Build sqlite db for trades and stocks

import sqlite3
import datetime
import time


conn = sqlite3.connect('trade_record_v2.db')
# conn = sqlite3.connect("test3.db")
c = conn.cursor()

# Create table

c.execute('''CREATE TABLE trades
         (Name text,
         ticker text,
         direction int,
         entryDate text,
         long int,
         price real,
         shares real,
         account text)''')

c.execute('''CREATE TABLE positions
         (Name text,
         ticker text,
         direction int,
         entryDate text,
         long int,
         price real,
         shares real)''')

conn.commit()
# c.execute('''
#
# ''')

# Insert a row of data
c.execute("INSERT INTO trades VALUES ('Enbridge', 'ENB.to', 'long', '2017-11-14', 200, 45.11, 'CAD', 'TDRSP')")
c.execute("INSERT INTO trades VALUES ('REIT', 'UN.to', 'long', '2017-11-15', 800, 11.41, 'CAD', 'TDRSP')")
c.execute("INSERT INTO trades VALUES ('Patriot', 'PAT.V', 'long', '2017-12-13', 4000, 1.17, 'CAD', 'TDRSP')")
c.execute("INSERT INTO trades VALUES ('Tesla', 'TSLA', 'long', '2018-1-4', 20, 313.60, 'US', 'TDRSP')")

conn.commit()