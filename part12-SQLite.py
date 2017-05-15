#! usr/bin/python

# create something that looks and works like a database server without the need
# of actually creating one
import sqlite3


#createDB = sqlite3.connect('sample.db')

createDB = sqlite3.connect(':memory:')

queryCurs = createDB.cursor()

# Creates the table
def createTable():
    # This is an SQL cammand / statement
    # execute the SQl command
    # primary key automatically generates a unique number
    queryCurs.execute('''CREATE TABLE customers
    (id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT, state TEXT, balance REAL)''')

    

def addCust(name,street,city,state,balance):
    queryCurs.execute('''INSERT INTO customers (name,street,city,state,balance)
    VALUES(?,?,?,?,?)''', (name,street,city,state,balance))

def main():
    createTable()
    
    addCust('Bob The Builder', '123 Imaginary road', 'neverland', "PA", 13.37)
    addCust('Tommas The Train', '456 Imaginary road', 'whereare', "PA", 14.37)
    addCust('Wazzup Guy', '789 Imaginary road', 'thoughtoday', "PA", 15.37)
    addCust('WTF guy', '9102 Imaginary road', 'forevernever', "PA", 16.37)
    
    # force database to make changes
    createDB.commit()
    
    
    
    # Add column to table for emails
    queryCurs.execute('ALTER TABLE customers ADD COLUMN email TEXT')
    
    # Add email address to customer
    queryCurs.execute('UPDATE customers SET email="wazup@gmail.com" WHERE id=1')
    
    # Delete email address of a customer
    queryCurs.execute('DELETE FROM customers WHERE id=4')
    
    # Print customers ordered by lowest balance and with titles 
    queryCurs.execute('SELECT * FROM customers ORDER BY balance DESC, name LIMIT 2 OFFSET 1 ')
    
    
    #queryCurs will now hold all the values
    #the star means from all
    #queryCurs.execute('SELECT * FROM customers ORDER BY balance')
    
    listTitle = ['ID Num ', 'Name ', 'Street ', 'City ', 'State ', 'Balance ', 'Email']
    k = 0
    
    for i in queryCurs:
        print "\n"
        for j in i:
            print listTitle[k],
            print j
            if k < 6: k+=1
            else: k = 0
            
    queryCurs.close()

if __name__ == '__main__': main()