# Calculate position status
# January 10, 2018
import sqlite3
import datetime
# import time

# read trades to build position status
conn = sqlite3.connect("trade_record_v2.db")
c = conn.cursor()

query = "SELECT * FROM trades"

c.execute(query)
trades = c.fetchall()

for trade in trades:
    print(trade)

conn.close()
