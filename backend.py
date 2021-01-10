import sqlite3

# the below files contains each and every function 
def connect():
    connection  = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id  INTEGER PRIMARY KEY,title text, Author text,year integer,isbn integer)")
    connection.commit()
    connection.close()
    

def insert(title,Author,year,isbn):
    connection  = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,Author,year,isbn))
    connection.commit()
    connection.close()
    
def view():
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("select * from book")
    rows = cur.fetchall()
    connection.close()
    return rows

def search(title="",Author="",year="",isbn=""): # we will be passing an empty string here
    
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("select * from book where title = ? or author =? or year = ? or isbn = ?",(title,Author,year,isbn))
    rows = cur.fetchall()
    connection.close()
    return rows

def delete(id): # this function will only be taking the id which is unique to each block of data
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("Delete from book where id = ?",(id,))
    connection.commit()
    connection.close()
    
def update(id,title,Author,year,isbn):
    
    connection = sqlite3.connect("books.db")
    cur = connection.cursor()
    cur.execute("Update book set title = ? or author =? or year = ? or isbn = ? where id = ?",(title,Author,year,isbn,id))
    connection.commit()
    connection.close()


connect() # inititaiting connect function is very important otherwise module functions will not get imported


    