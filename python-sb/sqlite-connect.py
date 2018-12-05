#!/usr/bin/env python3

''' sqlite3 database connect'''

import sqlite3
'''
   create a database in RAM --> :memory:
'''

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute('''CREATE TABLE stocks (date TEXT, trans TEXT, symbol TEXT, qty REAL, price REAL)''')

# insert many records at a time (tuple)
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
             ('2006-01-05','BUY','RHAT',100,35.14),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

t = ('MSFT', )
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# save changes
conn.commit()

# close
conn.close()