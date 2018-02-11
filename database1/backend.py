import sqlite3

def connect():
    connec = sqlite3.connect("books.db")
    curs = connec.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
    connec.commit()
    connec.close()

def insert(title, author):
    connec = sqlite3.connect("books.db")
    curs = connec.cursor()
    curs.execute("INSERT INTO book VALUES (NULL, ?, ?)", (title, author))
    connec.commit()
    connec.close()

def view():
    connec = sqlite3.connect("books.db")
    curs = connec.cursor()
    curs.execute("SELECT * FROM book")
    rows = curs.fetchall()
    connec.commit()
    connec.close()
    return rows

def search(title="", author=""):
    connec = sqlite3.connect("books.db")
    curs = connec.cursor()
    curs.execute("SELECT * FROM book WHERE title=? OR author=?", (title, author))
    rows = curs.fetchall()
    connec.commit()
    connec.close()
    return rows

def delete(id):
    connec = sqlite3.connect("books.db")
    curs = connec.cursor()
    curs.execute("DELETE FROM book WHERE id = ?", (id,))
    connec.commit()
    connec.close()

def update(id, title, author):
    connec = sqlite3.connect("books.db")
    curs = connec.cursor()
    curs.execute("UPDATE book SET title = ?, author = ? WHERE id = ?",(title, author, id))
    connec.commit()
    connec.close()


connect()
#insert("bro", "there")
#search("hi")
#print(view())
