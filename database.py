import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

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


def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()

def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    """c.execute('UPDATE stuffToPlot SET value=99 WHERE value=8')
    db.commit()

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]"""

    c.execute('DELETE FROM stuffToPlot WHERE value=99')
    db.commit()
    print(100*'#')

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]


del_and_update()

c.close()
db.close()