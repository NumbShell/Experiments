import sqlite3
import time
import datetime
import random

#Open a database connection
db = sqlite3.connect('example.db')
c = db.cursor()

#Create a table
def create_tabel():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

#Insert a row of data
def data_entry():
    c.execute("INSERT INTO names VALUES(129391239, '')")
    db.commit()
    c.close()
    db.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d &H: %M: %S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    db.commit()


def read_from_db():
    c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='Python'")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)




read_from_db()

"""create_tabel()
data_entry()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)"""
c.close()
db.close()