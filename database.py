import sqlite3


#Open a database connection
db = sqlite3.connect('example.db')
c = db.cursor()

#Create a table
def create_tabel():
    c.execute('CREATE TABLE IF NOT EXISTS names(name TEXT, age INT)')

#Insert a row of data
def data_entry():
    c.execute("INSERT INTO names VALUES('Max', 23)")
    db.commit()
    c.close()
    db.exit()


create_tabel()
data_entry()